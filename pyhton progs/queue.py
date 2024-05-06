class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def equeue(self, item):
        self.items.insert(0,item)

    def unqueue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
q=Queue()
	
q.equeue(4)
q.equeue('dog')
q.equeue(True)
print(q.size())
