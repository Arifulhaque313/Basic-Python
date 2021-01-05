import math

def f(e,x):
    return eval(e)
q=input("Enter the value of f(x)=")

def simp(a,b,n):
    h=(b-a)/n
    x=list()
    y=list()
    i=0

    while i<=n:
        x.append(a+i*h)
        y.append(f(q,x[i]))
        i+=1
    r=0
    i=0
    while i<=n:
        if i==0 or i==n:
            r+=y[i]
        elif i%2!=0:
            r+=4*(y[i])
        else :
            r+=2*(y[i])
        i+=1
    r=r*(h/3)
    return r
x0=float(input("Enter the value of x0="))
y0=float(input("Enter the value of y0="))
n=float(input("Enter the value of h="))

print("","%.4f"%simp(x0,y0,n))