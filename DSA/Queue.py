


class Queue:
    
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
        
    def dqueue(self,item):
        if len(self.queue)<1:
            return None
        self.queue.pop(item)
    
    def display(self):
        print(self.queue)
    
    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(22)
q.enqueue(25)
q.enqueue(32)
q.enqueue(72)
q.display()
q.dqueue(0)
q.dqueue(1)
q.size()
q.display()
