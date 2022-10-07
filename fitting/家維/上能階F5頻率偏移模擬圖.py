import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#F=3到F=5
'''
躍遷f=3到f=5 delta m =+2
mF= -3 到mF= -1  頻率偏移 -13864958339.88489
mF= -2 到mF=  0  頻率偏移 -7005465445.660696
mF= -1 到mF=  1  頻率偏移 -145972551.43650213
mF=  0 到mF=  2  頻率偏移 6713520342.787691
mF=  1 到mF=  3  頻率偏移 13573013237.011885
mF=  2 到mF=  4  頻率偏移 20432506131.23608
mF=  3 到mF=  5  頻率偏移 27291999025.460274

躍遷f=3到f=5 delta m =0
mF= -3 到mF= -3  頻率偏移 -20578478682.67258
mF= -2 到mF= -2  頻率偏移 -13718985788.44839
mF= -1 到mF= -1  頻率偏移 -6859492894.224195
mF=  0 到mF=  0  頻率偏移 0.0
mF=  1 到mF=  1  頻率偏移 6859492894.224195
mF=  2 到mF=  2  頻率偏移 13718985788.44839
mF=  3 到mF=  3  頻率偏移 20578478682.67258

躍遷f=3到f=5 delta m =-2
mF= -3 到mF= -5  頻率偏移 -27291999025.460274
mF= -2 到mF= -4  頻率偏移 -20432506131.23608
mF= -1 到mF= -3  頻率偏移 -13573013237.011885
mF=  0 到mF= -2  頻率偏移 -6713520342.787691
mF=  1 到mF= -1  頻率偏移 145972551.43650213
mF=  2 到mF=  0  頻率偏移 7005465445.660696
mF=  3 到mF=  1  頻率偏移 13864958339.88489

cg
躍遷f=3到f=5 delta m =+2
mf = -3		-0.037268
mf = -2		-0.083333
mf = -1		-0.144338
mf = -0		-0.220479
mf = 1		-0.311805
mf = 2		-0.41833
mf = 3		-0.540062

躍遷f=3到f=5 delta m =-2
mf = -3		-0.540062
mf = -2		-0.41833
mf = -1		-0.311805
mf = -0		-0.220479
mf = 1		-0.144338
mf = 2		-0.083333
mf = 3		-0.037268

躍遷f=3到f=5 delta m =0
mf = -3		-0.161016
mf = -2		-0.241522
mf = -1		-0.288676
mf = -0		-0.30429
mf = 1		-0.288676
mf = 2		-0.241522
mf = 3		-0.161016

'''

b1=0#4245.26969488 #mG

b=b1*0.0001*0.001
f1=-13864958339.88489*b/(math.pi)
f2=-7005465445.660696*b/(math.pi)
f3=-145972551.43650213*b/(math.pi)
f4=6713520342.787691*b/(math.pi)
f5=13573013237.011885*b/(math.pi)
f6=20432506131.23608*b/(math.pi)
f7=27291999025.460274*b/(math.pi)

f0_1=-20578478682.67258*b/(math.pi)
f0_2=-13718985788.44839*b/(math.pi)
f0_3=-6859492894.224195*b/(math.pi)
f0_4=0.0*b/(math.pi)
f0_5=6859492894.224195*b/(math.pi)
f0_6=13718985788.44839*b/(math.pi)
f0_7=20578478682.67258*b/(math.pi)

f_1=-27291999025.460274*b/(math.pi)
f_2=-20432506131.23608*b/(math.pi)
f_3=-13573013237.011885*b/(math.pi)
f_4=-6713520342.787691*b/(math.pi)
f_5=145972551.43650213*b/(math.pi)
f_6=7005465445.660696*b/(math.pi)
f_7=13864958339.88489*b/(math.pi)

n=14000
x1=[round((i-n/2)*0.001,3) for i in range(n)]
y1=[0 for i in range(n)]
y2=[0 for i in range(n)]
y3=[0 for i in range(n)]
y4=[0 for i in range(n)]
y5=[0 for i in range(n)]
y6=[0 for i in range(n)]
y7=[0 for i in range(n)]

