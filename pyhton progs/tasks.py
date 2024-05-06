m1=int(input("input marks for test 1 "))
m2=int(input("input marks for test 2 "))
if ((((m1+m2)/200)*100)>=45):
    print ("passed with ",(((m1+m2)/200)*100),"%")
else:
    print("youve failed with a whopping ",(((m1+m2)/200)*100),"%")
