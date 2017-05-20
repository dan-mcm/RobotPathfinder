'''
Created on Mar 5, 2017

@author: Daniel McMahon
'''
     
class stackADT:
    def __init__(self):
        self.storage = []
    
    def stackPUSH(self,item):
        '''adds element to stack - initially named push, renamed to prevent confusion when reading world.py'''
        self.storage.append(item)
        #return self.storage
    
    def pop(self):
        '''removes element from stack'''
        return self.storage.pop()
        #return self.storage
        
    def viewStack(self):
        '''easy way to view entire contents of stack'''
        return self.storage
    
    def checkLast(self):
        '''checks second last element added to stack - used to prevent doubling back...'''
        if len(self.storage) == 0:
            return 0
        else:
            return self.storage[len(self.storage)-2]
        
    def size(self):
        return len(self.storage)
    