
def f(x,y):
    return x+y
def rk(x0,y0,h):
    n=1
    y=y0

    for i in range(1,n+1):

        k1=h*f(x0,y0)
        k2=h*f(x0+h/2,y+k1/2)
        k3=h*f(x0+h/2,y+k2/2)
        k4=h*f(x0+h,y+k3)

        y+=1/6*(k1+2*k2+2*k3+k4)
        x0=x0+h
    return y
x0=float(input("Enter the value of x0="))
y0=float(input("Enter the value of y0="))
n=float(input("Enter the value of h="))

print("","%.6f"%rk(x0,y0,n))