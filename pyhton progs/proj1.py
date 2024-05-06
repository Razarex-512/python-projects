Max=200
import random



def disp_menu():
        print("1)Fill array\n2)Print\n3)Linear search\n4)Binary search\n5)Bubble sort\n6)bubble sort efficient\n7)insertion sort\n8)Quit")
def linear_search(data,item):
    for i in range(0,len(data)):
        if data[i]==item:
            print ("item is at index: ",i)
    else:        
                print("Not Found")

def binary_search(data,item):
    low=0
    high=Max-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if data[mid]<item:
            low=mid+1
        elif data[mid]>item:
            high=mid-1
        else:
            return mid
    return -1
def bubble_sort(data):
    n=len(data)
    for i in range (n-1):
        for j in range (0,n-i-1):
            if data[j]>data[j+1]:
                dtemp=data[j]
                data[j]=data[j+1]
                data[j+1]=dtemp
def bubble_sort_eff(data):
         n=len(data)
         for i in range (n-1):
                 flag=False
                 for j in range (0,n-i-1):
                    if data[j]>data[j+1]:
                        dtemp=data[j]
                        data[j]=data[j+1]
                        data[j+1]=dtemp
                        flag=True
                 if (flag==False):
                        break
def insertion_sort(data):
        for i in range(1,len(data)):
                ke=data[i]
                j=i-1
                while j>=0 and ke<data[j]:
                        data[j+1]=data[j]
                        j-=1
                        data[j+1]=ke
def main():
    data = [0] * Max
    while True:
     choice=0
     disp_menu()
     choice=int(input("Enter choice"))
     while choice<1 or choice>8:
         disp_menu()
         choice=int(input("Enter choice : "))
     if choice == 1:
         for i in range (0,Max):
          data[i]=random.randint(10,999)
     elif choice == 2:
             for i in range(len(data)):
              print("% d"% data[i]),
     elif choice == 3:
         item=int(input("Enter query"))
         linear_search(data,item)
     elif choice == 4:
         if data==sorted(data):
                 item=int(input("Enter query"))
                 res=binary_search(data,item)
                 if res !=-1:
                         print ("query is at index: ",str(res))
                 else:
                     print ("query is not present in array")
         else:
                 print("LiSt NoT sOrTeD (ab khush???)")
     elif choice == 5:
         bubble_sort(data)
     elif choice == 6:
             bubble_sort_eff(data)
     elif choice == 7:
             insertion_sort(data)
     elif choice==8:
             break
         
main()
