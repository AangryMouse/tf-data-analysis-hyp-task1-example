import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 396317433

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    prop_control = x_success / x_cnt
    prop_test = y_success / y_cnt

    z_stat, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='larger')

    return z_stat > 1.555
