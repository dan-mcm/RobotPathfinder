'''
Created on Mar 9, 2017

@author: Daniel McMahon
'''

from src.linked_list import LinkedList
from src.linked_list import Node

class stackADT_linkedlist:
    
    def __init__(self):
        self.storage = LinkedList()
        #counter will be used to get full size of the list
        self.counter = 0
     
    def stackPUSH(self,item):
        '''adds element to stack - initially named push, renamed to prevent confusion when reading world.py'''
        self.storage.add_head(Node(item))
        #increases total counter by 1
        self.counter += 1
     
    def pop(self):
        '''removes element from stack'''
        #reduces total counter by 1
        self.counter -= 1
        return self.storage.remove_head()
         
    def viewStack(self):
        '''easy way to view entire contents of stack'''
        return self.storage
                
    def size(self):
        return self.counter