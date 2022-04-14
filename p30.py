ans="1234"
b=input("請輸入數字(不能重複)")
c=0
e=0
for i in ans:
    for j in b:
        if i==j:
            if ans.index(i)==b.index(j):
                c+=1
            else:
                e+=1
print(str(c)+"A"+str(e)+"B")