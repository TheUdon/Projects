from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import random
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
import sqlite3

app = Flask(__name__)

##Connect to Database
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable
    Float: Callable
    Boolean: Callable

db = MySQLAlchemy(app)

Bootstrap(app)

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location', validators=[DataRequired()])
    url = StringField('Google Maps (URL)', validators=[DataRequired(), URL(message="Invalid URL")])
    img_url = StringField('Photo of Cafe (URL)', validators=[DataRequired(), URL(message="Invalid URL")])
    coffee_price = StringField('How much is a coffee?', validators=[DataRequired()])
    power_socket = SelectField('Has a Power Sockets', choices=["Yes", "No"], validators=[DataRequired()])
    wifi = SelectField('Has a Wifi', choices=["Yes", "No"], validators=[DataRequired()])
    toilet = SelectField('Has a Bathroom', choices=["Yes", "No"], validators=[DataRequired()])
    calls = SelectField('Can Take Calls', choices=["Yes", "No"], validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print(request.form["cafe"])
        if request.form.get("power_socket") == "Yes":
            has_sockets = 1
        elif request.form.get("power_socket") == "No":
            has_sockets = 0
        if request.form.get("toilet") == "Yes":
            has_toilet = 1
        elif request.form.get("toilet") == "No":
            has_toilet = 0
        if request.form.get("wifi") == "Yes":
            has_wifi = 1
        elif request.form.get("wifi") == "No":
            has_wifi = 0
        if request.form.get("calls") == "Yes":
            can_take_calls = 1
        elif request.form.get("calls") == "No":
            can_take_calls = 0
        new_cafe = Cafe(
            name=request.form.get("cafe"),
            map_url=request.form.get("url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=has_sockets,
            has_toilet=has_toilet,
            has_wifi=has_wifi,
            can_take_calls=can_take_calls,
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    cafe_dict = {}
    try:
        connection = sqlite3.connect('cafes.db')
        cursor = connection.cursor()

        sqlite_select_query = """SELECT * from cafe"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            cafe = {}
            cafe["name"] = row[1]
            cafe["url"] = row[2]
            cafe["location"] = row[4]
            if row[5] == 1:
                cafe["Has Sockets"] = "Yes"
            elif row[5] == 0:
                cafe["Has Sockets"] = "No"
            if row[6] == 1:
                cafe["Has Bathroom"] = "Yes"
            elif row[6] == 0:
                cafe["Has Bathroom"] = "No"
            if row[7] == 1:
                cafe["Has Wifi"] = "Yes"
            elif row[7] == 0:
                cafe["Has Wifi"] = "No"
            if row[8] == 1:
                cafe["Can Take Calls"] = "Yes"
            elif row[8] == 0:
                cafe["Can Take Calls"] = "No"
            cafe["Seats"] = row[9]
            cafe["Coffee Price"] = row[10]
            cafe_dict[row[0]] = cafe

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if connection:
            connection.close()
            print("The Sqlite connection is closed")
    print(cafe_dict[1])
    return render_template('cafes.html', cafes=cafe_dict)


## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def all_cafe():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route("/search")
def search_cafe_at_location():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

## HTTP PUT/PATCH - Update Record

@app.route("/update/<int:cafe_id>", methods=["PATCH"])
def update_cafe_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        # To pass an HTTP code with response, just add after the json method. 200 = Ok
        return jsonify({"success": "Successfully updated the price!"}), 200
    else:
        # 404 = Resource not found
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

## HTTP DELETE - Delete Record

@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            # To pass an HTTP code with response, just add after the json method. 200 = Ok
            return jsonify({"success": "Successfully removed the cafe from the database!"}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    else:
        # 403 = Not authorized to make that request
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key"}), 403

if __name__ == '__main__':
    app.run(debug=True)
