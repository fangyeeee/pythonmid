c=int(input("班級數"))
d=[]
if c>=1 and c<=10:
    for i in range(c):
        b=str(input())
        d.append(b)
    print(max(d))