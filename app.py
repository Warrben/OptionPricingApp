from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import option_pricing_library


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://warrbenms:Manish$0579@warrbenms.mysql.pythonanywhere-services.com/warrbenms$OptionPricingApp'
db = SQLAlchemy(app)

class OptionData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    share_price = db.Column(db.Float, nullable=False)
    exercise_PRICE = db.Column(db.Float, nullable=False)
    risk_free_rate = db.Column(db.Float, nullable=False)
    volatility = db.Column(db.Float, nullable=False)
    tenure = db.Column(db.Float, nullable=False)
    call_price = db.Column(db.Float)
    put_price = db.Column(db.Float)

    def __init__(self, share_price, exercise_PRICE, risk_free_rate, volatility, tenure, call_price, put_price):
        self.share_price = share_price
        self.exercise_PRICE = exercise_PRICE
        self.risk_free_rate = risk_free_rate
        self.volatility = volatility
        self.tenure = tenure
        self.call_price = call_price
        self.put_price = put_price

    def __repr__(self):
        return f"OptionData(id={self.id}, share_price={self.share_price}, exercise_PRICE={self.exercise_PRICE}, risk_free_rate={self.risk_free_rate}, volatility={self.volatility}, tenure={self.tenure}, call_price={self.call_price}, put_price={self.put_price})"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    share_price = float(request.form.get('share_price'))
    exercise_PRICE = float(request.form.get('exercise_PRICE'))
    risk_free_rate = float(request.form.get('risk_free_rate'))
    volatility = float(request.form.get('volatility'))
    tenure = float(request.form.get('tenure'))

     # Perform option pricing calculations using your library
    call_price = option_pricing_library.calculate_call_price(share_price, exercise_PRICE, risk_free_rate, volatility, tenure)
    put_price = option_pricing_library.calculate_put_price(share_price, exercise_PRICE, risk_free_rate, volatility, tenure)

    # Save data to the database
    option_data = OptionData(
        share_price=share_price,
        exercise_PRICE=exercise_PRICE,
        risk_free_rate=risk_free_rate,
        volatility=volatility,
        tenure=tenure,
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