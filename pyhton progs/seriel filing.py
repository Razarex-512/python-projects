import pickle
import os

class Product:
    ProductID=0
    Name=" "
    UnitPrice=0.0
    Discontinued=False

def add_rec():
    NewRec=Product()
    NewRec.ProductID=int(input("Enter product ID : "))
    NewRec.Name=input("Enter product name : ")
    NewRec.UnitPrice=float(input("Enter Unit price : "))
    dis=input("Is this product in stock? Y/N: ")
    if dis=="Y" or dis=="y":
        NewRec.Discontinued=False
    elif dis=="N" or dis=="n":
        NewRec.Discontinued=True
    fptr=open("products.dat","ab")
    pickle.dump(NewRec,fptr)
    fptr.close()

def print_all():
    TempRec=Product()
    fptr=open("products.dat","rb")
    fptr.read()
    eof=fptr.tell()
    fptr.seek(0)
    while fptr.tell()!=eof:
        TempRec=pickle.load(fptr)
        print("Product ID               : ",TempRec.ProductID)
        print("Product Name             : ",TempRec.Name)
        print("Unit Price               : ",TempRec.UnitPrice)
        print("Discontinued Status      : ",TempRec.Discontinued)
        print("\n**************************************************")

def delete(item):
    TempRec=Product()
    fptr1=open("products.dat","rb")
    fptr2=open("Temp.dat","wb")
    fptr1.read()
    eof=fptr1.tell()
    fptr1.seek(0)
    found=False
    while fptr1.tell()!=eof:
        TempRec=pickle.load(fptr1)
        if TempRec.ProductID==item:
            found=True
        else:
            pickle.dump(TempRec,fptr2)
    fptr1.close()
    fptr2.close()
    if found==False:
        print("Record not found")
        os.remove("Temp.dat")
    else:
        os.remove("Products.dat")
        os.rename("Temp.dat","Products.dat")


choice=0
while choice!=9:
    
    print("\n1)       Add a Record\n2)       Print all Records\n3)       Search a Record by ID\n4)       Delete a Record \n5)       Total Stock Value\n6)       List the discontinued products\n7)       List the continued products\n8)       list of items above 100.00\n9)       Exit")
    choice=int(input("\nEnter your choice:   "))
    if choice==1:
        add_rec()
    if choice==2:
        print_all()
    if choice==3:
        item=int(input("\nEnter Product ID: "))
        TempRec=Product()
        fptr1=open("products.dat","rb")
        fptr1.read()
        eof=fptr1.tell()
        fptr1.seek(0)
        found=False
        while fptr1.tell() != eof :
            TempRec=pickle.load(fptr1)
            if TempRec.ProductID==item:
                found=True
                prodname= TempRec.Name
        fptr1.close()
        if found == True:
            print ("\n-->item "+str(prodname)+" with ID : "+str(item)+" found"  )
        else:
            print("not found")
    if choice==4:
        item=int(input("Enter item ID: "))
        delete(item)
    if choice==5:
        total_price=0
        c=0
        TempRec=product()
        fptr1=open("products.dat","rb")
        fptr1.read()
        eof=fptr1.tell()
        fptr1.seek(0)
        found=False
        while fptr1.tell() != eof :
            TempRec=pickle.load(fptr1)
            total_price=total_price + TempRec.UnitPrice
            c=c+1
        print("\n-->Total stock price for "+str(c)+" items is: "+str(total_price))
        fptr1.close()
    if choice==6:
        TempRec=Product()
        fptr=open("products.dat","rb")
        fptr.read()
        eof=fptr.tell()
        fptr.seek(0)
        while fptr.tell()!=eof:
            TempRec=pickle.load(fptr)
            if TempRec.Discontinued==True:
                print("\n-> ",TempRec.Name," is discontinued")
        fptr.close()
    if choice==7:
        TempRec=Product()
        fptr=open("products.dat","rb")
        fptr.read()
        eof=fptr.tell()
        fptr.seek(0)
        while fptr.tell()!=eof:
            TempRec=pickle.load(fptr)
            if TempRec.Discontinued==False:
                print("\n-> ",TempRec.Name," is in stock")
        fptr.close()
    if choice==8:
        TempRec=Product()
        fptr=open("products.dat","rb")
        fptr.read()
        eof=fptr.tell()
        fptr.seek(0)
        while fptr.tell()!=eof:
            TempRec=pickle.load(fptr)
            if TempRec.UnitPrice>100:
                print("\n-> ",TempRec.Name," is above 100 usd")
        fptr.close()        
    
        
