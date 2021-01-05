def f(x,y):
    return x+y
def rk(x0,y0,h):
    y=y0
    n=1
    for i in range(1,n+1):
        k1=h*f(x0,y0)
        k2=h*f(x0+h/2,y+k1/2)
        k3 = h * f(x0 + h / 2, y + k2 / 2)
        k4=h*f(x0+h,y+k3)

        y+=(1/6)*(k1+2*k2+2*k3+k4)
        x0=x0+h
    return y
x=0
y0=1
h=0.1

print(rk(x,y0,h))