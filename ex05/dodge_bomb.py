import pygame as pg
import sys
import random
import datetime
import tkinter.messagebox as tkm


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(image)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
            

class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)


    def update(self, scr: Screen):
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] :
            self.rct.centery -= 1
        if key_states[pg.K_DOWN] :
            self.rct.centery += 1
        if key_states[pg.K_LEFT] :
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        if check_bound(self.rct, scr.rct) != (1, 1):
            if key_states[pg.K_UP] == True: self.rct.centery += 1
            if key_states[pg.K_DOWN] == True: self.rct.centery -= 1
            if key_states[pg.K_LEFT] == True: self.rct.centerx += 1
            if key_states[pg.K_RIGHT] == True: self.rct.centerx -= 1
        self.blit(scr)



class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size))
        self.sfc.set_colorkey((0,0,0))
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        self.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        
        self.rct.move_ip(self.vx, self.vy)
        # screen_sfc.blit(bmimg_sfc, bmimg_rct)

        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate

        scr.sfc.blit(self.sfc, self.rct)
        self.blit(scr)

def main():
    clock = pg.time.Clock()

    scr = Screen("逃げろ！こうかとん", (1600, 900), "ex04/fig/pg_bg.jpg")

    kkt = Bird("ex05/fig/6.png",2.0,(900,400))


    bkd = Bomb((255,0,0), 10, (+1, +1), scr)

    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        kkt.update(scr)

        bkd.update(scr)
        if kkt.rct.colliderect(bkd.rct):
            return


        pg.display.update()
        clock.tick(1000)


def check_bound(rct, scr_rct):

    yoko, tate = +1, +1
    if rct.left < scr_rct.left or scr_rct.right < rct.right: yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate = -1

    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()