y8=[0 for i in range(n)]

y0_1=[0 for i in range(n)]
y0_2=[0 for i in range(n)]
y0_3=[0 for i in range(n)]
y0_4=[0 for i in range(n)]
y0_5=[0 for i in range(n)]
y0_6=[0 for i in range(n)]
y0_7=[0 for i in range(n)]

y_1=[0 for i in range(n)]
y_2=[0 for i in range(n)]
y_3=[0 for i in range(n)]
y_4=[0 for i in range(n)]
y_5=[0 for i in range(n)]
y_6=[0 for i in range(n)]
y_7=[0 for i in range(n)]

yy=[0 for i in range(n)]

a=1
hwhm=2.08185
for i in range(n):
    #delta m =+2
    y1[i]=a/math.pi*hwhm/2/(((x1[i]-f1/1000000))**2+(hwhm/2)**2)*(-0.037268)**2
    y2[i]=a/math.pi*hwhm/2/(((x1[i]-f2/1000000))**2+(hwhm/2)**2)*(-0.083333)**2
    y3[i]=a/math.pi*hwhm/2/(((x1[i]-f3/1000000))**2+(hwhm/2)**2)*(-0.144338)**2
    y4[i]=a/math.pi*hwhm/2/(((x1[i]-f4/1000000))**2+(hwhm/2)**2)*(-0.220479)**2
    y5[i]=a/math.pi*hwhm/2/(((x1[i]-f5/1000000))**2+(hwhm/2)**2)*(-0.311805)**2
    y6[i]=a/math.pi*hwhm/2/(((x1[i]-f6/1000000))**2+(hwhm/2)**2)*(-0.41833)**2
    y7[i]=a/math.pi*hwhm/2/(((x1[i]-f7/1000000))**2+(hwhm/2)**2)*(-0.540062)**2
    
    #delta m =0
    y0_1[i]=a/math.pi*hwhm/2/(((x1[i]-f0_1/1000000))**2+(hwhm/2)**2)*(-0.161016)**2
    y0_2[i]=a/math.pi*hwhm/2/(((x1[i]-f0_2/1000000))**2+(hwhm/2)**2)*(-0.241522)**2
    y0_3[i]=a/math.pi*hwhm/2/(((x1[i]-f0_3/1000000))**2+(hwhm/2)**2)*(-0.288676)**2
    y0_4[i]=a/math.pi*hwhm/2/(((x1[i]-f0_4/1000000))**2+(hwhm/2)**2)*(-0.30429)**2
    y0_5[i]=a/math.pi*hwhm/2/(((x1[i]-f0_5/1000000))**2+(hwhm/2)**2)*(-0.288676)**2
    y0_6[i]=a/math.pi*hwhm/2/(((x1[i]-f0_6/1000000))**2+(hwhm/2)**2)*(-0.241522)**2
    y0_7[i]=a/math.pi*hwhm/2/(((x1[i]-f0_7/1000000))**2+(hwhm/2)**2)*(-0.161016)**2
    
    #delta m =-2
    y_1[i]=a/math.pi*hwhm/2/(((x1[i]-f_1/1000000))**2+(hwhm/2)**2)*(-0.540062)**2
    y_2[i]=a/math.pi*hwhm/2/(((x1[i]-f_2/1000000))**2+(hwhm/2)**2)*(-0.41833)**2
    y_3[i]=a/math.pi*hwhm/2/(((x1[i]-f_3/1000000))**2+(hwhm/2)**2)*(-0.311805)**2
    y_4[i]=a/math.pi*hwhm/2/(((x1[i]-f_4/1000000))**2+(hwhm/2)**2)*(-0.220479)**2
    y_5[i]=a/math.pi*hwhm/2/(((x1[i]-f_5/1000000))**2+(hwhm/2)**2)*(-0.144338)**2
    y_6[i]=a/math.pi*hwhm/2/(((x1[i]-f_6/1000000))**2+(hwhm/2)**2)*(-0.083333)**2
    y_7[i]=a/math.pi*hwhm/2/(((x1[i]-f_7/1000000))**2+(hwhm/2)**2)*(-0.037268)**2
    
    y8[i]=y1[i]+y2[i]+y3[i]+y4[i]+y5[i]+y6[i]+y7[i]#+y_1[i]+y_2[i]+y_3[i]+y_4[i]+y_5[i]+y_6[i]+y_7[i]\
    #+y0_1[i]+y0_2[i]+y0_3[i]+y0_4[i]+y0_5[i]+y0_6[i]+y0_7[i]
    yy[i]=str(x1[i])+'\t'+str(y8[i])
    
