from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame as pg
from random import choice,randrange

class symbol:
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.value = choice(green_char)
        self.interval = randrange(3,10)
        self.speed  = speed

    def draw(self,color):
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_char if color == "green" else light_green_char)
        self.y = self.y + self.speed if self.y < height else -font_size
        screen.blit(self.value,(self.x,self.y))

class SymbolColomn:
    def __init__(self,x,y):
        self.colomn_height = randrange(5,20)
        self.speed = randrange(3, 20)
        self.symbols = [symbol(x,i,self.speed) for i in range(y,y-font_size*self.colomn_height,-font_size) ]

    def draw(self):
        [symbol.draw("green") if i else symbol.draw("lightgreen") for i,symbol in enumerate(self.symbols)]

pg.init()
width = 1300
height = 700
font_size = 20
pg.display.set_caption("Ge'ez Matrix")
screen = pg.display.set_mode((width,height))
surface = pg.Surface((width,height))
clock = pg.time.Clock()

characters = [ch for ch in "፩፪፫፬፭፮፯፰፱፲"]
font = pg.font.Font("font/PGUNICODE1.TTF",size=font_size)
green_char = [font.render(char,True, pg.Color(choice(((2, 163, 25),(1, 66, 10))))) for char in characters]
light_green_char = [font.render(char, True, pg.Color(choice(((180, 255, 180),(0, 255, 70))))) for char in characters]
symbolcoloms = [SymbolColomn(x,randrange(-height,height)) for x in range(0,width,font_size-10)]

while True:
    screen.blit(surface,(width,height))
    screen.fill(pg.Color("black"))
    [symbolcolomn.draw() for symbolcolomn in symbolcoloms]
    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(30)
