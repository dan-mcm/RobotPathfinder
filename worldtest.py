'''
Created on Mar 7, 2017

@author: Daniel McMahon
'''
import sys
from src.world import World

def test(did_pass):
    """print the results of a test"""
    line_num = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = ("Test at line {0} ok.".format(line_num))
    else:
        msg = ("Test at line {0} FAILED.".format(line_num))
    print(msg)
    
def tests_simple():
    
    #Creates an empty world
    earth = World(3,3)
    
    #Inserts robot
    earth.insertRobot("r2d2",1,1)
    
    #Inserts walls
    earth.insertWalls(0,1)
    
    #Inserts goal
    earth.insertGoal(2,2)

    #testing where robot is
    test(earth.where_is_robot() == [1,1])
    
    #testing feasible locations
    test(earth.is_feasible(1,2) == True)
    test(earth.is_feasible(1,0) == True)
    test(earth.is_feasible(2,1) == True)
    test(earth.is_feasible(0,0) == True)
    test(earth.is_feasible(0,1) == False)
    
    #testing movement
    earth.move_robot(1,2)
    earth.move_robot(1,1)
    earth.move_robot(1,0)
    
    #testing where robot is
    test(earth.where_is_robot() == [1,0])
    
    #testing movement
    earth.move_robot(1,1)
    earth.move_robot(1,2)
    earth.move_robot(2,2)
    
    #testing where robot is
    test(earth.where_is_robot() == [2,2])
    
    #testing movement
    earth.move_robot(2,1)
    earth.move_robot(2,0)
    
    #testing where robot is
    test(earth.where_is_robot() == [2,0])
    
    #testing movement
    earth.move_robot(2,1)

    #testing where robot is
    test(earth.where_is_robot() == [2,1])
    
    #moving towards goal
    earth.move_robot(2,2)
    
    #goal reached
    test(earth.goal_reached() == True)

if __name__ == "__main__":    
    tests_simple()