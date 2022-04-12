a=int(input("輸入使用度數"))
s="夏月"
n="非夏月"
if a <= 120:
    print("summer months:" + str(a*2.10))
    print("Non-Summer months:" + str(a*2.10))
elif a>121 and a<=330:
    print("summer months:" + str(a*3.02))
    print("Non-Summer months:" + str(a*2.68))
elif a>331 and a<=500:
    print("summer months:" + str(a*4.39))
    print("Non-Summer months:" + str(a*3.61))
elif a>501 and a<=700:
    print("summer months:" + str(a*4.97))
    print("Non-Summer months:" + str(a*4.01))
elif a>700:
    print("summer months:" + str(a*5.63))
    print("Non-Summer months:" + str(a*4.50))