plt.figure()
plt.title('F=3 to F=5')
plt.plot(x1, y1, linewidth=1.5)
plt.plot(x1, y2, linewidth=1.5)
plt.plot(x1, y3, linewidth=1.5)
plt.plot(x1, y4, linewidth=1.5)
plt.plot(x1, y5, linewidth=1.5)
plt.plot(x1, y6, linewidth=1.5)
plt.plot(x1, y7, linewidth=1.5)

'''plt.plot(x1, y0_1, linewidth=1.5)
plt.plot(x1, y0_2, linewidth=1.5)
plt.plot(x1, y0_3, linewidth=1.5)
plt.plot(x1, y0_4, linewidth=1.5)
plt.plot(x1, y0_5, linewidth=1.5)
plt.plot(x1, y0_6, linewidth=1.5)
plt.plot(x1, y0_7, linewidth=1.5)

plt.plot(x1, y_1, linewidth=1.5)
plt.plot(x1, y_2, linewidth=1.5)
plt.plot(x1, y_3, linewidth=1.5)
plt.plot(x1, y_4, linewidth=1.5)
plt.plot(x1, y_5, linewidth=1.5)
plt.plot(x1, y_6, linewidth=1.5)
plt.plot(x1, y_7, linewidth=1.5)'''

plt.figure()
plt.title('F=3 to F=5')
plt.plot(x1, y8, linewidth=1.5)

with open(r'test.txt', 'w') as f:
    for item in yy:
        # write each item on a new line
        f.write("%s\n" % item)
        
    print('Done')
f.close()

from scipy.optimize import curve_fit

def Lorentz(x,A,xc,w):
    y = (2*A/np.pi)*(w/2/((x-xc/1000000)**2 + (w/2)**2))
    return y

x = [x1[i] for i in range(n)]
y = [y8[i] for i in range(n)]

fig, ax = plt.subplots()
ax.plot(x,y,'o')

p,c = curve_fit(Lorentz, x, y,
                p0=[-10,427.5,0.1],absolute_sigma=True)
A,xc,w=p

xfit = np.linspace((0-n/2)*0.001,(n-n/2)*0.001,200)
yfit = Lorentz(xfit,A,xc,w)

ax.plot(xfit,yfit,'-')

