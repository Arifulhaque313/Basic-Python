def f(e,x):
    return eval(e)
q=input("Enter the value of f(x)=")

def trap(a,b,n):
    h=(b-a)/n
    s=(f(q,a)+f(q,b))
    i=1

    while i<n:
        s+=2*f(q,a+i*h)
        i+=1
    return s*(h/2)
l=int(input("Enter the lower limit="))
u=float(input("Enter the  upper limit="))
n=int(input("Enter the value of n="))
print("","%.4f"%trap(l,u,n))