from queue import *
from array import array



class MickeyMove(object):
    '''
    Constructor with starting position x , y
                     the mouse moved path 
    ''' 
    def __init__(self, map ,x_start, y_start):
        print("create mickey maze")
        self.x_start = x_start
        self.y_start = y_start
        self.path = Queue(maxsize=0)
        self.maze_map = map
     
    '''
    Return True if next move is available   
    ''' 
    @classmethod
    def checkMove(selft, x_nextPos, y_nextPos):
        return False

    '''
    
    '''
    @classmethod
    def move(self, x_move, y_move):
        return True
    
    @classmethod
    def printMaze(self):
        print("in maze")
        for row in self.maze_map:
            for val in row:
                print(val,end=" ")
            print(end="\n")    
        







maze =[
        [2, 2, 2, 2, 2, 2, 2],
        [2, 0, 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 2, 0, 2],
        [2, 0, 0, 0, 0, 2, 2],
        [2, 2, 0, 2, 0, 2, 2],
        [2, 0, 0, 0, 0, 0, 2],
        [2, 2, 2, 2, 2, 2, 2]]

m = MickeyMove(maze, 1,1)
#try to print maze by using method
m.printMaze()
for row in maze:
    for val in row:
        print(val,end=" ")
    print(end="\n")    

#si = 1
#sj = 1
#ei = 5
#ej = 5


#print(maze)