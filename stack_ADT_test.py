'''
Created on Mar 9, 2017

@author: Daniel McMahon
'''

import sys
from src.stack_ADT import stackADT

def test(did_pass):
    """print the results of a test"""
    line_num = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = ("Test at line {0} ok.".format(line_num))
    else:
        msg = ("Test at line {0} FAILED.".format(line_num))
    print(msg)
    
def tests_simple():
    
    #makes initial stack for testing
    stack = stackADT()
    
    #pushes element to stack - tests it contains the value
    stack.stackPUSH([5,0])
    test(stack.viewStack() == [[5,0]])
    
    #further pushes to the stack
    stack.stackPUSH([4,1])
    stack.stackPUSH([3,2])
    
    #examines second last element added to stack
    test(stack.checkLast()==[4,1])
    
    #removing top elements from stack
    stack.pop()
    
    #checking elements were removed
    test(stack.checkLast()==[5,0])
    
    #checking view of overall stack at this point
    test(stack.viewStack()==[[5,0],[4,1]])
    
    test(stack.size() == 2)
    
if __name__ == "__main__":    
    tests_simple()