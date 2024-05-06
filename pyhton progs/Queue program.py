MAX=10
data=[""]*MAX
TOS=0
rear=-1
def isfull():
    if rear==MAX:
        return True
    else:
        return False
def isempty():
    if TOS<0 or TOS>rear:
        return True
    else:
        return False
def enqueue(data,val):
    global rear
    if (isfull()):
        print("Cannot push, queue is full at this time ")
        
    else:
        while rear == MAX-1:
            print ("queue out of space please pop ")
            return True
            
        rear=rear+1
        data[rear]=val
        return True
def dequeue(data):
    global TOS
    if (isempty()):
        print("queue is empty")
        TOS=0
        rear=-1
    else:
        queue=data[TOS]
        TOS=TOS+1
        return True
def main():
    while True:
        print("\nChoose out of the following\n1)Push into queue\n2)Pop out of queue\n3)Display queue\n4)Quit")
        choice=int(input("enter choice: "))
        while choice>4 or choice<1:
            print("\nChoose out of the following\n1)Push into queue\n2)Pop out of queue\n3)Display queue\n4)Quit\n:")
            choice=int(input("enter choice: "))
        if choice==1:
            val=input("What would you like to add")
            enqueue(data,val)
            print (rear)
        elif choice==2:
            dequeue(data)
        elif choice==3:
            i = TOS
            while i >=0 and i<=MAX-1 :
                print(data[i],end="  ")
                i=i+1
            i=0
        elif choice==4:
            print("Exiting program...")
            break
main()
