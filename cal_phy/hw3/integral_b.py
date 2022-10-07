#import math 
import numpy as np 
from decimal import Decimal
def f(x):
    return np.exp(2*x) * np.sin(3*x)

real_soluton=(3+np.exp(4)*(2*np.sin(6)-3*np.cos(6)))/13
print("the range you want to integral ")
a , b = input().split() # 多個輸入 split
a=float(a)
b=float(b)
n=100
sum=0
error=1

while (abs(real_soluton-sum) > 1e-6):
    h = abs(a-b) / n
    x = np.linspace(a+h, b-h, n-2)
    sum = ( 2 * np.sum(f(x)) - f(a) - f(b) ) * h / 2
    error = abs(real_soluton - sum)
    n = n * 2
    print(sum)
    

print('the number is ',n)    
print('the composite trapezoidal rule output is', sum) 
print('the composite trapezoidal rule error is', abs(error) ) #finish the composite trapezoidal rule 

sum=0 #reset
n=100
error=1
while (abs(real_soluton-sum) > 1e-6):
    h=abs(a-b)/(n)
    sum=0
    for i in range (1,int( (n/2) -1 )):
        sum = sum + 2*f( a + 2*i*h )*(h/3)
    # np.sum( np.arange(a,b-2*h,h) ) 
    for i in range (1,int( (n/2) )):
        sum = sum + (4*h/3)*f(a+(2*i-1)*h)
    sum = sum + (h/3)*(f(a)+f(b))
    n = n *10
    error=abs(real_soluton-sum)
    #print(error)
    if n>1000:
        pass 

print('the n is ',n)   
print('the composite simposon`s rule ', sum) 
print('the composite simposon`s rule error is', abs(error) ) #finish the composite simposon`s rule