print('A,xc,w:')
print(A,xc,w)
print('A,xc,w: standard error')
print(np.sqrt(np.diag(c)))
#F=4到F=5
'''
躍遷f=4到f=5 delta m =+2
mF= -4 到mF= -2  頻率偏移 7297410548.5337
mF= -3 到mF= -1  頻率偏移 7151437997.097199
mF= -2 到mF=  0  頻率偏移 7005465445.660696
mF= -1 到mF=  1  頻率偏移 6859492894.224195
mF=  0 到mF=  2  頻率偏移 6713520342.787691
mF=  1 到mF=  3  頻率偏移 6567547791.35119
mF=  2 到mF=  4  頻率偏移 6421575239.914687
mF=  3 到mF=  5  頻率偏移 6275602688.478184
mF=  4 到mF=  6  無躍遷

躍遷f=4到f=5 delta m =0
mF= -4 到mF= -4  頻率偏移 583890205.7460085
mF= -3 到mF= -3  頻率偏移 437917654.30950683
mF= -2 到mF= -2  頻率偏移 291945102.87300426
mF= -1 到mF= -1  頻率偏移 145972551.43650213
mF=  0 到mF=  0  頻率偏移 0.0
mF=  1 到mF=  1  頻率偏移 -145972551.43650213
mF=  2 到mF=  2  頻率偏移 -291945102.87300426
mF=  3 到mF=  3  頻率偏移 -437917654.30950683
mF=  4 到mF=  4  頻率偏移 -583890205.7460085

躍遷f=4到f=5 delta m =-2
mF= -4 到mF= -6  無躍遷
mF= -3 到mF= -5  頻率偏移 -6275602688.478184
mF= -2 到mF= -4  頻率偏移 -6421575239.914687
mF= -1 到mF= -3  頻率偏移 -6567547791.35119
mF=  0 到mF= -2  頻率偏移 -6713520342.787691
mF=  1 到mF= -1  頻率偏移 -6859492894.224195
mF=  2 到mF=  0  頻率偏移 -7005465445.660696
mF=  3 到mF=  1  頻率偏移 -7151437997.097199
mF=  4 到mF=  2  頻率偏移 -7297410548.5337

cg
躍遷f=4到f=5 delta m =+2
mf = -4		0.052705
mf = -3		0.098601
mf = -2		0.144338
mf = -1		0.186339
mf = -0		0.220479
mf = 1		0.241523
mf = 2		0.241523
mf = 3		0.204124
mf = 4		0


躍遷f43到f=5 delta m =-2
mf = -4		0
mf = -3		-0.204124
mf = -2		-0.241523
mf = -1		-0.241523
mf = -0		-0.220479
mf = 1		-0.186339
mf = 2		-0.144338
mf = 3		-0.098601
mf = 4		-0.052705


躍遷f=4到f=5 delta m =0
mf = -4		0.182574
mf = -3		0.182574
mf = -2		0.139443
mf = -1		0.074536
mf = -0		0
mf = 1		-0.074536
mf = 2		-0.139443
mf = 3		-0.182574
mf = 4		-0.182574


'''

b1=4245.26969488 #mG

b=b1*0.0001*0.001
f1=7297410548.5337*b/(math.pi)
f2=7151437997.097199*b/(math.pi)
f3=7005465445.660696*b/(math.pi)
f4=6859492894.224195*b/(math.pi)
f5=6713520342.787691*b/(math.pi)
f6=6567547791.35119*b/(math.pi)
f7=6421575239.914687*b/(math.pi)
f8=6275602688.478184*b/(math.pi)
f9=0*b/(math.pi)

f0_1=583890205.7460085*b/(math.pi)
f0_2=437917654.30950683*b/(math.pi)
f0_3=291945102.87300426*b/(math.pi)
f0_4=145972551.43650213*b/(math.pi)
f0_5=0*b/(math.pi)
f0_6=-145972551.43650213*b/(math.pi)
f0_7=-291945102.87300426*b/(math.pi)
f0_8=-437917654.30950683*b/(math.pi)
f0_9=-583890205.7460085*b/(math.pi)

f_1=0*b/(math.pi)
f_2=-6275602688.478184*b/(math.pi)
f_3=-6421575239.914687*b/(math.pi)
f_4=-6567547791.35119*b/(math.pi)
f_5=-6713520342.787691*b/(math.pi)
f_6=-6859492894.224195*b/(math.pi)
f_7=-7005465445.660696*b/(math.pi)
f_8=-7151437997.097199*b/(math.pi)
f_9=-7297410548.5337*b/(math.pi)

