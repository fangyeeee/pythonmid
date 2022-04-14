n=int(input("輸入幾個點"))
if n>=2 and n<=10:
    for i in range(n):
        a=int(input())
        if a>=1 and a<=1000:
            if a%9==0 or a%11==0:
                print("第"+str(i+1)+"個點"+str(a))
        