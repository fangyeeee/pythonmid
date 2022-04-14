n=int(input("輸入比數n:"))
m=[]
for i in range(n):
    m.append(input().split())
for ms in m:
    print(ms[0]+"牌的到"+ms[1]+"面")