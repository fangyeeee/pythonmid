a=input("請輸入第一組數字")
b=input("請輸入第二組數字")
c=0
e=0
if (len(a)>=2 and len(a)<=6) and (len(b)>=2 and len(b)<=6):
    for i in a:
        for j in b:
            if i==j:
                if a.index(i)==b.index(j):
                    c+=1
                else:
                    e+=1
if c==4 and e==0:
    print(str(c)+"A"+str(e)+"B"+"全對")
else:
    print(str(c)+"A"+str(e)+"B"+"加油")

