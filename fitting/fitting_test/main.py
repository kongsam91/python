# 6. 自定義函數曲線擬合：單變量
import numpy as np
import matplotlib.pyplot as plt # 導入 Matplotlib 工具包
from scipy.optimize import leastsq, curve_fit # 導入 scipy 中的曲線擬合工具
def fitfunc6(x, p0, p1, p2, p3): # 定義擬合函數為自定義函數
# p0, p1, p2, p3 = p # 擬合函數的參數
    y = p0 + ((x*x-p1)**2+ p2) * np.sin(x*p3)
    return y
# def error6(p, x, y): # 定義觀測值與擬合函數值的誤差函數
# p0, p1, p2, p3 = p
# err = fitfunc6(x, p0, p1, p2, p3) - y # 計算殘差
# return err
# 創建給定數據點集 (x, yObs)
p0, p1, p2, p3 = [1.0, 1.2, 0.5, 0.8] # y = p0 + ((x*x-p1)**2+ p2) * np.sin(x*p3)
x = np.linspace(-1, 2, 30)
y = fitfunc6(x, p0, p1, p2, p3)
np.random.seed(1)
yObs = y + 0.5*np.random.randn(x.shape[-1]) # 生成帶有噪聲的觀測數據
# # 用 scipy.optimize.leastsq() 進行函數擬合
# pIni = [1, 1, 1, 1] # 設置擬合函數的參數初值
# pFit, info = leastsq(error6, pIni, args=(x, yObs)) # 最小二乘法求擬合參數
# print("Data fitting of custom function by leastsq")
# print("y = p0 + ((x*x-p1)**2+ p2) * np.sin(x*p3)")
# print("p[0] = {:.4f}\np[1] = {:.4f}\np[2] = {:.4f}\np[3] = {:.4f}"
# .format(pFit[0], pFit[1], pFit[2], pFit[3]))
# 用 scipy.optimize.curve_fit() 進行自定義函數擬合(單變量)
pFit, pcov = curve_fit(fitfunc6, x, yObs)
print("Data fitting of custom function by curve_fit:")
print("y = p0 + ((x*x-p1)**2+ p2) * np.sin(x*p3)")
print("p[0] = {:.4f}\np[1] = {:.4f}\np[2] = {:.4f}\np[3] = {:.4f}"
.format(pFit[0], pFit[1], pFit[2], pFit[3]))
print("estimated covariancepcov:\n",pcov)



# 由擬合函數 fitfunc 計算擬合曲線在數據點的函數值
yFit = fitfunc6(x, pFit[0], pFit[1], pFit[2], pFit[3])

# 繪圖
fig, ax = plt.subplots(figsize=(8,6))
ax.set_title("Data fitting of custom function")
plt.scatter(x, yObs, label="observed data")
plt.plot(x, y, 'r--', label="theoretical curve")
plt.plot(x, yFit, 'b-', label="fitting curve")
plt.legend(loc="best")
plt.show()