from bangtal import *
import threading, random

# Game Settings
setGameOption(GameOption.ROOM_TITLE, False)
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)
# Scenes
inGame = Scene('inGame','images/bgday.jpg')    #1280 x 720

Startmygame = Scene('Startmygame', 'images/bgday.jpg')

menu = Scene('menu','images/bgday.jpg')    #1280 x 720
menuline = Object('images/menuline.png')
menuline.locate(menu,0,0)
menuline.show()
menu.setLight(0.85)

gameClear = Scene('gameClear','images/gameclear.jpg')
gameClear.setLight(0.85)

gameOver = Scene('gameOver','images/gameover.jpg')
gameOver.setLight(0.85)

# Classes
class Current():
    isGameRunning = False

    mapsize = 11
    playerX = 600       # 실제 scene 좌표
    playerY = 300
    mapX = 0            # 상대적 map 좌표
    mapY = 0

    bossHP = 80
    bossday = 7

    bX = 512
    bY = 260
    boardX = 5          #시야범위 width(홀수)
    boardY = 3          #시야범위 height(홀수)

    LR = 1              # 1:Right  2:Left
    playerMoving = False
    direction = 0        # current moving direction

    hp = 5
    xp = 0
    level = 1
    sky = 1             # 1:Sun  2:Moon
    light = 0.6
    day = 1
    turn = 0
    turnMax = 20        # turns in one day

    max_fruit = 8
    num_fruit = [0, 0, 0, 0]
    max_animal = 4
    num_animal = [0, 0, 0, 0]

    apple = 0
    banana = 0
    coconut = 0
    orange = 0
    crocodile = 0
    turtle = 0
    snake = 0
    monkey = 0

