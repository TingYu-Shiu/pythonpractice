import numpy as np
from scipy.stats import ttest_ind

# 假設兩組實驗數據
control_group = [4, 5, 6, 7, 5, 4, 6, 7, 3, 5]
experimental_group = [6, 7, 8, 7, 6, 5, 6, 8, 5, 6]

# 計算兩組數據的平均值
control_mean = np.mean(control_group)
experimental_mean = np.mean(experimental_group)

# 執行獨立樣本 t 檢定
t_statistic, p_value = ttest_ind(control_group, experimental_group)

# 輸出結果
print("Control Group Mean:", control_mean)
print("Experimental Group Mean:", experimental_mean)
print("T-statistic:", t_statistic)
print("P-value:", p_value)

# 判斷結果是否達到統計顯著性
if p_value < 0.05:
    print("結果達到統計顯著性")
else:
    print("結果未達到統計顯著性")