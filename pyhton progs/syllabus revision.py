import random
from re import M
mylist=[""]*10
for k in range (len(mylist)):
    mylist[k]=random.randint(0,99)
item=int(input("enter Item to be found:"))
found=False
for i in range (len(mylist)):
    if mylist[i]==item:
        found=True
if found==True:
    print("item found")
    print(mylist)
else:
    print("not found")
    print(mylist)