with open("bhola.txt","r") as  f:
    Counter = 0
  
    Content = f.read() 
    CoList = Content.split("\n") 
  
    for i in CoList: 
        if i: 
            Counter += 1
    records= Counter/6

    
while True:
    
    choice = int(input("Enter Choice"))
    
    if choice == 1:
        records += 1
        count = 0
        with open("bhola.txt","a+") as f:
                
                ProductCode  = input("Enter")
                Unit_Price   = input("Enter")
                Name_Disk    = input("Enter") 
                QtyInStock   = input("Enter")
                MinStockLevel = input("Enter")
                Discontinued = input("Enter")



                f.writelines(["ProductCode ",ProductCode,"\n"])
                f.writelines(["Unit_Price ",Unit_Price,"\n"])
                f.writelines(["Name_Disk ",Name_Disk,"\n"])
                f.writelines(["QtyInStock ",QtyInStock,"\n"])
                
                f.writelines(["MinStockLevel ",MinStockLevel,"\n"])
                f.writelines(["Discontinued ",Discontinued,"\n"])
                

    if choice == 2:
        code = int(input("enter"))
        with open("bhola.txt","r+") as f:
            while True:
                temp1 = f.readline().split(" ")
                if (temp1[1]) == code:
                    print("ProductCode entered ",code)
                    count = 0
                    while count !=5:
                        print(f.readline())
                        count += 1
                    break
                if not f.readline():
                    print("Wrong Code")
                    break
    if choice == 3:
        print("CODE--PRICE--DISK_NAME--QTY--MIN--DISCONTINUED")
        with open("bhola.txt","r+") as f:
            for i in range(int(records)):
                for i in range(6):
                    print(f.readline().split()[1],"--",end="")
                print("\n")

            
        
