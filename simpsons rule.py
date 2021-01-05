import math
print("Md.Ariful Haque \nId:173462130")
def f(e,x):
    return eval (e)
F=input("Enter an integral = ")
def sim(a,b,n):
    h=(b-a)/n

    x=list()
    y=list()
    i=0

    while i<=n:
        x.append(a+i*h)
        y.append(f(F,x[i]))

        i+=1
    r=0
    i=0
    while i<=n:
        if i==0 or i==n:
            r+=y[i]
        elif i%2!=0:
            r+=4*y[i]
        else:
            r+=2*y[i]
        i+=1
    r=r*h/3
    return r
l=int(input("Enter the lower limit="))
u=int(input("Enter the  upper limit="))
n=int(input("Enter the value of n="))
print("The value is =","%.6f"%sim(l,u,n))