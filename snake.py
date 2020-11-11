import pygame
import random
step = 40   #每格大小
screensize = [step * 20, step * 20]     #窗口大小
white = [255, 255, 255]
black = [0, 0, 0]
MOVE = 24
pygame.time.set_timer(MOVE, 200)        #移动定时器
forward = 'RIGHT'
screen = pygame.display.set_mode(screensize)    #初始窗口
snakes = [{'x': step * 5, 'y': step * 5},       #初始蛇
          {'x': step * 6, 'y': step * 5},
          {'x': step * 7, 'y': step * 5},
          {'x': step * 8, 'y': step * 5}]
def getFood():      #生成一个食物
    global food
    food = {'x': random.choice(range(step * 2, step * 18, step)),
            'y': random.choice(range(step * 2, step * 18, step))}
def newFood():      #吃掉、生成食物
    if snakes[-1]['x'] == food['x'] and snakes[-1]['y'] == food['y']:
        getFood()
        snakeAppend()
def draw():         #绘制
    screen.fill(black)
    for snake in snakes:
        pygame.draw.rect(screen, white, [snake['x'], snake['y'], step - 2, step - 2])
        if food['x'] == snake['x'] and food['y'] == snake['y']:
            getFood()       #新食物在蛇身重新生成
    pygame.draw.rect(screen, [255, 75, 75], [snakes[-1]['x'], snakes[-1]['y'], step - 2, step - 2])
    pygame.draw.rect(screen, [200, 150, 255], [food['x'], food['y'], step - 2, step - 2])
    pygame.display.update()
def snakeAppend():          #蛇变长
    global snakes
    if forward == 'RIGHT':
        snakes.append({'x': snakes[-1]['x'] + step, 'y': snakes[-1]['y']})
    elif forward == 'LEFT':
        snakes.append({'x': snakes[-1]['x'] - step, 'y': snakes[-1]['y']})
    elif forward == 'UP':
        snakes.append({'x': snakes[-1]['x'], 'y': snakes[-1]['y'] - step})
    elif forward == 'DOWN':
        snakes.append({'x': snakes[-1]['x'], 'y': snakes[-1]['y'] + step})
def move():                 #蛇移动
    global snakes
    if isAlive():
        snakes.remove(snakes[0])    #去尾
        snakeAppend()               #加头
def isAlive():              #蛇活着
    if step * 19 >= snakes[-1]['x'] > -step:
        if step * 19 >= snakes[-1]['y'] > -step:
            for i in range(0, len(snakes) - 2):
                if snakes[i]['x'] == snakes[-1]['x'] and snakes[i]['y'] == snakes[-1]['y']:
                    return False    #撞自己
            return True
def eventListen():          #监听
    global forward
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and forward != 'UP':
                forward = 'DOWN'
            elif event.key == pygame.K_UP and forward != 'DOWN':
                forward = 'UP'
            elif event.key == pygame.K_RIGHT and forward != 'LEFT':
                forward = 'RIGHT'
            elif event.key == pygame.K_LEFT and forward != 'RIGHT':
                forward = 'LEFT'
            elif event.key == pygame.K_SPACE:
                snakeAppend()
        elif event.type == MOVE:
            move()
getFood()
while True:
    eventListen()
    newFood()
    draw()
