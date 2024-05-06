import random
Max=10
data=[0]*Max
for k in range (0,Max):
          data[k]=random.randint(10,99)
data.sort()
if data==sorted(data) :
        print ("data is sorted g")
        print(data)
else:
        print("not sorted0")
        print(data)

def flip(array):

    max_ = len(array)-1
    min_ = 0

    while max_>min_:

        temp = array[max_]
        array[max_] = array[min_]
        array[min_] = temp
        max_-=1
        min_+=1

flip(data)

print(data)
        
