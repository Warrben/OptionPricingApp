import numpy as np
from scipy.stats import norm

def calculate_call_price(share_price, exercise_PRICE, risk_free_rate, volatility, tenure):
  d1 = (np.log(share_price / exercise_PRICE) + (risk_free_rate + 0.5 * volatility**2) * tenure) / (volatility * np.sqrt(tenure))
  d2 = d1 - volatility * np.sqrt(tenure)
  
  call_price = share_price * norm.cdf(d1) - exercise_PRICE * np.exp(-risk_free_rate * tenure) * norm.cdf(d2)
  return call_price

def calculate_put_price(share_price, exercise_PRICE, risk_free_rate, volatility, tenure):
    d1 = (np.log(share_price / exercise_PRICE) + (risk_free_rate + 0.5 * volatility**2) * tenure) / (volatility * np.sqrt(tenure))
    d2 = d1 - volatility * np.sqrt(tenure)
    
    put_price = exercise_PRICE * np.exp(-risk_free_rate * tenure) * norm.cdf(-d2) - share_price * norm.cdf(-d1)
    return put_price
