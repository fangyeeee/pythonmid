x=int(input("請輸入X軸座標"))
y=int(input("請輸入y軸座標"))
if x==0 and y==0:
    print("該座標位於原點上")
elif x>0 and y>0:
    print("該座標位於第一象限")
    print("離原點距離為根號"+str(x*x+y*y))
elif x<0 and y>0:
    print("該座標位於第二象限")
    print("離原點距離為根號"+str(x*x+y*y))
elif x<0 and y<0:
    print("該座標位於第三象限")
    print("離原點距離為根號"+str(x*x+y*y))
elif x>0 and y<0:
    print("該座標位於第四象限")
    print("離原點距離為根號"+str(x*x+y*y))
elif x==0 and y>0:
    print("該座標位於上半面y軸上")
    print("離原點距離為根號"+str(x*x+y*y))
elif x==0 and y<0:
    print("該座標位於下半面y軸上")
    print("離原點距離為根號"+str(x*x+y*y))
elif x>0 and y==0:
    print("該座標位於右半面x軸上")
    print("離原點距離為根號"+str(x*x+y*y))
elif x<0 and y==0:
    print("該座標位於左半面x軸上")
    print("離原點距離為根號"+str(x*x+y*y))
