n=int(input("輸入比數n:"))
d={}
for i in range(n):
    m,n=input().split()
    d[m]=n
    print(m+"牌得到"+d[m]+"面")