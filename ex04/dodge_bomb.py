import pygame as pg
import sys
import random
import datetime
import tkinter.messagebox as tkm
def main():
    clock = pg.time.Clock()
    font = pg.font.Font(None, 60)


#練習１
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("ex04/fig/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    speed = 1


#練習３
    kkimg_sfc = pg.image.load("ex04/fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900, 400

#練習5

    bmimg_sfc = pg.Surface((20, 20))
    bmimg_sfc.set_colorkey((0,0,0))

    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    vx, vy = +1, +1

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        screen_sfc.blit(kkimg_sfc, kkimg_rct)       
        日付 = font.render(str(datetime.date.today()), True, (100, 0, 100))
        時刻 = font.render(datetime.datetime.now().strftime("%H:%M:%S"), True, (0, 0, 100))
        screen_sfc.blit(日付, [1350, 40])    
        screen_sfc.blit(時刻, [1370, 80])
#練習２
        for event in pg.event.get():
            if event.type == pg.QUIT: return

#練習４
        
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP] == True: kkimg_rct.centery -= speed
        if key_states[pg.K_DOWN] == True: kkimg_rct.centery += speed
        if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -= speed
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += speed

        if check_bound(kkimg_rct, screen_rct) != (1, 1):
            if key_states[pg.K_UP] == True: kkimg_rct.centery += speed
            if key_states[pg.K_DOWN] == True: kkimg_rct.centery -= speed
            if key_states[pg.K_LEFT] == True: kkimg_rct.centerx += speed
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= speed

        screen_sfc.blit(kkimg_sfc,kkimg_rct)

        bmimg_rct.move_ip(vx,vy)

        screen_sfc.blit(bmimg_sfc, bmimg_rct)

        yoko, tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate

        if key_states[pg.K_SPACE] == True:
            kkimg_sfc = pg.image.load("ex04/fig/3.png")
            kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
        else:
            kkimg_sfc = pg.image.load("ex04/fig/6.png")
            kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)

        if key_states[pg.K_LSHIFT] == True:
            speed = 2
        else:
            speed = 1

        if key_states[pg.K_1] == True:
            kkimg_sfc = pg.image.load("ex04/fig/2.png")
            kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)





        if kkimg_rct.colliderect(bmimg_rct):
            if key_states[pg.K_SPACE] == True:
                continue
            if key_states[pg.K_1] == True:
                vx *= -1
                vy *= -1
            else:
                return False


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