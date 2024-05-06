import pickle
import os
from tempfile import tempdir

class employee:
    EmployeeID=0
    Name=" "
    EmpSal=0.0
    Department=" "

def add_emp():
    s=os.path.isfile("Employees.dat")
    if s==False:
        NewRec=employee()
        NewRec.EmployeeID=int(input("Enter Employee ID : "))
        NewRec.Name=input("Enter Employee name : ")
        NewRec.EmpSal=float(input("Enter Employee salary : "))
        NewRec.Department=input("Sales,HR or Development")
        fptr=open("Employees.dat","ab")
        pickle.dump(NewRec,fptr)
        fptr.close()
    else:
        NewRec=employee()
        found=True
        while found==True:
            NewRec.EmployeeID=int(input("Enter Employee ID: "))
            item=NewRec.EmployeeID
            TempRec=employee()
            fptr1=open("Employees.dat","rb")
            fptr1.read()
            eof=fptr1.tell()
            fptr1.seek(0)
            found=False
            while fptr1.tell() != eof :
                TempRec=pickle.load(fptr1)
                if TempRec.EmployeeID==item:
                    found=True
                    Emp_ID= TempRec.Name
                    print("\n-->employee "+str(Emp_ID)+" already has ID : "+str(item)+" in use\nchoose another ID: "  )      
            fptr1.close()
        NewRec.Name=input("Enter Employee Name: ")
        NewRec.EmpSal=float(input("Enter Employee Salary: "))
        NewRec.Department=input("Sales,HR or Development: ")
        fptr1=open("Employees.dat","rb")
        fptr2=open("Temp.dat","ab")
        fptr1.read()
        eof=fptr1.tell()
        fptr1.seek(0)
        bigger=False
        while fptr1.tell()!=eof:
            TempRec=pickle.load(fptr1)
            if TempRec.EmployeeID<item:
                bigger=True
            elif TempRec.EmployeeID>item:
                bigger=False
        fptr1.close()
        if bigger==True:
            fptr1=open("Employees.dat","rb")
            fptr1.read()
            eof1=fptr1.tell()
            fptr1.seek(0)
            while fptr1.tell()!=eof1:
                Tc=pickle.load(fptr1)
                pickle.dump(TempRec,fptr2)
                print(TempRec)
            pickle.dump(NewRec,fptr2)
            fptr1.close()
            fptr2.close()
        else:
            fptr1=open("Employees.dat","rb")
            fptr1.read()
            eof2=fptr1.tell()
            fptr1.seek(0)
            fptr3=open("Temp.dat","rb")
            fptr3.read()
            eof=fptr3.tell()
            fptr3.seek(0)
            while fptr1.tell()!=eof2:
                Tc=pickle.load(fptr1)
                if Tc.EmployeeID<item:
                    pickle.dump(Tc,fptr2)
                elif Tc.EmployeeID>item:
                    while fptr3.tell() != eof :
                        TempRec=pickle.load(fptr1)
                        if TempRec.ProductID==item:
                            pickle.dump(Tc,fptr2)

                        else:
                            pickle.dump(NewRec,fptr2)
                            pickle.dump(Tc,fptr2)
                    fptr3.close()
            fptr1.close()
            fptr2.close()
        os.remove("Employees.dat")
        os.rename("Temp.dat","Employees.dat")

def print_all():
    fptr=open("Employees.dat","rb")
    fptr.read()
    eof=fptr.tell()
    fptr.seek(0)
    while fptr.tell()!=eof:
        TempRec=pickle.load(fptr)
        print("Employee ID               : ",TempRec.EmployeeID)
        print("Employee Name             : ",TempRec.Name)
        print("Employee salary           : ",TempRec.EmpSal)
        print("Employee Department       : ",TempRec.Department)
        print("\n**************************************************")

choice=0
while choice!=6:
    choice=int(input("menu:"))
    if choice==1:
      add_emp()
    if choice==2:
        print_all()