n=14000
x1=[round((i-n/2)*0.001,3) for i in range(n)]
y1=[0 for i in range(n)]
y2=[0 for i in range(n)]
y3=[0 for i in range(n)]
y4=[0 for i in range(n)]
y5=[0 for i in range(n)]
y6=[0 for i in range(n)]
y7=[0 for i in range(n)]
y81=[0 for i in range(n)]
y9=[0 for i in range(n)]

y8=[0 for i in range(n)]

y0_1=[0 for i in range(n)]
y0_2=[0 for i in range(n)]
y0_3=[0 for i in range(n)]
y0_4=[0 for i in range(n)]
y0_5=[0 for i in range(n)]
y0_6=[0 for i in range(n)]
y0_7=[0 for i in range(n)]
y0_8=[0 for i in range(n)]
y0_9=[0 for i in range(n)]

y_1=[0 for i in range(n)]
y_2=[0 for i in range(n)]
y_3=[0 for i in range(n)]
y_4=[0 for i in range(n)]
y_5=[0 for i in range(n)]
y_6=[0 for i in range(n)]
y_7=[0 for i in range(n)]
y_8=[0 for i in range(n)]
y_9=[0 for i in range(n)]

yy=[0 for i in range(n)]

a=1
hwhm=1.92844
for i in range(n):
    #delta m =+2
    y1[i]=a/math.pi*hwhm/2/(((x1[i]-f1/1000000))**2+(hwhm/2)**2)*(0.052705)**2
    y2[i]=a/math.pi*hwhm/2/(((x1[i]-f2/1000000))**2+(hwhm/2)**2)*(0.098601)**2
    y3[i]=a/math.pi*hwhm/2/(((x1[i]-f3/1000000))**2+(hwhm/2)**2)*(0.144338)**2
    y4[i]=a/math.pi*hwhm/2/(((x1[i]-f4/1000000))**2+(hwhm/2)**2)*(0.186339)**2
    y5[i]=a/math.pi*hwhm/2/(((x1[i]-f5/1000000))**2+(hwhm/2)**2)*(0.220479)**2
    y6[i]=a/math.pi*hwhm/2/(((x1[i]-f6/1000000))**2+(hwhm/2)**2)*(0.241523)**2
    y7[i]=a/math.pi*hwhm/2/(((x1[i]-f7/1000000))**2+(hwhm/2)**2)*(0.241523)**2
    y81[i]=a/math.pi*hwhm/2/(((x1[i]-f8/1000000))**2+(hwhm/2)**2)*(0.204124)**2
    y9[i]=a/math.pi*hwhm/2/(((x1[i]-f9/1000000))**2+(hwhm/2)**2)*(0)**2
    #delta m =0
    y0_1[i]=a/math.pi*hwhm/2/(((x1[i]-f0_1/1000000))**2+(hwhm/2)**2)*(0.182574)**2
    y0_2[i]=a/math.pi*hwhm/2/(((x1[i]-f0_2/1000000))**2+(hwhm/2)**2)*(0.182574)**2
    y0_3[i]=a/math.pi*hwhm/2/(((x1[i]-f0_3/1000000))**2+(hwhm/2)**2)*(0.139443)**2
    y0_4[i]=a/math.pi*hwhm/2/(((x1[i]-f0_4/1000000))**2+(hwhm/2)**2)*(0.074536)**2
    y0_5[i]=a/math.pi*hwhm/2/(((x1[i]-f0_5/1000000))**2+(hwhm/2)**2)*(0)**2
    y0_6[i]=a/math.pi*hwhm/2/(((x1[i]-f0_6/1000000))**2+(hwhm/2)**2)*(-0.074536)**2
    y0_7[i]=a/math.pi*hwhm/2/(((x1[i]-f0_7/1000000))**2+(hwhm/2)**2)*(-0.139443)**2
    y0_8[i]=a/math.pi*hwhm/2/(((x1[i]-f0_8/1000000))**2+(hwhm/2)**2)*(-0.182574)**2
    y0_9[i]=a/math.pi*hwhm/2/(((x1[i]-f0_9/1000000))**2+(hwhm/2)**2)*(-0.182574)**2
    #delta m =-2
    y_1[i]=a/math.pi*hwhm/2/(((x1[i]-f_1/1000000))**2+(hwhm/2)**2)*(0)**2
    y_2[i]=a/math.pi*hwhm/2/(((x1[i]-f_2/1000000))**2+(hwhm/2)**2)*(-0.204124)**2
    y_3[i]=a/math.pi*hwhm/2/(((x1[i]-f_3/1000000))**2+(hwhm/2)**2)*(-0.241523)**2
    y_4[i]=a/math.pi*hwhm/2/(((x1[i]-f_4/1000000))**2+(hwhm/2)**2)*(-0.241523)**2
    y_5[i]=a/math.pi*hwhm/2/(((x1[i]-f_5/1000000))**2+(hwhm/2)**2)*(-0.220479)**2
    y_6[i]=a/math.pi*hwhm/2/(((x1[i]-f_6/1000000))**2+(hwhm/2)**2)*(-0.186339)**2
    y_7[i]=a/math.pi*hwhm/2/(((x1[i]-f_7/1000000))**2+(hwhm/2)**2)*(-0.144338)**2
    y_8[i]=a/math.pi*hwhm/2/(((x1[i]-f_8/1000000))**2+(hwhm/2)**2)*(-0.098601)**2
    y_9[i]=a/math.pi*hwhm/2/(((x1[i]-f_9/1000000))**2+(hwhm/2)**2)*(-0.052705)**2
    
    y8[i]=y1[i]+y2[i]+y3[i]+y4[i]+y5[i]+y6[i]+y7[i]+y81[i]+y9[i]#+y_1[i]+y_2[i]+y_3[i]+y_4[i]+y_5[i]+y_6[i]+y_7[i]\
    #+y_8[i]+y_9[i]+y0_1[i]+y0_2[i]+y0_3[i]+y0_4[i]+y0_5[i]+y0_6[i]+y0_7[i]+y0_8[i]+y0_9[i]
    yy[i]=str(x1[i])+'\t'+str(y8[i])
    
