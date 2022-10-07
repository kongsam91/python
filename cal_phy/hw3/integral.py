import math 
def f(x):
    f=math.exp(2*x)*math.sin(3*x)
    return f
def df(x):
    df=math.exp(2*x)*(2*math.sin(3*x)+3*math.cos(3*x))
    return df
def ddf(x):
    ddf=math.exp(2*x)*(12*math.cos(3*x)-5*math.sin(3*x))
    return ddf
real_soluton=-14.214
print("the range you want to integral ")
a , b = input().split() # 多個輸入 split
a=float(a)
b=float(b)
n=int(10000)
error=0
sum=0 #reset
h=abs(a-b)/(n)    
for i in range (1,int(n-1)):
    sum=sum+h*f(a+h*i)
sum=sum+(h/2)*(f(a)+f(b))
error= abs(real_soluton-sum)
print('the composite traoezidaal rule error is ',error)
print('the composite trapezoidal rule output is', sum) #finish the composite trapezoidal rule 
sum=0 #reset
error=0
h=abs(a-b)/(n)
for i in range (1,int( (n/2) -1 )):
    sum = sum + 2*f( a + 2*i*h )*(h/3) 
for i in range (1,int( (n/2) )):
    sum = sum + (4*h/3)*f(a+(2*i-1)*h)
sum = sum + (h/3)*(f(a)+f(b))
error= abs(real_soluton-sum)
print('the composite simposon`s rule error is ',error)
print('the composite simposon`s rule ', sum) #finish the composite simposon`s rule


#h=abs(a-b)/(n+2)
# for i in range (int(n/2)):
#     sum=sum+2*h*f(a+h+(2*i*h))
# print('the composite midpoint rule output is', sum) #finish composite midpoint rule




