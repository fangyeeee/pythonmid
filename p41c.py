t=int(input("搭了幾次電梯"))
f=1
m=0
for i in range(t):
    n=int(input())
    if n>f:
        m+=(n-f)*20
    elif n<f:
        m+=(f-n)*10
    f=n
print(str(m)+"元")
