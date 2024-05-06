list=[""]*10
TOS=-1
while True:
    choice=int(input("\n1)Push \n2)Pop \n3)Traverse \n4)Quit"))
    while choice>4:
        choice=int(input("1)Push \n2)Pop \n3)Traverse \n4)Quit"))
    if choice==1:
        if TOS<9:
            push=input("what do you want to push?")
            TOS=TOS+1
            list[TOS]=push
            print(list)
        else:
            print("the stack is full StAcK oVurFlOw")
    elif choice==2:
        if TOS == -1 :
            print("Empty")
        else:
            i = TOS
            while i >=0 :
                print(list[i],end="  ")
                i-=1
    elif choice==3:
        i = TOS
        while i >=0 :
            print(list[i],end="  ")
            i-=1
            print(list)
    else:
        print("see you next time")
        break

