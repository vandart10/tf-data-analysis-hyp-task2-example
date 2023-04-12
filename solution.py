import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 710820274 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    (_, pvalue) = stats.mannwhitneyu(x, y)
    return pvalue < 0.1
