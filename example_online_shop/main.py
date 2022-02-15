import requests
from pprint import pprint
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DecimalField, FileField
from wtforms.validators import DataRequired
from typing import Callable
import sqlite3

# First time run
# db = sqlite3.connect("shop-items-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, item_name varchar(250) NOT NULL UNIQUE, item_description varchar(500) NOT NULL, price INTEGER NOT NULL, rating FLOAT NULL, item_image varchar(250) NULL, sale INTEGER NULL)")
# # Sale would be a Boolean represented as 1(true) or 0(false)
# db.commit()

UPLOAD_FOLDER = "static/uploads"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop-items-collection.db'
app.config['SECRET_KEY'] = 'N6NnTBUUxTxrovGfBjEU'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

admin_key = "Sj89SJSIJdsa4sda64"

class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable
    Float: Callable

db = MySQLAlchemy(app)

Bootstrap(app)

class ShopItem(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(250), unique=True, nullable=False)
    item_description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    item_image = db.Column(db.String(250), nullable=True)
    sale = db.Column(db.Integer, nullable=True)


class NewItemForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    item_description = StringField('Description of Item', validators=[DataRequired()])
    price = DecimalField('Price', places=2, rounding=None, validators=[DataRequired()])
    rating = DecimalField('Rating (from 0.0 to 5.0)', places=1, rounding=None, validators=[DataRequired()])
    item_image = FileField('Select Image for Item')
    sale = SelectField('Item on Sale?', choices=["Yes", "No"])
    submit = SubmitField('Submit')


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/all")
def all_items():
    items = db.session.query(ShopItem).all()
    return render_template("all_items.html", items=items)


# Would need a better way to add and delete items from the database without a key like this
# Need to figure out how to save images to database
# Need to add edit route
# Need to be able to add stuff to the cart and view the item by itself
@app.route(f"/add/{admin_key}", methods=["GET", "POST"])
def add():
    form = NewItemForm()
    if form.validate_on_submit():
        if request.form.get("sale") == "Yes":
            sale = 1
        elif request.form.get("sale") == "No":
            sale = 0
        new_item = ShopItem(
            item_name = request.form.get("item_name"),
            item_description = request.form.get("item_description"),
            price = request.form.get("price"),
            rating = request.form.get("rating"),
            item_image = request.form.get("item_image"),
            sale = sale,
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_item.html", form=form)


@app.route(f"/delete/{admin_key}/<item_name>", methods=["DELETE"])
def delete(item_name):
    item_to_delete = db.session.query(ShopItem).get(item_name)
    if item_to_delete:
        db.session.delete(item_to_delete)
        db.session.commit()
        return jsonify({"success": "Successfully removed the item from the database!"}), 200
    else:
        return jsonify(error={"Not Found": "Sorry, that item is not in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
