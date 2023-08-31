import numpy as np
from scipy.stats import norm

def calculate_call_price(input_1, input_2, input_3, input_4, input_5):
  d1 = (np.log(input_1 / input_2) + (input_3 + 0.5 * input_4**2) * input_5) / (input_4 * np.sqrt(input_5))
  d2 = d1 - input_4 * np.sqrt(input_5)
  
  call_price = input_1 * norm.cdf(d1) - input_2 * np.exp(-input_3 * input_5) * norm.cdf(d2)
  return call_price

def calculate_put_price(input_1, input_2, input_3, input_4, input_5):
    d1 = (np.log(input_1 / input_2) + (input_3 + 0.5 * input_4**2) * input_5) / (input_4 * np.sqrt(input_5))
    d2 = d1 - input_4 * np.sqrt(input_5)
    
    put_price = input_2 * np.exp(-input_3 * input_5) * norm.cdf(-d2) - input_1 * norm.cdf(-d1)
    return put_price
