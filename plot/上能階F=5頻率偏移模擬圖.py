import math
import matplotlib.pyplot as plt

#F=3到F=5
'''
躍遷f=3到f=5 delta m =+2
mF= -3 到mF= -1  能階偏移 -5.7340859841239153e-05
mF= -2 到mF=  0  能階偏移 -2.8972276900877363e-05
mF= -1 到mF=  1  能階偏移 -6.036939605155736e-07
mF=  0 到mF=  2  能階偏移 2.7764888979846215e-05
mF=  1 到mF=  3  能階偏移 5.6133471920208e-05
mF=  2 到mF=  4  能階偏移 8.45020548605698e-05
mF=  3 到mF=  5  能階偏移 0.00011287063780093158

mf = -3		-0.037268
mf = -2		-0.083333
mf = -1		-0.144338
mf = -0		-0.220479
mf = 1		-0.311805
mf = 2		-0.41833
mf = 3		-0.540062

'''
b=0
f1=-5.7340859841239153*10**(-5)*b
f2=-2.8972276900877363*10**(-5)*b
f3=-6.036939605155736*10**(-7)*b
f4=2.7764888979846215*10**(-5)*b
f5=5.6133471920208*10**(-5)*b
f6=8.45020548605698*10**(-5)*b
f7=0.00011287063780093158*b


x1=[(i-2500)*0.001 for i in range(5000)]
y1=[0 for i in range(5000)]
y2=[0 for i in range(5000)]
y3=[0 for i in range(5000)]
y4=[0 for i in range(5000)]
y5=[0 for i in range(5000)]
y6=[0 for i in range(5000)]
y7=[0 for i in range(5000)]
y8=[0 for i in range(5000)]

for i in range(5000):
    y1[i]=1/(((x1[i]-f1))**2+1)*(-0.037268)**2
    y2[i]=1/(((x1[i]-f2))**2+1)*(-0.083333)**2
    y3[i]=1/(((x1[i]-f3))**2+1)*(-0.144338)**2
    y4[i]=1/(((x1[i]-f4))**2+1)*(-0.220479)**2
    y5[i]=1/(((x1[i]-f5))**2+1)*(-0.311805)**2
    y6[i]=1/(((x1[i]-f6))**2+1)*(-0.41833)**2
    y7[i]=1/(((x1[i]-f7))**2+1)*(-0.540062)**2
    y8[i]=y1[i]+y2[i]+y3[i]+y4[i]+y5[i]+y6[i]+y7[i]


plt.plot(x1, y1, linewidth=1.5)
# plt.title("Plot line in Matplotlib",fontsize=15)
# plt.xlabel("X",fontsize=13)
# plt.ylabel("Y",fontsize=13)
plt.plot(x1, y2, linewidth=1.5)
plt.plot(x1, y3, linewidth=1.5)
plt.plot(x1, y4, linewidth=1.5)
plt.plot(x1, y5, linewidth=1.5)
plt.plot(x1, y6, linewidth=1.5)
plt.plot(x1, y7, linewidth=1.5)
plt.figure()
plt.plot(x1, y8, linewidth=1.5)


with open(r'test.txt', 'w') as f:
    for x, y in zip(x1, y8):
        f.write(f'{x},{y}\n')
    print('Done')
f.close()
