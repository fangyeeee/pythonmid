n=int(input("輸入筆數n:"))
a={}
for i in range(n):
    e,c=input().split()
    a[e]=c
b=input("輸入欲查詢單字")
if b in a:
    print(b+"中文意思為:"+a[b])
else:
    print("字典未有此單字")
