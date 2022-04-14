a=int(input("請輸入a"))
b=int(input("請輸入b"))
c=int(input("請輸入c"))
x0=b**2-4*a*c
x=(-b+(x0)**(1/2))/2*a
x1=(-b-(x0)**(1/2))/2*a
if x0==0:
    print(x)
elif x0<0:
    print('0')
elif x0>0:
    print(str(x))
    print(str(x1))