plt.figure()
plt.title('F=4 to F=5')
plt.plot(x1, y1, linewidth=1.5)
plt.plot(x1, y2, linewidth=1.5)
plt.plot(x1, y3, linewidth=1.5)
plt.plot(x1, y4, linewidth=1.5)
plt.plot(x1, y5, linewidth=1.5)
plt.plot(x1, y6, linewidth=1.5)
plt.plot(x1, y7, linewidth=1.5)
plt.plot(x1, y81, linewidth=1.5)
plt.plot(x1, y9, linewidth=1.5)

'''plt.plot(x1, y0_1, linewidth=1.5)
plt.plot(x1, y0_2, linewidth=1.5)
plt.plot(x1, y0_3, linewidth=1.5)
plt.plot(x1, y0_4, linewidth=1.5)
plt.plot(x1, y0_5, linewidth=1.5)
plt.plot(x1, y0_6, linewidth=1.5)
plt.plot(x1, y0_7, linewidth=1.5)
plt.plot(x1, y0_8, linewidth=1.5)
plt.plot(x1, y0_9, linewidth=1.5)

plt.plot(x1, y_1, linewidth=1.5)
plt.plot(x1, y_2, linewidth=1.5)
plt.plot(x1, y_3, linewidth=1.5)
plt.plot(x1, y_4, linewidth=1.5)
plt.plot(x1, y_5, linewidth=1.5)
plt.plot(x1, y_6, linewidth=1.5)
plt.plot(x1, y_7, linewidth=1.5)
plt.plot(x1, y_8, linewidth=1.5)
plt.plot(x1, y_9, linewidth=1.5)'''

plt.figure()
plt.title('F=4 to F=5')
plt.plot(x1, y8, linewidth=1.5)

with open(r'test1.txt', 'w') as f:
    for item in yy:
        # write each item on a new line
        f.write("%s\n" % item)
        
    print('Done')
f.close()