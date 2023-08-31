from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import option_pricing_library


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://warrbenms:Manish$0579@warrbenms.mysql.pythonanywhere-services.com/warrbenms$OptionPricingApp'
db = SQLAlchemy(app)

class OptionData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_1 = db.Column(db.Float, nullable=False)
    input_2 = db.Column(db.Float, nullable=False)
    input_3 = db.Column(db.Float, nullable=False)
    input_4 = db.Column(db.Float, nullable=False)
    input_5 = db.Column(db.Float, nullable=False)
    call_price = db.Column(db.Float)
    put_price = db.Column(db.Float)

    def __init__(self, input_1, input_2, input_3, input_4, input_5, call_price, put_price):
        self.input_1 = input_1
        self.input_2 = input_2
        self.input_3 = input_3
        self.input_4 = input_4
        self.input_5 = input_5
        self.call_price = call_price
        self.put_price = put_price

    def __repr__(self):
        return f"OptionData(id={self.id}, input_1={self.input_1}, input_2={self.input_2}, input_3={self.input_3}, input_4={self.input_4}, input_5={self.input_5}, call_price={self.call_price}, put_price={self.put_price})"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    input_1 = float(request.form.get('input_1'))
    input_2 = float(request.form.get('input_2'))
    input_3 = float(request.form.get('input_3'))
    input_4 = float(request.form.get('input_4'))
    input_5 = float(request.form.get('input_5'))

     # Perform option pricing calculations using your library
    call_price = option_pricing_library.calculate_call_price(input_1, input_2, input_3, input_4, input_5)
    put_price = option_pricing_library.calculate_put_price(input_1, input_2, input_3, input_4, input_5)

    # Save data to the database
    option_data = OptionData(
        input_1=input_1,
        input_2=input_2,
        input_3=input_3,
        input_4=input_4,
        input_5=input_5,
        call_price=call_price,
        put_price=put_price
    )
    db.session.add(option_data)
    db.session.commit()

    return render_template('result.html', call_price=call_price, put_price=put_price)

@app.route('/history')
def history():
    option_data = OptionData.query.all()
    return render_template('history.html', option_data=option_data)