#Pledge Algorithm
#right-hand rule
from queue import *
from array import array
path = LifoQueue(maxsize = 0)
realpath ={}
recpath = {}
Counter = 0
class MickeyMove():
    def __init__(self, map,x_start , y_start):
        print("create mickey maze")
        self.x_start = x_start
        self.y_start = y_start
        self.path = Queue(maxsize=0)
        self.maze_map = map

    @classmethod
    def checkMove(self, x_nextmove, y_nextmove):
        maze = self.maze_map    
        if maze[x_nextmove+1][y_nextmove] == 0: #no obstacle on R
            right1 = [x_nextmove+1,y_nextmove]
            return right1
        elif maze[x_nextmove+1][y_nextmove] != 0 and maze[x_nextmove][y_nextmove+1] == 0: #obstacle on R, neither F 
            right2 = [x_nextmove,y_nextmove+1] 
            return right2
        elif maze[x_nextmove][y_nextmove+1] != 0 and maze[x_nextmove+1][y_nextmove] != 0: #obstacle on both R and F
            right3 = [x_nextmove-11,y_nextmove]
            return right3
    @classmethod
    def counter(self,direction):
        print(direction)
        global Counter
        if direction == 'right':
            if 'right' in realpath:
                Counter = Counter
            else:
                Counter = Counter
        elif direction == 'left':
            if 'left' in realpath:
                Counter = Counter
            else:
                Counter += 1
        elif direction == 'up':
            if 'up' in realpath:
                Counter = Counter
            else:
                Counter += 1
        elif direction == 'down':
            if 'down' in realpath:
                Counter = Counter
            else:
                Counter += 1
        print(Counter)
    @classmethod    
    def heading(self,nextM,Moved):
        directionX = nextM[0]-Moved[0]
        directionY = nextM[1]-Moved[1]
        if directionX == 0 and directionY > 0:
                realpath['right'] = nextM
                return 'right'
        elif directionX == 0 and directionY < 0:
                realpath['left'] = nextM
                return 'left'
        elif directionX > 0 and directionY == 0:
                realpath['down'] = nextM
                return 'down'
        elif directionX < 0 and directionY == 0:
                realpath['up'] = nextM
                return 'up'
    @classmethod
    def recDirection(self,nextM,Moved):
        directionX = nextM[0]-Moved[0]
        directionY = nextM[1]-Moved[1]
        if directionX == 0 and directionY > 0:
            realpath['right'] = 'right'
        elif directionX == 0 and directionY < 0:
            realpath['left'] = 'left'
        elif directionX > 0 and directionY == 0:
            realpath['down'] = 'down'
        elif directionX < 0 and direction[1] == 0:
            realpath['up']  = 'up'
    @classmethod
    def move(self,x_move,y_move):
        Moved = [x_move,y_move]
        Next_move = self.checkMove(x_move,y_move)
        self.recDirection(Next_move,Moved)
        heading = self.heading(Next_move,Moved)
        print("heading",heading,"next",Next_move)
        print(realpath)
        self.counter(heading)
        self.move(Next_move[0],Next_move[1])
    @classmethod
    def getMaze(self,val):
        self.maze_map = val


def main():
    maze =[ 
           [2, 2, 2, 2, 2, 2, 2],
           [2, 0, 0, 0, 0, 0, 2],
           [2, 0, 2, 0, 2, 0, 2],
           [2, 0, 0, 0, 0, 2, 2],
           [2, 2, 0, 2, 0, 2, 2],
           [2, 0, 0, 0, 0, 0, 0],
           [2, 2, 2, 2, 2, 2, 2]]
    m = MickeyMove(maze,1,1)
    m.getMaze(maze)
    m.move(1,1)
if __name__ == "__main__":
    Si = 1
    Sj = 1
    main()
