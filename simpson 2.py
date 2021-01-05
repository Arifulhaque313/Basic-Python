def f(e,x):
    return eval(e)
F=input("enter the value f(x)=")

def simp(a,b,n):
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
            else :
                r+=2*y[i]
            i+=1
    r=r*(h/3)
    return r
v=0
l=1
n=5
print("","%.4f"%simp(v,l,n))
