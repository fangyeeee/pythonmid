m=75
k=float(input("請輸入路程公里數(km)"))
a=(k-1.5)*1000%250
b=(k-1.5)*1000//250
if k<1.5:
    print("所需車資為:",m)
elif k>1.5 and a==0:
    print("所需車資為:",m+(b*5))
elif k>1.5 and a>=250:
    print("所需車資為:",m+(b*5))
elif k>1.5 and a<250:
    print("所需車資為:",m+5+(b*5))