a_list=input("輸入一整數序列為:").split()
b="no"
for i in a_list:
    if a_list.count(i)>len(a_list)/2:
        b=i
        print("過半元素為"+i)
    else:
        print("過半元素為"+b)