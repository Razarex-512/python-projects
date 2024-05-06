class Stack: 
  def __init__(self, items = []): 
      self.items = list(items) 
       
  def pop(self): 
      self.items = self.items[1:] 
      return self.items 
       
  def push(self,item): 
      self.items = [item] + self.items 
      return self.items 
 
       
stack = Stack([1,2,3,4,5]) 
b = stack.push(12) 
print(b) 
b = stack.pop() 
print(b) 
b=stack.pop()
b=stack.pop()
print (b)