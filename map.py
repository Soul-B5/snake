from random import randint

class Map():
    
    def __init__(self,col:int,row:int):
        ''' 
        Args:
            col: map length
            row: map width
        '''
        self.col = col
        self.row = row
        self.walk = [[0 for i in range(self.col)] for j in range(self.row)]
        self.create_map()
        
    def create_map(self):
        for i in range(self.col):
            for j in range(self.row):
                t = 1 if i == 0 or i == self.col-1 or j == self.row-1 or j == 0 else 0 # 边界为1
                self.walk[i][j] = t

    def create_food(self,num:int = 1)->None:
        for _ in range(num):
            self.walk[randint(1,self.col-2)][randint(1,self.row-2)] = 2 # 2:food

    def delet_food(self,coord:tuple)->None:
        '''
        Args:
            head: 2-dimensional coordinates
        '''
        i , j = coord
        self.walk[i][j] = 0    
