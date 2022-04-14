n=int(input("請輸入n"))
k=int(input("請輸入k"))
if k>=1:
    print("PETER可以抽"+(str(n+n//k+n//k//k))+"支菸")