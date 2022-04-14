info={}
n=int(input("輸入n值:"))
for i in range(n):
    name=input("請輸入姓名")
    email=input("請輸入電子郵件")
    info[name]=email
s=input("請輸入要查詢的電子郵件的姓名")
print(s+"電子郵件帳號為:"+str(info[s]))