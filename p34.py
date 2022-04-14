n=int(input("請輸入一正整數:"))
if n<=1000 and n>=11:
    if (n%2==0 and n%11==0) and (n%5!=0 and n%7!=0):
        print(n,"為新公倍數?Yes")
    else:
        print(n,"為新公倍數?NO")
 