print("Md.Ariful Haque \nId:173462130")
def f(x,y):
    return(3*x+y*y)
def rk(x0,y0,h):
    y=y0
    n=1
    for i in range(1,n+1):
        k1=h*f(x0,y0)
        k2=h*f(x0+h/2,y+k1/2)
        k3 = h * f(x0 + h / 2, y + k2/ 2)
        k4 = h * f(x0 + h, y + k3)
        y+=(1/6)*(k1+2*k2+2*k3+k4)
        x0+=h
    return y
x0=float(input("Enter the value of x0="))
y0=float(input("Enter the value of y0="))
h=float(input("Enter the value of h="))

print("The answer is= ","%.6f"%rk(x0,y0,h))