class Snake(): # 加上Object,可使用一些基本方法

    direction = {'up'   : 4, 'down' : 5, 
                 'left' : 6, 'right': 7} 
    def __init__(self):
        self.name = "snake_1"
        self.direction = Snake.direction["up"]
        self.head = (5,5)
        self.body = [self.head]
        self.length = 1 

    def eat_food(self):
        self.body.append(self.head)
        self.length += 1

    def move_snake(self):
        self.body.append(self.head)
        self.body.pop(0)

    def onwald(self):
        ''' control the snake '''
        if self.direction == Snake.direction['up']: 
            self.head = (self.head[0]-1,self.head[1])
        elif self.direction == Snake.direction['right']:
            self.head = (self.head[0],self.head[1]+1)
        elif self.direction == Snake.direction['down']:
            self.head = (self.head[0]+1,self.head[1])
        elif self.direction == Snake.direction['left']:
            self.head = (self.head[0],self.head[1]-1)
        else:
            pass
    def __len__(self):
        return self.length