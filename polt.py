from copy import deepcopy
import sys
from snake import Snake # 怎么自定义类的类型提示？

UP = "\033[32m{}\033[0m".format(" ▲")
DOWN = "\033[32m{}\033[0m".format(" ▼")
LEFT = "\033[32m{}\033[0m".format("◀ ")
RIGHT = "\033[32m{}\033[0m".format(" ▶")
BODY = "\033[36m{}\033[0m".format(" ◕")
WALK = "\033[33m{}\033[0m".format(" &")
FOOD = "\033[31m{}\033[0m".format(" *")

class Polt(object):

    events = {"air":0, 
              "walk":1, 
              "food":2, 
              "snake_body":3,
              "snake_head_up":4,
              "snake_head_down":5,
              "snake_head_left":6,
              "snake_head_right":7}
    
    lump = {"air" : "  ",
            "walk" : WALK,
            "food" : FOOD,
            "snake_body" : BODY,
            "snake_head_up" : UP,
            "snake_head_down" : DOWN,
            "snake_head_left" : LEFT,
            "snake_head_right" : RIGHT}
    
    def __init__(self,col:int,row:int):
        self.lenght = col
        self.width = row
    def plot_ui(self,map:list, head:tuple, direction:int, lenght:int)->None:

        '''
        polt the ui
        
        Args:
            map: 2-dimensional list
        '''

        string  = ""
        for i in range(self.lenght):
            for j in range(self.width):
                if map[i][j] == Polt.events["air"]: 
                    string  += Polt.lump['air']
                elif map[i][j] == Polt.events["walk"]:
                    string  += Polt.lump['walk']
                elif map[i][j] == Polt.events["food"]:
                    string  += Polt.lump["food"]
                elif map[i][j] == Polt.events["snake_body"]:
                    string  += Polt.lump["snake_body"]
                elif map[i][j] == Polt.events["snake_head_up"]:
                    string  += Polt.lump["snake_head_up"]
                elif map[i][j] == Polt.events["snake_head_down"]:
                    string  += Polt.lump["snake_head_down"]
                elif map[i][j] == Polt.events["snake_head_left"]:
                    string  += Polt.lump["snake_head_left"]
                elif map[i][j] == Polt.events["snake_head_right"]:
                    string  += Polt.lump["snake_head_right"]
                else:
                    pass
            string  += "\n"
        string  += "snake head: {}                      \n".format(head)
        string  += "snake direction: {}                 \n".format(direction)
        string  += "snake body length: {}               \n".format(lenght)
        sys.stdout.write(string )

    def map_snake_union(self,map:list,snake:Snake)->None:
        '''
        plot the snake on the map

        Args:
            map: 2-dimensional list                 |list[list[int]]
            snake: Snake object                     |Snake
        '''
        _map = deepcopy(map)
        for lump in snake.body:
            _map[lump[0]][lump[1]] = Polt.events["snake_body"] # 蛇身
        _map[snake.head[0]][snake.head[1]] = snake.direction 

        self.plot_ui(_map, snake.head, snake.direction, snake.length)

    def clear_screen():
      '''命令行清屏'''
      sys.stdout.write("cls")

    def set_cursor_top():
        '''光标置顶,左上角'''
        sys.stdout.write("\033[0;0H") 
