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
    return (h/2)*s
x0=float(input("Enter the value of x0="))
y0=float(input("Enter the value of y0="))
n=float(input("Enter the value of h="))

print("","%.6f"%trap(x0,y0,n))