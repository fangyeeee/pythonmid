a=input("請輸入一組四位數字")
b=[]
for i in a:
    b.append((int(i)+7)%10)
print(str(b[2])+str(b[3])+str(b[0])+str(b[1]))
