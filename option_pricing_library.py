import numpy as np
from scipy.stats import norm

def calculate_option_prices(underlying_price, strike_price, risk_free_rate, volatility, time_to_expiry):
    d1 = (np.log(underlying_price / strike_price) + (risk_free_rate + 0.5 * volatility**2) * time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
    d2 = d1 - volatility * np.sqrt(time_to_expiry)
    
    call_price = underlying_price * norm.cdf(d1) - strike_price * np.exp(-risk_free_rate * time_to_expiry) * norm.cdf(d2)
    put_price = strike_price * np.exp(-risk_free_rate * time_to_expiry) * norm.cdf(-d2) - underlying_price * norm.cdf(-d1)
    
    return call_price, put_price
