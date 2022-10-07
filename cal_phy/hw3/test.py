import math 
from decimal import Decimal
def f(x):
    f=Decimal(math.exp(2*x)*math.sin(3*x))
    return f

real_soluton=Decimal(-14.214)
print("the range you want to integral ")
a , b = input().split() # 多個輸入 split
a=Decimal((a))
b=Decimal(float(b))
n=int(100)
sum=Decimal(0)
error=Decimal(1)


sum=sum #reset
print(sum)

while (Decimal(abs(real_soluton-sum)) > Decimal(1e-6)):
    h=Decimal(abs(a-b)/(n))    
    sum=0
    for i in range (1,int(n-1)):
        sum=sum+h*f(a+h*i)
    sum=sum+(h/2)*(f(a)+f(b))
    n=n+1
    error=abs(real_soluton-sum)
    if n>5000:
        break 

print('the number is ',n)    
print('the composite trapezoidal rule output is', sum) 
print('the composite trapezoidal rule error is', abs(error) ) #finish the composite trapezoidal rule 

sum=Decimal(0) #reset
n=100
error=Decimal(1)
while (abs(real_soluton-sum) > 1e-6):
    h=abs(a-b)/(n)
    sum=Decimal(0)
    for i in range (1,int( (n/2) -1 )):
        sum = sum + 2*f( a + 2*i*h )*(h/3) 
    for i in range (1,int( (n/2) )):
        sum = sum + (4*h/3)*f(a+(2*i-1)*h)
    sum = Decimal(sum + (h/3)*(f(a)+f(b)))
    n=n+1
    error=Decimal(abs(real_soluton-sum))
    if n>5000:
        break 

print('the n is ',n)   
print('the composite simposon`s rule ', sum) 
print('the composite simposon`s rule error is', abs(error) ) #finish the composite simposon`s rule
