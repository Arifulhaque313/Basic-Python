def f(e,x):
    return eval (e)
q=input("Enter the value of f(x)=")

def trap(a,b,n):
    h=(b-a)/n
    s=(f(q,a)+f(q,b))
    i=1

    while i<n:
        s+=2*f(q,a+i*h)
        i+=1

    return ((h/2)*s)
a=0
b=2
n=5
print("","%.4f"%trap(a,b,n))