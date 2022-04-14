m=int(input("請輸入月租費形式"))
t=int(input("請輸入通話費時間"))
if m==186:
    if round(t*0.09/(186*2))>1:
        print("通話費為"+str(round(t*0.09*0.8)))
    elif round(t*0.09/(186*2))<1:
        print("通話費為"+str(round(t*0.09*0.9)))
if m==386:
    if round(t*0.09/(386*2))>1:
        print("通話費為"+str(round(t*0.08*0.7)))
    elif round(t*0.09/(386*2))<1:
        print("通話費為"+str(round(t*0.08*0.8)))
if m==586:
    if round(t*0.09/(586*2))>1:
        print("通話費為"+str(round(t*0.07*0.6)))
    elif round(t*0.09/(586*2))<1:
        print("通話費為"+str(round(t*0.07*0.7)))
if m==986:
    if round(t*0.09/(986*2))>1:
        print("通話費為"+str(round(t*0.06*0.5)))
    elif round(t*0.09/(986*2))<1:
        print("通話費為"+str(round(t*0.06*0.6)))