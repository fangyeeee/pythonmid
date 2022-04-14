a={"123 456":9000,"456 789":5000,"789 888":6000,"336 558":10000,"775 666":12000,"566 221":7000}
b=int(input("輸入查詢組數N為:"))
for i in range(b):
    aa=input()
    if aa in a:
        print(a[aa])
    else:
        print("error")