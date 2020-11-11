# Pygame-简易贪吃蛇

新手学习Pygame制作属于自己的第一个贪吃蛇游戏

## 环境

使用 **python 3.7.7** 或更高版本，它对新手友好很多，并且运行速度更快

安装 **pygame** 的最好方法是使用 **pip** 工具（python用于安装软件包的工具）

我们使用`--user`标志告诉它安装到主目录中，而不是全局。

`python -m pip install -U pygame --user`

查看是否安装成功：

`python -m pygame.examples.aliens`

>安装过程引用修改自：[Pygame GettingStarted Wiki](https://www.pygame.org/wiki/GettingStarted)

## 基本思路

#### 1. 导入模块
```
import pygame
import random
```
#### 2. 初始化框架
- 设置每格大小以及窗口大小（宽/高20格）：
```
step = 40
screensize = [step * 20, step * 20]
```
- 初始化窗口
```
screen = pygame.display.set_mode(screensize)
```
- 定义常用颜色RGB
```
white = [255, 255, 255]     # 白色
black = [0, 0, 0]           # 黑色
```
- 设置蛇移动的定时器
```
MOVE = 24
pygame.time.set_timer(MOVE, 200)
``` 
```
forward = 'RIGHT'   # 前进方向保存在forword中，初始方向为右
```
- 初始化蛇
```
snakes = [{'x': step * 5, 'y': step * 5},
          {'x': step * 6, 'y': step * 5},
          {'x': step * 7, 'y': step * 5},
          {'x': step * 8, 'y': step * 5}]
```
> 每个方块左上角坐标保存在列表snakes中

> `snakes[0]` 为蛇尾 , `snakes[3]` 即 `snakes[-1]` 为蛇头
#### 3. 事件监听
```
def eventListen():
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
```
> 点击右上角 × 结束程序

> 按上下左右键，修改forword
#### 4. 绘制函数
```
def draw():
    screen.fill(black)    # 填充黑色背景
    for snake in snakes:  # 遍历蛇身
        pygame.draw.rect(screen, white, [snake['x'], snake['y'], step - 2, step - 2])
    pygame.draw.rect(screen, [255, 75, 75], [snakes[-1]['x'], snakes[-1]['y'], step - 2, step - 2])   # 蛇头颜色设置为 [255, 75, 75]
    pygame.display.update()
```
> 背景黑色，蛇身填充白色，填充长宽为 `step - 2, step - 2` (留下方块周围空白)，再次填充蛇头颜色为 [255, 75, 75]
#### 等待更新...
