
'''

Push → inserting an element into the stack

Pop → deleting an element from the stack


'''

class Stack():
    
    def __init__(self):
        self.data = []
    
    def is_overflow(self):
        if len(self.data) == 5:
            print(" Satck Overflow ")
        else:
            print(" Stack Underflow")
            
            
    def push(self,elements):
        if len(self.data)==5:
            print( "Stack Overflow" )
        else:
            self.data.append(elements)
    
    
    def pop(self):
        if len(self.data)==0:
            print( "Satck Underflow" )
        else:
            self.data.pop()
 
s1 = Stack()
s1.push(11)
s1.push(13)
s1.push(14)
s1.push(11)
s1.push(12)
s1.push(10)
s1.push(19)
print(s1.is_overflow())
s1.pop()
s1.pop()
s1.pop()
s1.push(23)