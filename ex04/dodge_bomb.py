import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

#練習１
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))
    screen_rct = screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("ex04/fig/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    #pg.display.update()

    #clock.tick(0.5)

#練習３
    kkimg_sfc = pg.image.load("ex04/fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900, 400

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

#練習２
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        pg.display.update()
        clock.tick(1000)






if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()