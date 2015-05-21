from queue import *

class MickeyMove:
            
    '''
    Constructor with starting position x , y
                     the mouse moved path 
    ''' 
    def __init__(self, x_start, y_start):
        self.x_start = x_start
        self.y_start = y_start
        self.path = Queue(maxsize=0)
     
    @classmethod
    def checkMove(selft, x_nextPos, y_nextPos):
        return False

    
    @classmethod
    def move(self, x_move, y_move):








#maze =[
#        [2, 2, 2, 2, 2, 2, 2],
#        [2, 0, 0, 0, 0, 0, 2],
#        [2, 0, 2, 0, 2, 0, 2],
#        [2, 0, 0, 0, 0, 2, 2],
#        [2, 2, 0, 2, 0, 2, 2],
#        [2, 0, 0, 0, 0, 0, 2],
#        [2, 2, 2, 2, 2, 2, 2]]
#si = 1
#sj = 1
#ei = 5
#ej = 5


#print(maze)