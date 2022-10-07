#%%
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
x = np.linspace(-5,5,100)
y = np.exp(-x**2)
plt.plot(x,y)
#%%
# fitting y = f(x) abcd未知
def gauss(x,a,b,c,d):
    return a*np.exp(-(x-b)**2/(2*c**2))+d

boundpa = ([0,0,0,0],[1,1,1,1])
# 範圍[amin,bmin,cmin,dmin],[amax,bmax,cmax,dmax]

popt, pcov = curve_fit(gauss,x,y,bounds=boundpa)
# (哪個函數,x,y,範圍(可省略))

# fitting結果
a = popt[0]
b = popt[1]
c = popt[2]
d = popt[3]

plt.plot(x,y)
plt.plot(x,gauss(x,a,b,c,d),'--')

# %%
