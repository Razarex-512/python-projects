m1=int(input("enter marks 1"))
m2=int(input("enter marks 2"))
if ((m1+m2)>160):
    if(m2>80):
        if(m1>80):
            print ("distinction")
        else:
            print("merit")
    else:
        print("merit")
elif(160>=(m1+m2)>120):
    print("credit")
elif(120>=(m1+m2)>100):
    print("pass")
else:
    print("Fail")
      
