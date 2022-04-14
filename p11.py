m=int(input("請輸入月份"))
d=int(input("請輸入日期"))
if m==3 and d>=21 or m==4 and d<=19:
    print("星座為牧羊座")
elif m==4 and d>=20 or m==5 and d<=20:
    print("星座為金牛座")
elif m==5 and d>=21 or m==6 and d<=21:
    print("星座為雙子座")
elif m==6 and d>=22 or m==7 and d<=22:
    print("星座為巨蟹座")
elif m==7 and d>=23 or m==8 and d<=22:
    print("星座為獅子座")
elif m==8 and d>=23 or m==9 and d<=22:
    print("星座為處女座")
elif m==9 and d>=23 or m==10 and d<=23:
    print("星座為天秤座")
elif m==10 and d>=24 or m==11 and d<=22:
    print("星座為天蠍座")
elif m==11 and d>=23 or m==12 and d<=21:
    print("星座為射手座")
elif m==12 and d>=22 or m==1 and d<=19:
    print("星座為魔羯座")
elif m==1 and d>=20 or m==2 and d<=18:
    print("星座為水瓶座")
elif m==3 and d>=21 or m==3 and d<=19:
    print("星座為雙魚座")