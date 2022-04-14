a=input("請輸入要檢測字元(end結束)")
if a=="end":
    print("檢測結束")
else:
    b=input("要檢測的字元")
    print("字元"+str(b)+"出現的次數為"+str(a.count(b)))

