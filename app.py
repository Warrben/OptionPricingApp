from flask import Flask, render_template, request
import option_pricing_library  # You will need to create this module

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        underlying_price = float(request.form['underlying_price'])
        strike_price = float(request.form['strike_price'])
        risk_free_rate = float(request.form['risk_free_rate'])
        volatility = float(request.form['volatility'])
        time_to_expiry = float(request.form['time_to_expiry'])

        call_price, put_price = option_pricing_library.calculate_option_prices(
            underlying_price, strike_price, risk_free_rate, volatility, time_to_expiry
        )

        return render_template('index.html', call_price=call_price, put_price=put_price)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
