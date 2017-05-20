'''
Created on Mar 5, 2017

@author: Daniel McMahon
'''

from src.stack_ADT import stackADT

class World:
    
    def __init__(self,width,height):
        '''initiates a new world - all spaces blank by default'''
        self.width = width
        self.height = height
 
        world = []
        for i in range (0,height):
            world.append([0]*width)
        self.world = world
    
    def insertWalls(self,x1,y1):
        '''inserts wall values on instance os a world depending on file that is read in main function'''
        self.world[x1][y1] = 1
    
    def insertRobot(self,name,x1,y1):
        '''inserts robot value on instance of a world depending on file that is read in main function'''
        self.robotname = name
        self.world[x1][y1] = name
        self.robotx1=x1
        self.roboty1=y1

    def insertGoal(self,x1,y1):
        '''inserts goal value on instance of a world depending on file that is read in main function'''
        self.goalx1 = x1
        self.goaly1 = y1
        self.world[x1][y1] = "G"

    def create_world(self):
        '''Note: this only prints the world as such - world is created by default in initialization of class'''
        
        for elem in self.world:
            print(elem)
        
    def where_is_robot(self):
        '''Scans a world instance for the robot value'''
        for i in range (0,self.height):
            for j in range(0,self.width):
                if self.world[i][j] == "r2d2": #this was 'G' before everything broke...
                    self.robotx1 = i
                    self.roboty1 = j
                    return [self.robotx1,self.roboty1]
#                     print("Robot is currently at: ", "x:", self.robotx1, "y:", self.roboty1)
#                     print()
    
    # may be able to improve efficiency without nesting the loops...
    def is_feasible(self,x2,y2):
        '''checks if a move is feasible by checking input coordinates relative to robot position'''
        if x2<self.height and x2>-1 and y2<self.width and y2>-1:
            if self.world[x2][y2] != 1:
                if x2 == self.robotx1+1 or x2 == self.robotx1-1 or x2 == self.robotx1:
                    if y2 == self.roboty1+1 or y2 == self.roboty1-1 or y2 == self.roboty1:
                        #test statements
                        #print("Moving... *beep*")
                        #print()
                        return True
                    else:
                        #test statements
                        #print("Move is too far away! I can only move one space at a time! *beep*")
                        #print()
                        return False
                else:
                    #test statements
                    #print("Move is too far away! I can only move one space at a time! *beep*")
                    #print()
                    return False
            else:
                #test statements
                #print("Invalid Move - Wall in the Way - Crash Imminent.")
                #print("I refuse to kill myself for your amusement - try another move.")
                #print()
                return False
        else:
            #test statements
            #print("Move is outside map area! Use coordinates within map size. Try Again.")
            #print()
            return False
    
    def move_robot(self,x1,y1):
        '''function that moves robots coordinates - also prints updated world'''
        if self.is_feasible(x1,y1):
            self.world[self.robotx1][self.roboty1] = 0
            self.robotx1 = x1
            self.roboty1 = y1
            self.world[self.robotx1][self.roboty1] = self.robotname
            return self.world
#         for elem in self.world:
#             print(elem)


    def goal_reached(self):
        '''function that tests if goal has been reached'''
        if self.world[self.goalx1][self.goaly1] == self.robotname:
            #print("VICTORY!!!!")
            return True
        else:
            return False
        
# Note: requirement to take x1/y1 arguments here.... not a single direction... le sigh. 
# Leaving legacy code here as reference - may come in useful if checking n,s,e,w co-ords
#
#     def move_robot(self,direction):
#         if direction == "n":
#             
#       
#             #if self.is_feasible(self.roboty1-1,self.robotx1):
#             if self.world[self.robotx1-1][self.roboty1] != 1:
#                 self.world[self.robotx1][self.roboty1] = 0
#                 self.robotx1 = self.robotx1 - 1
#                 self.world[self.robotx1][self.roboty1] = self.robotname
#             else:
#                 print("Invalid Move - Wall in the Way - Crash IMMINENT!")
#                 
#         if direction == "s":
#             if self.world[self.robotx1+1][self.roboty1] != 1:
#                 self.world[self.robotx1][self.roboty1] = 0
#                 self.robotx1 = self.robotx1 + 1
#                 self.world[self.robotx1][self.roboty1] = self.robotname
#             else:
#                 print("Invalid Move - Wall in the Way - Crash IMMINENT!")
# 
#         if direction == "e":
#             
#             if self.world[self.robotx1][self.roboty1+1] != 1:
#                 
#                 self.world[self.robotx1][self.roboty1] = 0
#                 self.roboty1 = self.roboty1 + 1
#                 self.world[self.robotx1][self.roboty1] = self.robotname
#                 
#             else:
#                 print("Invalid Move - Wall in the Way - Crash IMMINENT")
#                 
#         if direction == "w":
#             
#             if self.world[self.robotx1][self.roboty1-1] != 1:
#                 
#                 self.world[self.robotx1][self.roboty1] = 0
#                 self.roboty1 = self.roboty1 - 1
#                 self.world[self.robotx1][self.roboty1] = self.robotname
#             else:
#                 print("Invalid Move - Wall in the Way - Crash IMMINENT")
#             
#         #may wish to remove later - reprints world....
#         for elem in self.world:
#             print(elem)
        
    
        
        
        
