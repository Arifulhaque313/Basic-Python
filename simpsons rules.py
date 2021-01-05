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
        elif i%2!=0 :
            r+=4*y[i]
        else :
            r+=2*y[i]
        i+=1
    r=r*(h/3)
    return r
a=0
b=2
n=100
print("","%.4f"%simp(a,b,n))