class Fruits():
    coconut = 10
    apple = 10
    orange = 10
    banana = 10

    def AppleUp(amount):
        Current.apple += int(amount)
        Fruits.showmenuApple()

    def showmenuApple():
        APPLE = Current.apple
        if APPLE<10:
            Apple100.setImage(setNumImage(0))
            Apple10.setImage(setNumImage(0))
            Apple1.setImage(setNumImage(APPLE))
        elif APPLE<100:
            Apple100.setImage(setNumImage(0))
            Apple10.setImage(setNumImage(APPLE//10))
            Apple1.setImage(setNumImage(APPLE%10))
        else:
            x = APPLE-(APPLE//100*100)
            Apple100.setImage(setNumImage(APPLE//100))
            Apple10.setImage(setNumImage(x//10))
            Apple1.setImage(setNumImage(x%10))
        Apple1.show()
        Apple10.show()
        Apple100.show()

    def BananaUp(amount):
        Current.banana += int(amount)
        Fruits.showmenuBanana()

    def showmenuBanana():
        BANANA = Current.banana
        if BANANA<10:
            Banana100.setImage(setNumImage(0))
            Banana10.setImage(setNumImage(0))
            Banana1.setImage(setNumImage(BANANA))
        elif BANANA<100:
            Banana100.setImage(setNumImage(0))
            Banana10.setImage(setNumImage(BANANA//10))
            Banana1.setImage(setNumImage(BANANA%10))
        else:
            x = BANANA-(BANANA//100*100)
            Banana100.setImage(setNumImage(BANANA//100))
            Banana10.setImage(setNumImage(x//10))
            Banana1.setImage(setNumImage(x%10))
        Banana1.show()
        Banana10.show()
        Banana100.show()

    def OrangeUp(amount):
        Current.orange += int(amount)
        Fruits.showmenuOrange()

    def showmenuOrange():
        ORANGE = Current.orange
        if ORANGE<10:
            Orange100.setImage(setNumImage(0))
            Orange10.setImage(setNumImage(0))
            Orange1.setImage(setNumImage(ORANGE))
        elif ORANGE<100:
            Orange100.setImage(setNumImage(0))
            Orange10.setImage(setNumImage(ORANGE//10))
            Orange1.setImage(setNumImage(ORANGE%10))
        else:
            x = ORANGE-(ORANGE//100*100)
            Orange100.setImage(setNumImage(ORANGE//100))
            Orange10.setImage(setNumImage(x//10))
            Orange1.setImage(setNumImage(x%10))
        Orange1.show()
        Orange10.show()
        Orange100.show()

    def CoconutUp(amount):
        Current.coconut += int(amount)
        Fruits.showmenuCoconut()

    def showmenuCoconut():
        COCONUT = Current.coconut
        if COCONUT<10:
            Coconut100.setImage(setNumImage(0))
            Coconut10.setImage(setNumImage(0))
            Coconut1.setImage(setNumImage(COCONUT))
        elif COCONUT<100:
            Coconut100.setImage(setNumImage(0))
            Coconut10.setImage(setNumImage(COCONUT//10))
            Coconut1.setImage(setNumImage(COCONUT%10))
        else:
            x = COCONUT-(COCONUT//100*100)
            Coconut100.setImage(setNumImage(COCONUT//100))
            Coconut10.setImage(setNumImage(x//10))
            Coconut1.setImage(setNumImage(x%10))
        Coconut1.show()
        Coconut10.show()
        Coconut100.show()

class Animals():
    lion_atk = 3

    turtle_hp = 1
    turtle_atk = 0
    turtle_xp = 15

    snake_hp = 3
    snake_atk = 1
    snake_xp = 20
    
    monkey_hp = 5
    monkey_atk = 1
    monkey_xp = 25
    
    crocodile_hp = 7
    crocodile_atk = 2
    crocodile_xp = 30

    def turtleUp(amount):
        Current.turtle += int(amount)
        Animals.showmenuturtle()

    def showmenuturtle():
        TURTLE = Current.turtle
        if TURTLE<10:
            turtle100.setImage(setNumImage(0))
            turtle10.setImage(setNumImage(0))
            turtle1.setImage(setNumImage(TURTLE))
        elif TURTLE<100:
            turtle100.setImage(setNumImage(0))
            turtle10.setImage(setNumImage(TURTLE//10))
            turtle1.setImage(setNumImage(TURTLE%10))
        else:
            x = TURTLE-(TURTLE//100*100)
            turtle100.setImage(setNumImage(TURTLE//100))
            turtle10.setImage(setNumImage(x//10))
            turtle1.setImage(setNumImage(x%10))
        turtle1.show()
        turtle10.show()
        turtle100.show()

    def snakeUp(amount):
        Current.snake += int(amount)
        Animals.showmenusnake()

    def showmenusnake():
        SNAKE = Current.snake
        if SNAKE<10:
            snake100.setImage(setNumImage(0))
            snake10.setImage(setNumImage(0))
            snake1.setImage(setNumImage(SNAKE))
        elif SNAKE<100:
            snake100.setImage(setNumImage(0))
            snake10.setImage(setNumImage(SNAKE//10))
            snake1.setImage(setNumImage(SNAKE%10))
        else:
            x = SNAKE-(SNAKE//100*100)
            snake100.setImage(setNumImage(SNAKE//100))
            snake10.setImage(setNumImage(x//10))
            snake1.setImage(setNumImage(x%10))
        snake1.show()
        snake10.show()
        snake100.show()
        
    def monkeyUp(amount):
        Current.monkey += int(amount)
        Animals.showmenumonkey()

    def showmenumonkey():
        MONKEY = Current.monkey
        if MONKEY<10:
            monkey100.setImage(setNumImage(0))
            monkey10.setImage(setNumImage(0))
            monkey1.setImage(setNumImage(MONKEY))
        elif MONKEY<100:
            monkey100.setImage(setNumImage(0))
            monkey10.setImage(setNumImage(MONKEY//10))
            monkey1.setImage(setNumImage(MONKEY%10))
        else:
            x = MONKEY-(MONKEY//100*100)
            monkey100.setImage(setNumImage(MONKEY//100))
            monkey10.setImage(setNumImage(x//10))
            monkey1.setImage(setNumImage(x%10))
        monkey1.show()
        monkey10.show()
        monkey100.show()

    def crocodileUp(amount):
        Current.crocodile += int(amount)
        Animals.showmenucrocodile()

    def showmenucrocodile():
        CROCODILE = Current.crocodile
        if CROCODILE<10:
            crocodile100.setImage(setNumImage(0))
            crocodile10.setImage(setNumImage(0))
            crocodile1.setImage(setNumImage(CROCODILE))
        elif CROCODILE<100:
            crocodile100.setImage(setNumImage(0))
            crocodile10.setImage(setNumImage(CROCODILE//10))
            crocodile1.setImage(setNumImage(MCROCODILE%10))
        else:
            x = CROCODILE-(CROCODILE//100*100)
            crocodile100.setImage(setNumImage(CROCODILE//100))
            crocodile10.setImage(setNumImage(x//10))
            crocodile1.setImage(setNumImage(x%10))
        crocodile1.show()
        crocodile10.show()
        crocodile100.show()

class Wall():
    Up = False
    Down = False
    Left = False
    Right = False

# All Objects
class GameObject(Object):
    def __init__(self, image, scene = None, x = 0, y = 0, scale = 1, shown = True):
        super().__init__(image)
        if scene is not None:
            self.locate(scene, x, y)
            self.setScale(scale)
            if shown:
                self.show()

player = GameObject('images/player/playerR0.png', inGame, Current.playerX, Current.playerY, 0.235, True)

menuplayer = GameObject('images/player/playerR0.png', menu, 130, 40, 0.7, True)

title = GameObject('images/title.png', Startmygame, 25, 50, 0.5, True)
startplayer = GameObject('images/player/playerR0.png', Startmygame, 780, 40, 0.7, True)
startbutton = GameObject('images/startgame.jpg', Startmygame, 940, 520, 0.3, True)

weather = GameObject('images/weathers/sun.png', menu, 730, 560, 0.25, True)

DAY = GameObject('images/day.png', menu, 520, 625, 0.15, True)
Days10 = GameObject('images/numbers/0.png', menu, 650, 625, 0.15, True)
Days1 = GameObject('images/numbers/1.png', menu, 680, 625, 0.15, True)

Applemenu = GameObject('images/contents/apple.png', menu, 530, 425, 0.15, True)
Apple100 = GameObject('images/numbers/0.png', menu, 670, 428, 0.15, True)
Apple10 = GameObject('images/numbers/0.png', menu, 710, 428, 0.15, True)
Apple1 = GameObject('images/numbers/0.png', menu, 750, 428, 0.15, True)

Orangemenu = GameObject('images/contents/orange.png', menu, 530, 325, 0.15, True)
Orange100 = GameObject('images/numbers/0.png', menu, 670, 328, 0.15, True)
Orange10 = GameObject('images/numbers/0.png', menu, 710, 328, 0.15, True)
Orange1 = GameObject('images/numbers/0.png', menu, 750, 328, 0.15, True)

Coconutmenu = GameObject('images/contents/coconut.png', menu, 530, 225, 0.15, True)
Coconut100 = GameObject('images/numbers/0.png', menu, 670, 228, 0.15, True)
Coconut10 = GameObject('images/numbers/0.png', menu, 710, 228, 0.15, True)
Coconut1 = GameObject('images/numbers/0.png', menu, 750, 228, 0.15, True)

Bananamenu = GameObject('images/contents/banana.png', menu, 530, 125, 0.15, True)
Banana100 = GameObject('images/numbers/0.png', menu, 670, 128, 0.15, True)
Banana10 = GameObject('images/numbers/0.png', menu, 710, 128, 0.15, True)
Banana1 = GameObject('images/numbers/0.png', menu, 750, 128, 0.15, True)

crocodilemenu = GameObject('images/contents/crocodile.png', menu, 825, 130, 0.35, True)
crocodile100 = GameObject('images/numbers/0.png', menu, 1010, 128, 0.15, True)
crocodile10 = GameObject('images/numbers/0.png', menu, 1050, 128, 0.15, True)
crocodile1 = GameObject('images/numbers/0.png', menu, 1090, 128, 0.15, True)

snakemenu = GameObject('images/contents/snake.png', menu, 860, 330, 0.12, True)
snake100 = GameObject('images/numbers/0.png', menu, 1010, 328, 0.15, True)
snake10 = GameObject('images/numbers/0.png', menu, 1050, 328, 0.15, True)
snake1 = GameObject('images/numbers/0.png', menu, 1090, 328, 0.15, True)

monkeymenu = GameObject('images/contents/monkey.png', menu, 865, 220, 0.17, True)
monkey100 = GameObject('images/numbers/0.png', menu, 1010, 228, 0.15, True)
monkey10 = GameObject('images/numbers/0.png', menu, 1050, 228, 0.15, True)
monkey1 = GameObject('images/numbers/0.png', menu, 1090, 228, 0.15, True)

turtlemenu = GameObject('images/contents/turtle.png', menu, 860, 425, 0.15, True)
turtle100 = GameObject('images/numbers/0.png', menu, 1010, 428, 0.15, True)
turtle10 = GameObject('images/numbers/0.png', menu, 1050, 428, 0.15, True)
turtle1 = GameObject('images/numbers/0.png', menu, 1090, 428, 0.15, True)

multi = GameObject('images/numbers/multi.png', menu, 610, 428, 0.1, True)
multi = GameObject('images/numbers/multi.png', menu, 610, 328, 0.1, True)
multi = GameObject('images/numbers/multi.png', menu, 610, 228, 0.1, True)
multi = GameObject('images/numbers/multi.png', menu, 610, 128, 0.1, True)
multi = GameObject('images/numbers/multi.png', menu, 950, 428, 0.1, True)
multi = GameObject('images/numbers/multi.png', menu, 950, 328, 0.1, True)
multi = GameObject('images/numbers/multi.png', menu, 950, 228, 0.1, True)
multi = GameObject('images/numbers/multi.png', menu, 950, 128, 0.1, True)

TURN = GameObject('images/turn.png', menu, 520, 565, 0.15, True)
turns10 = GameObject('images/numbers/0.png', menu, 650, 565, 0.15, True)
turns1 = GameObject('images/numbers/1.png', menu, 680, 565, 0.15, True)

LEVEL = GameObject('images/sword.png', inGame, 560, 670, 0.11, True)
level10 = GameObject(   'images/numbers/0.png', inGame, 610, 680, 0.12, True)
level1 = GameObject('images/numbers/1.png', inGame, 640, 680, 0.12, True)

menuLEVEL = GameObject('images/level.png', menu, 900, 625, 0.13, True)
menulevel10 = GameObject('images/numbers/0.png', menu, 1030, 625, 0.14, True)
menulevel1 = GameObject('images/numbers/1.png', menu, 1060, 625, 0.14, True)

HP = GameObject('images/hearts/3.png', inGame, 270, 670, 0.1, True)
menuHP = GameObject('images/hearts/3.png', menu, 40, 630, 0.12, True)

menuXP = GameObject('images/xp.png', menu, 900, 565, 0.09, True)
menuxp100 = GameObject('images/numbers/0.png', menu, 1000, 565, 0.13, True)
menuxp10 = GameObject('images/numbers/0.png', menu, 1030, 565, 0.13, True)
menuxp1 = GameObject('images/numbers/0.png', menu, 1060, 565, 0.13, True)

XP = GameObject('images/xp.png', inGame, 710, 680, 0.09, True)
xp100 = GameObject('images/numbers/0.png', inGame, 770, 680, 0.12, True)
xp10 = GameObject('images/numbers/0.png', inGame, 800, 680, 0.12, True)
xp1 = GameObject('images/numbers/0.png', inGame, 830, 680, 0.12, True)

bossHP = GameObject('images/hearts/boss.png', inGame, 1140, 675, 0.1, False)
bosshp10 = GameObject('images/numbers/0.png', inGame, 1200, 675, 0.12, False)
bosshp1 = GameObject('images/numbers/0.png', inGame, 1230, 675, 0.12, False)

# Block Controls

class Const():
    INIT_PLAYER_X = Current.bX
    INIT_PLAYER_Y = Current.bY
    BLOCK_NUM = 4
    BLOCK_SIZE = 256
    ANIMATION_FRAME = 8     # 이동 애니메이션 총 프레임수

class Block(Object):
    def __init__(self, num, x, y):
        super().__init__("images/blocks/block"+str(num)+".png")
        self.num = num
        self.setScale(Const.BLOCK_SIZE/384)      
        self.locate_on_board(x, y)
        self.show()
    def locate_on_board(self, bx, by):
        self.x = bx
        self.y = by
        tx = int(Const.INIT_PLAYER_X + Const.BLOCK_SIZE * (bx-(Current.boardX//2)))
        ty = int(Const.INIT_PLAYER_Y + Const.BLOCK_SIZE * (by-(Current.boardY//2)))
        self.locate(inGame, tx, ty)
    def moveAnimation(self, direction, frame):        
        #if direction == RIGHT        
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        self.x += dx[direction]/Const.ANIMATION_FRAME
        self.y += dy[direction]/Const.ANIMATION_FRAME
        if frame == Const.ANIMATION_FRAME:
            self.x = round(self.x)
            self.y = round(self.y)
        self.locate_on_board(self.x, self.y)       
    def setImageNum(self, num):
        self.num = num
        self.setImage("images/blocks/block"+str(num)+".png")
    def clearBlock(self):
        self.setImageNum(self.num//10*10)

class BlockBoard():
    def __init__(self, width, height):
        self.board = []
        self.spareBoard = []
        self.width = width
        self.height = height
        self.frame = 1
        self.slist = []
        self.init_slist()

        for i in range(height):
            tl = []
            for j in range(width):
                tl.append(i*width + j)
            self.board.append(tl)       
        m = max(width, height)
        for i in range(width*height, width*height+m):
            self.spareBoard.append(i)        

    def init_slist(self):        
        tlist = []
        for i in range(self.height):
            tlist.append([i, -1])
        self.slist.append(tlist)
        tlist = []
        for i in range(self.height):
            tlist.append([i, self.width])
        self.slist.append(tlist)
        tlist = []
        for i in range(self.width):
            tlist.append([self.height, i])
        self.slist.append(tlist)
        tlist = []
        for i in range(self.width):
            tlist.append([-1, i])
        self.slist.append(tlist)

    def locate_spare(self, direction):
        # if direction == RIGHT              
        for i in range(len(self.slist[direction])):
            tblock = blocks[self.spareBoard[i]]
            tx = self.slist[direction][i][1]
            ty = self.slist[direction][i][0]
            tblock.setImageNum(mapContents(Current.mapX + tx - (self.width//2), Current.mapY + ty - (self.height//2)))
            tblock.locate_on_board(tx, ty)
            tblock.show()

    def update_board(self, direction):        
        #if direction == RIGHT
        tempSpare = []
        
        if direction == 0:
            for i in range(self.height):
                tempSpare.append(self.board[i][self.width-1])
            for i in range(self.width-1, -1, -1):
                for j in range(self.height):
                    if i==0:
                        self.board[j][i] = self.spareBoard[j]
                    else:
                        self.board[j][i] = self.board[j][i-1]
            for i in range(self.height):
                self.spareBoard.pop(0)
                self.spareBoard.append(tempSpare[i])
                blocks[tempSpare[i]].hide()
        
        elif direction == 1:            
            for i in range(self.height):                
                tempSpare.append(self.board[i][0])            
            for i in range(self.width):
                for j in range(self.height):
                    if i==(self.width-1):
                        self.board[j][i] = self.spareBoard[j]
                    else:
                        self.board[j][i] = self.board[j][i+1]
            for i in range(self.height):
                self.spareBoard.pop(0)
                self.spareBoard.append(tempSpare[i])
                blocks[tempSpare[i]].hide()

        elif direction == 2:
            for i in range(self.width):
                tempSpare.append(self.board[0][i])
            for i in range(self.height):
                for j in range(self.width):
                    if i==(self.height-1):
                        self.board[i][j] = self.spareBoard[j]
                    else:
                        self.board[i][j] = self.board[i+1][j]
            for i in range(self.width):
                self.spareBoard.pop(0)
                self.spareBoard.append(tempSpare[i])
                blocks[tempSpare[i]].hide()

        elif direction == 3:            
            for i in range(self.width):
                tempSpare.append(self.board[self.height-1][i])            
            for i in range(self.height-1, -1, -1):
                for j in range(self.width):
                    if i==0:
                        self.board[i][j] = self.spareBoard[j]
                    else:
                        self.board[i][j] = self.board[i-1][j]
            for i in range(self.width):
                self.spareBoard.pop(0)
                self.spareBoard.append(tempSpare[i])
                blocks[tempSpare[i]].hide()

    def boardAnimation(self, direction):
        minimum = min(self.width, self.height)
        maximum = max(self.width, self.height)
        for i in range((minimum+1)*maximum):
            blocks[i].moveAnimation(direction, self.frame)
        self.frame = self.frame % Const.ANIMATION_FRAME + 1
        if self.frame == 1:            
            self.update_board(direction)
            onWhichBlock()
            return

    def move(self,direction):
        self.locate_spare(direction)
        self.boardAnimation(direction)

    def currentBoard(self):
        for i in range(2, -1, -1):
            print(self.board[i])

    def coordFromPlayer(self, x, y):
        return [x - Current.mapX - 5, y - Current.mapY - 5]

    # x, y : board coordinate (0~9), only if it is already in sight range
    def setImage(self, x, y, num):
        cP = self.coordFromPlayer(x, y)
        # change to board's coordinate
        bP = [cP[0]+Current.boardX//2, cP[1]+Current.boardY//2]
        print("block board's coordinate")
        print(bP)
        
        if bP[0] >= 0 and bP[0] < Current.boardX and bP[1] >= 0 and bP[1] < Current.boardY:
            self.currentBoard()
            blockNum = self.board[bP[1]][bP[0]]
            print(blockNum)
            blocks[blockNum].setImageNum(num)


# Map Controls
MapSizeX = Current.mapsize
MapSizeY = Current.mapsize

Contents = []
MapBlocks = []

def areaNum(x, y):
    if x>(MapSizeX+1)//2 and y>=(MapSizeY+1)//2:
        return 1
    elif x<=(MapSizeX+1)//2 and y>(MapSizeY+1)//2:
        return 2
    elif x<(MapSizeX+1)//2 and y<=(MapSizeY+1)//2:
        return 3
    elif x>=(MapSizeX+1)//2 and y<(MapSizeY+1)//2:
        return 4
    return 0 # Not in area

# return [[xmin, xmax], [ymin, ymax]]
def areaMinMax(num):
    if num == 1:
        return [ [(MapSizeX+3)//2, MapSizeX], [(MapSizeY+1)//2, MapSizeY] ]
    elif num == 2:
        return [[0, (MapSizeX+1)//2], [(MapSizeY+3)//2, MapSizeY] ]
    elif num == 3:
        return [[0, (MapSizeX-1)//2], [0, (MapSizeY+1)//2]]
    elif num == 4:
        print([[(MapSizeX+1)//2, MapSizeX], [0, (MapSizeY-1)//2]])
        return [[(MapSizeX+1)//2, MapSizeX], [0, (MapSizeY-1)//2]]

# num번 area가 [max_fruit]개의 과일을 가지게 채움.
def fillFruit(num):
    r = areaMinMax(num)
    while(Current.num_fruit[num-1] < Current.max_fruit):
        rx = random.randint(r[0][0], r[0][1])
        ry = random.randint(r[1][0], r[1][1])
        if(Contents[ry][rx] % 10 == 0): #if empty
            Contents[ry][rx] += 1
            Current.num_fruit[num-1] += 1

def fillAnimal(num):
    r = areaMinMax(num)
    while(Current.num_animal[num-1] < Current.max_animal):
        rx = random.randint(r[0][0], r[0][1])
        ry = random.randint(r[1][0], r[1][1])
        if(Contents[ry][rx] % 10 == 0): #if empty
            Contents[ry][rx] += 2
            Current.num_animal[num-1] += 1

def checkRespawn():
    if Current.sky ==1:
        if Current.mapX == 3:
            fillFruit(2)
            fillFruit(3)
            fillAnimal(2)
            fillAnimal(3)
        elif Current.mapX == -3:
            fillFruit(1)
            fillFruit(4)
            fillAnimal(1)
            fillAnimal(4)
        if Current.mapY == 2:
            fillFruit(3)
            fillFruit(4)
            fillAnimal(3)
            fillAnimal(4)
        elif Current.mapY == -2:
            fillFruit(1)
            fillFruit(2)
            fillAnimal(1)
            fillAnimal(2)


for y in range(MapSizeY+2):
    Contents.append([])
    for x in range(MapSizeX+2):
        if (x in [0, MapSizeX+1]) or (y in [0, MapSizeY+1]):
            Contents[y].append(-1)
        elif x==((MapSizeX+1)//2) and y==((MapSizeY+1)//2):
            Contents[y].append(30)
        else : Contents[y].append(areaNum(x,y)*10)

for i in range(4):
    fillFruit(i+1)
    fillAnimal(i+1)

def mapContents(x, y):
    global MapSizeX
    global MapSizeY
    X = int(x + 1+(MapSizeX-1)/2)
    Y = int(y + 1+(MapSizeY-1)/2)
    #print("x, y : %d, %d -> X, Y : %d, %d"%(x, y, X, Y))
    if (0 <= X <= (MapSizeX+1)) and (0 <= Y <= (MapSizeY+1)):
        return Contents[Y][X]
    #print("X, Y is over map : %d %d, so using block0 image"%(X, Y))
    return 0

def showmap2():
    for x in range(Current.mapsize+1, -1, -1):
        print(Contents[x])
showmap2()

# 30 blocks[y][x] (5x5 blocks + 5 spare blocks)
blocks = []
m1 = max(Current.boardX, Current.boardY)
m2 = min(Current.boardX, Current.boardY)
for i in range((m2+1)*m1):    
    blocks.append(Block(0, i%Current.boardX, i//Current.boardX))
    blocks[i].setImageNum(mapContents((i%Current.boardX) - (Current.boardX//2), (i//Current.boardX) - (Current.boardY//2)))
    if i >= (Current.boardX*Current.boardY):
        blocks[i].hide()

# BlockBoard and slist
blockBoard = BlockBoard(Current.boardX, Current.boardY)

# Fruits and Mobs
def isSomething(x,y):
    global Contents
    global blocks
    blocknum = int(Contents[y][x])
    if blocknum in [11,21,31,41]:           # 과일
        blocks[blockBoard.board[Current.boardY//2][Current.boardX//2]].clearBlock()
        Contents[y][x] = blocknum//10*10
        if blocknum == 11:            
            xpUp(Fruits.coconut)
            Fruits.CoconutUp(1)
            Current.num_fruit[0] -= 1
        elif blocknum == 21:
            xpUp(Fruits.orange)
            Fruits.OrangeUp(1)
            Current.num_fruit[1] -= 1
        elif blocknum == 31:
            xpUp(Fruits.apple)
            Fruits.AppleUp(1)
            Current.num_fruit[2] -= 1
        elif blocknum == 41:
            xpUp(Fruits.banana)
            Fruits.BananaUp(1)
            Current.num_fruit[3] -= 1
        Sound.play(Sound('sounds/bite.mp3'))

    elif blocknum in [12,22,32,42]:
        if blocknum == 12:                    # 거북이
            blocks[blockBoard.board[Current.boardY//2][Current.boardX//2]].clearBlock()
            Contents[y][x] = 10
            xpUp(Animals.turtle_xp)
            changeHP(-1*Animals.turtle_atk)
            Animals.turtleUp(1)
            Current.num_animal[0] -= 1

        elif blocknum == 22:                    # 뱀
            blocks[blockBoard.board[Current.boardY//2][Current.boardX//2]].clearBlock()
            Contents[y][x] = 20
            xpUp(Animals.snake_xp)
            changeHP(-1*Animals.snake_atk)
            Animals.snakeUp(1)
            Current.num_animal[1] -= 1

        elif blocknum == 32:                    # 악어
            blocks[blockBoard.board[Current.boardY//2][Current.boardX//2]].clearBlock()
            Contents[y][x] = 40
            xpUp(Animals.crocodile_xp)
            changeHP(-1*Animals.crocodile_atk)
            Animals.crocodileUp(1)
            Current.num_animal[2] -= 1

        elif blocknum == 42:                    # 원숭이
            blocks[blockBoard.board[Current.boardY//2][Current.boardX//2]].clearBlock()
            Contents[y][x] = 40
            xpUp(Animals.monkey_xp)
            changeHP(-1*Animals.monkey_atk)
            Animals.monkeyUp(1)
            Current.num_animal[3] -= 1

        Sound.play(Sound('sounds/hit.mp3'))
    
    elif blocknum == 100:                    # 사자 보스
        Sound.play(Sound('sounds/hit.mp3'))
        Current.bossHP -= Current.level
        changeHP(-1*Animals.lion_atk)
        showBossHP()
        
    checkGameOver()
    print(blocknum)

def isTurtleNearby(Up, Down, Left, Right):
    if Up==12:
       if Current.level<Animals.turtle_hp:
           Wall.Up = True
    if Down==12:
       if Current.level<Animals.turtle_hp:
           Wall.Down = True
    if Left==12:
       if Current.level<Animals.turtle_hp:
           Wall.Left = True
    if Right==12:
       if Current.level<Animals.turtle_hp:
           Wall.Right = True

def isSnakeNearby(Up, Down, Left, Right):
    if Up==22:
       if Current.level<Animals.snake_hp:
           Wall.Up = True
    if Down==22:
       if Current.level<Animals.snake_hp:
           Wall.Down = True
    if Left==22:
       if Current.level<Animals.snake_hp:
           Wall.Left = True
    if Right==22:
       if Current.level<Animals.snake_hp:
           Wall.Right = True

def isCrocodileNearby(Up, Down, Left, Right):
    if Up==32:
       if Current.level<Animals.crocodile_hp:
           Wall.Up = True
    if Down==32:
       if Current.level<Animals.crocodile_hp:
           Wall.Down = True
    if Left==32:
       if Current.level<Animals.crocodile_hp:
           Wall.Left = True
    if Right==32:
       if Current.level<Animals.crocodile_hp:
           Wall.Right = True

def isMonkeyNearby(Up, Down, Left, Right):
    if Up==42:
       if Current.level<Animals.monkey_hp:
           Wall.Up = True
    if Down==42:
       if Current.level<Animals.monkey_hp:
           Wall.Down = True
    if Left==42:
       if Current.level<Animals.monkey_hp:
           Wall.Left = True
    if Right==42:
       if Current.level<Animals.monkey_hp:
           Wall.Right = True

def isSomethingNearby(x,y):
    global Contents
    global blocks
    Up = int(Contents[y+1][x])
    Down = int(Contents[y-1][x])
    Left = int(Contents[y][x-1])
    Right = int(Contents[y][x+1])
    print(Up, Down, Left, Right)

    Wall.Up = Wall.Down = Wall.Left = Wall.Right = False
    
    if Up==-1: Wall.Up = True
    if Down==-1: Wall.Down = True
    if Left==-1: Wall.Left = True
    if Right==-1: Wall.Right = True
    
    isTurtleNearby(Up, Down, Left, Right)
    isSnakeNearby(Up, Down, Left, Right)
    isCrocodileNearby(Up, Down, Left, Right)
    isMonkeyNearby(Up, Down, Left, Right)
isSomethingNearby(int((Current.mapsize+1)/2 + Current.mapX), int((Current.mapsize+1)/2 + Current.mapY))

def onWhichBlock():
    x = int((Current.mapsize+1)/2 + Current.mapX)
    y = int((Current.mapsize+1)/2 + Current.mapY)
    isSomething(x,y)
    isSomethingNearby(x,y)


# Player Controls
def inGame_onKeyboard(key, pressed):
    global MapSizeX
    global MapSizeY
    if pressed:
        if (not Current.playerMoving):
            if key==1 or key==82:           # 'A' or 'Left'
                if not Wall.Left:
                    Current.LR = 2                    
                    Current.direction = 0
                    blockBoard.locate_spare(Current.direction)
                    playerAnimation()
                    playerTurn()
                    Current.mapX -= 1
                    checkRespawn()
                    
            elif key==4 or key==83:         # 'D' or 'Right'
                if not Wall.Right:
                    Current.LR = 1                    
                    Current.direction = 1
                    blockBoard.locate_spare(Current.direction)
                    playerAnimation()
                    playerTurn()
                    Current.mapX += 1
                    checkRespawn()
                    
            elif key==23 or key==84:         # 'W' and 'Up'
                if not Wall.Up:
                    Current.direction = 2
                    blockBoard.locate_spare(Current.direction)
                    playerAnimation()
                    playerTurn()
                    Current.mapY += 1
                    checkRespawn()
                    
            elif key==19 or key==85:         # 'S' and 'Down'
                if not Wall.Down:
                    Current.direction = 3
                    blockBoard.locate_spare(Current.direction)
                    playerAnimation()
                    playerTurn()
                    Current.mapY -= 1
                    checkRespawn()
                    
            elif key==64:       # Tab
                menu.enter()
            print("Current Position: ",Current.mapX, Current.mapY)
inGame.onKeyboard = inGame_onKeyboard

def menu_onKeyboard(key, pressed):
    if not pressed:
        if key==64 or key==59:       # ESC
            inGame.enter()
menu.onKeyboard = menu_onKeyboard

animationFrame = 0
def playerAnimation():
    Current.playerMoving = True
    global animationFrame
    animationTimer = threading.Timer(0.125, playerAnimation)
    sound = 'sounds/walk.mp3'
    if animationFrame==7:
        Sound.stop(Sound(sound))

    else:
        Sound.play(Sound(sound))
    blockBoard.boardAnimation(Current.direction)
    if Current.LR==1:
        if animationFrame==7:
            animationTimer._stop()
            animationFrame = 0
            Current.playerMoving = False
        else:
            animationTimer.start()
            animationFrame+=1
        player.setImage('images/player/playerR'+str(animationFrame%4)+'.png')
    elif Current.LR==2:
        if animationFrame==7:
            animationTimer._stop()
            animationFrame = 0
            Current.playerMoving = False
        else:
            animationTimer.start()
            animationFrame+=1
        player.setImage('images/player/playerL'+str(animationFrame%4)+'.png')
    
# Interface Controls
def setNumImage(num):
    image = "images/numbers/"+str(num)+".png"
    return image

def dayChange():
    Current.day += 1
    Days10.setImage(setNumImage(Current.day//10))
    Days1.setImage(setNumImage(Current.day%10))

cloud1 = GameObject('images/cloud1.png', inGame, -60, -10, 1.1, False)
cloud2 = GameObject('images/cloud2.png', inGame, 960, -10, 1.1, False)

def skyChange():
    if Current.sky == 1:
        Current.sky = 2
        weather.setImage('images/weathers/moon.png')
        cloud1.show()
        cloud2.show()
    elif Current.sky == 2:
        dayChange()
        Current.sky = 1
        weather.setImage('images/weathers/sun.png')
        cloud1.hide()
        cloud2.hide()
    else:               # 해, 달 외의 다른 날씨 추가 (비, 흐림 등등)
        pass    

def lightChange():
    if 0<=Current.turn<int(Current.turnMax*1/4):
        if Current.sky==1:
            Current.light += 0.08
        else:
            Current.light -= 0.08
    elif int(Current.turnMax*3/4)<=Current.turn<Current.turnMax:
        if Current.sky==1:
            Current.light -= 0.08
        else:
            Current.light += 0.08
    inGame.setLight(Current.light)
lightChange()

def playerTurn():
    Current.turn += 1
    if Current.turn==Current.turnMax:
        skyChange()
        Current.turn = 0
    else:
        lightChange()
    turns10.setImage(setNumImage(Current.turn//10))
    turns1.setImage(setNumImage(Current.turn%10))
    if Current.monkey >= 6 and Current.crocodile >= 3 and Current.snake >= 9 and Current.turtle >= 12:
        if Current.day >= Current.bossday:
            boss_start()

def showHP():
    image = 'images/hearts/'+str(Current.hp)+'.png'
    HP.setImage(image)
    menuHP.setImage(image)
showHP()

def changeHP(amount):
    Current.hp += amount
    showHP()

def xpUp(amount):
    Current.xp += amount
    if (Current.xp>=100):
        Current.xp -= 100
        levelUP(1)
        Sound.play(Sound('sounds/levelup.mp3'))
    showXP()
    showmenuXP()

def showmenuXP():
    XP = Current.xp
    if XP<10:
        menuxp100.setImage(setNumImage(0))
        menuxp10.setImage(setNumImage(0))
        menuxp1.setImage(setNumImage(XP))
    elif XP<100:
        menuxp100.setImage(setNumImage(0))
        menuxp10.setImage(setNumImage(XP//10))
        menuxp1.setImage(setNumImage(XP%10))
    else:
        x = XP-(XP//100*100)
        menuxp100.setImage(setNumImage(XP//100))
        menuxp10.setImage(setNumImage(x//10))
        menuxp1.setImage(setNumImage(x%10))
    menuxp1.show()
    menuxp10.show()
    menuxp100.show()
showmenuXP()

def showXP():
    XP = Current.xp
    if XP<10:       
        xp100.setImage(setNumImage(0))
        xp10.setImage(setNumImage(0))
        xp1.setImage(setNumImage(XP))
    elif XP<100:
        xp100.setImage(setNumImage(0))
        xp10.setImage(setNumImage(XP//10))
        xp1.setImage(setNumImage(XP%10))
    else:
        x = XP-(XP//100*100)
        xp100.setImage(setNumImage(XP//100))
        xp10.setImage(setNumImage(x//10))
        xp1.setImage(setNumImage(x%10))
    xp1.show()
    xp10.show()
    xp100.show()
showXP()

def levelUP(amount):
    Current.level += int(amount)
    showLevel()
    if Current.hp < 5:
        Current.hp = 5
        showHP()

def showLevel():
    if Current.level<10:
        level10.setImage(setNumImage(0))
        level1.setImage(setNumImage(Current.level))
        menulevel10.setImage(setNumImage(0))
        menulevel1.setImage(setNumImage(Current.level))
    elif Current.level<100:
        level10.setImage(setNumImage(Current.level//10))
        level1.setImage(setNumImage(Current.level%10))
        menulevel10.setImage(setNumImage(Current.level//10))
        menulevel1.setImage(setNumImage(Current.level%10))
    level10.show()
    level1.show()
    menulevel10.show()
    menulevel1.show()
showLevel()

def showBossHP():
    if Current.bossHP<=0:
        boss_clear()
    elif Current.bossHP<10:
        bosshp10.setImage(setNumImage(0))
        bosshp1.setImage(setNumImage(Current.bossHP))
        bosshp10.show()
        bosshp1.show()
    elif Current.bossHP<100:
        bosshp10.setImage(setNumImage(Current.bossHP//10))
        bosshp1.setImage(setNumImage(Current.bossHP%10))
        bosshp10.show()
        bosshp1.show()

def boss_start():
    global Contents
    Sound.play(Sound('sounds/roar_long.mp3'))
    bossHP.show()
    showBossHP()
    Contents[int((Current.mapsize+1)/2 + 0)][int((Current.mapsize+1)/2 + 0)] = 100
    blockBoard.setImage(boosX, bossY, 100)

def boss_clear():
    Current.isGameRunning = False
    Contents[int((Current.mapsize+1)/2 + 0)][int((Current.mapsize+1)/2 + 0)] = 30
    Sound.play(Sound('sounds/roar_short.mp3'))
    bossHP.hide()
    bosshp10.hide()
    bosshp1.hide()
    lightoffsmooth()    

def checkGameOver():
    if Current.hp <= 0:
        Current.isGameRunning = False
        lightoffsmooth()
        
def next_scene():
    if Current.hp <= 0:
        gameOver.enter()
    elif Current.bossHP <= 0:
        gameClear.enter()

def lightoffsmooth():
    lightTimer = threading.Timer(0.125, lightoffsmooth)
    if Current.light>0:
        Current.light -= 0.1
        inGame.setLight(Current.light)
        lightTimer.start()
    else:
        next_scene()
        lightTimer._stop()

def player_onMouseAction(x, y, action):
    xpUp(10)
player.onMouseAction = player_onMouseAction

def startbutton_onMouseAction(x,y,action):
    inGame.enter()
startbutton.onMouseAction = startbutton_onMouseAction

def inGame_onEnter():
    Current.isGameRunning = True
    Sound.stop(Sound('sounds/intro.mp3'))
    Sound.play(Sound('sounds/wind.mp3'))
inGame.onEnter = inGame_onEnter

def gameClear_onEnter():
    Sound.stop(Sound('sounds/wind.mp3'))
    Sound.play(Sound('sounds/gameclear.mp3'))
gameClear.onEnter = gameClear_onEnter

def gameOver_onEnter():
    Sound.stop(Sound('sounds/wind.mp3'))
    Sound.play(Sound('sounds/gameover.mp3'))
gameOver.onEnter = gameOver_onEnter

# ///// Game Start /////
Fruits.showmenuApple()
Fruits.showmenuBanana()
Fruits.showmenuOrange()
Fruits.showmenuCoconut()

Sound.play(Sound('sounds/intro.mp3'))
startGame(Startmygame)
