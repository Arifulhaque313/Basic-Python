def f(e,x):
    return eval (e)
F=input("Enter the function f(x)=")
def trap(a,b,n):
    h=(b-a)/n
    s=(f(F,a)+f(F,b))
    i=1
    while i<=n:
        s+=2*f(F,a+i*h)
        i+=1
    return (s*(h/2))
x0=0
y0=1
n=5
print("","%.4f"%trap(x0,y0,n))