# does not work inside class as need to access stackADT push methods on recursion calls.......
# a painful lesson in having to move function and change self variable....
# 
#     def find_path(self,world,current_path,rx1,ry1,gx1,gx2):
#         
#         if self.robotx1 == self.goalx1 and self.roboty1 == self.goaly1:
#             print("Victory!")
#             return True
#         
#         #if robot can't move
#         if self.is_feasible(self.robotx1+1,self.roboty1)==False and self.is_feasible(self.robotx1-1,self.roboty1)==False and self.is_feasible(self.robotx1,self.roboty1+1)==False and self.is_feasible(self.robotx1,self.roboty1-1)==False:
#             print("Trapped!") 
#             return False
#         
#         #if robot can move north...
#         if self.is_feasible(self.robotx1-1,self.roboty1)==True:
#             return self.find_path(self.world,current_path.push((self.robotx1-1,self.roboty1)),self.robotx1-1,self.roboty1,self.goalx1,self.goaly1)
#         #if robot can move south...
#        
#         if self.is_feasible(self.robotx1+1,self.roboty1)==True:
#             return self.find_path(self.world,current_path.push((self.robotx1+1,self.roboty1)),self.robotx1+1,self.roboty1,self.goalx1,self.goaly1)
#         
#         #if robot can move west...
#         if self.is_feasible(self.robotx1,self.roboty1-1)==True:
#             return self.find_path(self.world,current_path.push((self.robotx1+1,self.roboty1-1)),self.robotx1+1,self.roboty1-1,self.goalx1,self.goaly1)
#         
#         #if robot can move east...
#         if self.is_feasible(self.robotx1,self.roboty1+1)==True:
#             return self.find_path(self.world,current_path.push((self.robotx1+1,self.roboty1+1)),self.robotx1+1,self.roboty1+1,self.goalx1,self.goaly1)
#             
        


def find_path(world,current_path,rx1,ry1,gx1,gy1):
    
    #current_path.viewStack() #test statement... displays results
        
    #may be better to use goalreached function however
    #currently not working when used with find_path....
    if rx1 == gx1 and ry1 == gy1:
        print()
        print("GOAL!!!!!!!!!!!!!!!!!!!!!!!!! (arrived at goal)")
        print()
        print("Here is what the stack trail looks like:")
        print(current_path.viewStack())
        return True
        
        #if robot can't move
    elif world.is_feasible(rx1+1,ry1)==False and world.is_feasible(rx1-1,ry1)==False and world.is_feasible(rx1,ry1+1)==False and world.is_feasible(rx1,ry1-1)==False:
        print("Trapped!") 
        return False
    
    else:
        test = current_path.checkLast()
        
        #if robot can move south... and if we weren't there 2 moves ago.
        if world.is_feasible(rx1+1,ry1) and test != [rx1+1,ry1]:
            #print("Moving South")
            #print((rx1+1,ry1)==current_path.checkLast())
            current_path.stackPUSH([rx1+1,ry1])
            world.robotx1 = rx1+1
            return find_path(world,current_path,rx1+1,ry1,gx1,gy1)
        
        #if robot can move north... and if we weren't there 2 moves ago.
        if world.is_feasible(rx1-1,ry1) and test != [rx1-1,ry1]:
            #print("Moving North")
            #print((rx1-1,ry1)==current_path.checkLast())
            current_path.stackPUSH([rx1-1,ry1])
            world.robotx1=rx1-1
            return find_path(world,current_path,rx1-1,ry1,gx1,gy1)
        
        #if robot can move east... and if we weren't there 2 moves ago.
        if world.is_feasible(rx1,ry1+1) and test != [rx1,ry1+1]:
            #print("Moving East")
            #print((rx1,ry1+1)==current_path.checkLast())
            current_path.stackPUSH([rx1,ry1+1]) #push move to stack - had as tuples initially.... lists more flexible?
            world.roboty1=ry1+1 #move robot - allows for accurate checking on next turn...
            return find_path(world,current_path,rx1,ry1+1,gx1,gy1)   
            
        #if robot can move west... and if we weren't there 2 moves ago.
        if world.is_feasible(rx1,ry1-1) and test != [rx1,ry1-1]:
            #print("Moving West")
            #print((rx1,ry1-1)==current_path.checkLast())
            current_path.stackPUSH([rx1,ry1-1])
            world.roboty1=ry1-1
            return find_path(world,current_path,rx1,ry1-1,gx1,gy1)

def main():

    fileInput = "world1.dat"

    with open(fileInput) as file:
        map_details = file.readline()
        width = int(map_details.split("x")[0])
        height = int(map_details.split("x")[1])
        test = World(width,height)
    
        for line in file:
            if line.startswith("w"):
                postW = line.split(" ")[1]
                w1 = int(postW.split(",")[0])
                w2 = int(postW.split(",")[1])
                test.insertWalls(w1,w2)
                 
            if line.startswith("goal"):
                postG = line.split(" ")[1]
                x2 = int(postG.split(",")[0])
                y2 = int(postG.split(",")[1])
                test.insertGoal(x2,y2)
            
            if line.startswith("r2d2"):
                name = "r2d2"
                postR = line.split(" ")[1]
                r1 = int(postR.split(",")[0])
                r2 = int(postR.split(",")[1])
                test.insertRobot(name,r1,r2)
                
        test.create_world()
        
    print()
    #test.where_is_robot()    
    
    stack = stackADT()
    find_path(test, stack, test.robotx1, test.roboty1, test.goalx1, test.goaly1)
    
#     while(test.goal_reached() == False):
# #         direction = input("Please insert direction to move (n/s/e/w): ")
#         x, y = input("Please insert x,y coordinates (e.g. 3,2):").split(",")
#         print()
#         #y = int(input("Please insert y coordinate to move to:"))
#         test.move_robot(int(x),int(y))
#         print()
#         test.where_is_robot()
    
if __name__ == "__main__":
    main()
    