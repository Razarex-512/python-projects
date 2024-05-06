import random
hidden=random.randrange(1,9999)
guess=int(input("enter your guess (hint:its between 1 to 10"))
h1=hidden%10
if guess==hidden:
    print ("thats exactly right")
elif guess>hidden:
    print ("oo that is higher than",hidden)
else:
    print("damn that is a bit lower than",hidden)
