import time,os,threading
import msvcrt # 用于监听键盘
from typing import Union # 复合类型注释，没用明白。
from map import Map
from snake import Snake
from polt import Polt
import sys
 
def game_over():
    '''结束游戏，打印游戏结束信息'''
    global switch
    switch = False
    print("Game Over")

def event_judge(snake:Snake,map:list)->any:
    ''' Collision detection '''
    col,row = snake.head
    if map[col][row] == 0:
        return 0 # 空地
    elif map[col][row] == 1:
        return 1 # 障碍物
    elif map[col][row] == 2:
        return 2 # 食物
    elif snake.head in snake.body[:-1]:
        return 3 # 蛇身
    else:
        return -1 # 其他情况
def clear_screen():
    sys.stdout.write("\033[0;0H") # 清屏
def listen_keyboard():
    '''监听键盘'''
    global direction_key
    global switch
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode()
            if key == "w":
                direction_key = 4
            elif key == "a":
                direction_key = 6
            elif key == "s":
                direction_key = 5
            elif key == "d":
                direction_key = 7
            elif key == "q":
                switch = False
                break
            else:
                pass

if __name__ == "__main__":

    map = Map(20,20)
    map.create_food(5) # 生成食物

    snake = Snake()
    
    global direction_key
    direction_key = 7 # 默认方向为上 4:up, 5:down, 6:left, 7:right
    
    # 暂时不考虑资源竞争问题
    t1 = threading.Thread(target=listen_keyboard)
    t1.start()

    events = {"move":0, "crash_walk":1, "eat_food":2, "crash_body":3}
    global switch 
    switch = True
     # 速度为1.3s/蛇身长

    Polt.clear_screen()

    while switch:
        speed = 20/(snake.length + 20) 

        snake.direction = direction_key
        snake.onwald()
    
        event =  event_judge(snake,map.walk)

        if event == events["move"]:
            snake.move_snake()
        elif event == events["crash_walk"]:
            game_over()
        elif event == events["eat_food"]:
            snake.eat_food()
            map.create_food(1)
            map.delet_food(snake.head)
        elif event == events["crash_body"]:
            game_over()
        else:
            pass

        Polt.set_cursor_top()  
        plt = Polt(map.col,map.row)
        map_ = plt.map_snake_union(map.walk,snake)
        sys.stdout.write("speed: %.2f step/s\n" % float(1/speed))
                
        time.sleep(speed)

    t1.join()
        
        