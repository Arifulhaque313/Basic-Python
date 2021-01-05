def u_cal(u,n):
    temp=u
    for i in range(1,n):
        temp=temp*(u-i)
    return temp
def fact(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f
n=7
x=[0,1,2,3,4,5,6]
y=[[0 for i in range(n)]
       for j in range(n)]
y[0][0]=0
y[1][0]=.7
y[2][0]=1.8
y[3][0]=3.4
y[4][0]=5.1
y[5][0]=6.5
y[6][0]=7.3

for i in range(1,n):
    for j in range(n-i):
        y[j][i]=y[j+1][i-1]-y[j][i-1]

for i in range(n):
    print(x[i],end="\t")
    for j in range(n-i):
        print("","%.1f"%y[i][j],end="\t")
    print("")