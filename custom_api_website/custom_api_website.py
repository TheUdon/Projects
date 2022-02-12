import requests
from pprint import pprint
from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'N6NnTBUUxTxrovGfBjEU'

Bootstrap(app)

# For now, this website just returns the data in a json format on the web page.
# Stock market API has limited amount of usages without subscription; code might not work
stock_market_apikey = "ace210f80377659c43ddf905ec0d82a7"
stock_market_endpoint = ""
parameters = {
    "access_key": stock_market_apikey,
    "symbols": "APPL,MSFT,GME",
    "limit": 100
}

class CheckStockForm(FlaskForm):
    company_symbols = StringField('Which companys do you want to check? (For multiple stock symbols use a comma with no spaces between, e.g. AAPL,MSFT): ', validators=[DataRequired()])
    data_type = SelectField('What would you like to know about the stock(s)?', choices=["eod", "intraday", "splits", "dividends"])
    submit = SubmitField('Submit')

@app.route("/", methods=["GET", "POST"])
def home():
    checkstock = CheckStockForm()
    if checkstock.validate_on_submit():
        stocks = checkstock.company_symbols.data
        data_type = checkstock.data_type.data
        parameters = {
            "access_key": stock_market_apikey,
            "symbols": stocks,
            "limit": 100
        }
        stock_market_endpoint = f"http://api.marketstack.com/v1/{data_type}"
        response = requests.get(url=stock_market_endpoint, params=parameters)
        response.raise_for_status()
        stock_market_data = response.json()
        return jsonify(stock_market_data)
    return render_template("index.html", form=checkstock)


if __name__ == '__main__':
    app.run(debug=True)
