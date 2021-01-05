import math
print("Md.Ariful Haque \nId:173462130")
def y(e,x):
    return eval(e)
f=input("Enter the integral y(x)= ")

def trap(a,b,n):
    h=(b-a)/n
    s=(y(f,a)+y(f,b))
    i=1

    while i<=n:
        s+=2*y(f,a+i*h)
        i+=1

    return ((h/2)*s)
x=int(input("Enter the value of lower limit ="))
x0=int(input("Enter the value of upper limit="))
n=int(input("Enter the value of n="))
print("The value is =","%.4f"%trap(x,x0,n))