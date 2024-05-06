Number = int(input("Please Enter any 4 digit number Number: "))    
Reverse_of_number = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse_of_number = (Reverse_of_number *10) + Reminder    
    Number = Number //10    
     
print("\n Reverse of entered number is = %d" %Reverse_of_number)   
