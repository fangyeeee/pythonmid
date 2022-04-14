a=str(input("請輸入傳送密碼(6位數)"))
b=[]
for i in range(len(a)):
    if len(a)==6:
        b.append(int(a[i])*4%7)
print(str(b))
