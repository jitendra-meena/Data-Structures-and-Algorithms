"""
The queue is a linear data structure where elements are in a sequential manner.
        It follows the F.I.F.O mechanism that means first in first out.
Think when you go to the cinema with your friends, as you can imagine the first of you that give the ticket is also
       the first that step out of the line. The mechanism of the queue is the same.


"""


class Queue:
    
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        if len(self.queue) <= 5:
            self.queue.append(item)
        else:
            return "overflow"
            
    def dqueue(self,item):
        if len(self.queue)==0:
            return "underflow"
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
