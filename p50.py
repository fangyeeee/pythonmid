a=set(["John","Mary","Tina","Fiona","Eva","Ben","Bill","Bert"])
e=set(["John","Mary","Fiona","Claire","Ben","Bill"])
m=set(["Mary","Fiona","Claire","Ben"])
print("英文與數學都及格",(e&m))
print("數學不及格",(a-m))
print("英文及格且數學不及格",(e&(a-m)))
