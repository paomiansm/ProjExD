import pygame
import random
import math
pygame.init()
#画面の大きさ横(x)、縦(y)
X=1366
Y=768
screen = pygame.display.set_mode((1366 ,768))
#タイトルバーに“工科大を守ろう！こうかとん”
pygame.display.set_caption("工科大を守ろう！こうかとん")
#左上の画像読み込む
icon = pygame.image.load("./ex06/fig/cursor.png")
pygame.display.set_icon(icon)
#バックグラウンドの画像を読み込む
bgImg = pygame.image.load("./ex06/fig/bg.jpg")


#飛んでるこうかとん画像と座標の設定
playerImg = pygame.image.load("./ex06/fig/aeroshuttle_original.png")
playerX = 400
playerY = 650
playerLStep = 0
playerRStep = 0

#こうかとんの移動に関する関数
def move_player():

    global playerX

    #こうかとんの座標更新
    screen.blit(playerImg,(playerX,playerY))

    #こうかとん移動
    playerX += (playerLStep+playerRStep)

    #こうかとんが画面の幅を超えたら
    if playerX > 1284:
        playerX = 1284
    if playerX < 0:
        playerX = 0


#敵
class Enemy():
    def __init__(self):
        self.enemyImg = pygame.image.load("./ex06/fig/nav_buoy_old.png")
        self.enemyX = random.randint(0,X-64)
        self.enemyY = random.randint(100,170)
        self.enemyStep = 1
    #敵の復活
    def respawn(self):
        self.enemyX = random.randint(0,1302)
        self.enemyY = random.randint(100,170)

#敵の数
number_of_enemies = 6
enemies = []
for i in range(number_of_enemies):
    enemies.append(Enemy())

   
#敵の移動に関する関数
def move_enemy():
    for e in enemies:
        #敵座標更新
        screen.blit(e.enemyImg,(e.enemyX,e.enemyY))

        #敵の移动
        e.enemyX += e.enemyStep

        #敵が画面の幅を超えたら
        if e.enemyX > 1302 or e.enemyX < 0:
            e.enemyStep *= -1
            e.enemyY += 20

#銃弾に関する関数
class Bullet():
    def __init__(self):
        self.bulletImg = pygame.image.load("./ex06/fig/missile_harpoon.png")
        self.bulletX = playerX + 35
        self.bulletY = playerY - 26
        self.bulletStep = 5

    def hit(self):
        for e in enemies:
            if(distance(self.bulletX,self.bulletY,e.enemyX,e.enemyY)<20):
                bullets.remove(self)
                e.respawn()

#空の銃弾リスト
bullets = []

#銃弾の移動に関する関数
def move_bullet():
    for b in bullets:
        screen.blit(b.bulletImg,(b.bulletX,b.bulletY))
        b.hit()
        b.bulletY -= b.bulletStep
        if b.bulletY < 0:
            bullets.remove(b)

#銃弾と敵の衝突判定
def distance(bulletX,bulletY,enemyX,enemyY):
    a = bulletX - enemyX
    b = bulletY - enemyY
    return math.sqrt(a * a + b * b)

#ゲーム初級Trueにする
running = True
while running:

    #バックグラウンドを描画する
    screen.blit(bgImg,(0,0))

    #イベント
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerRStep = 5
            elif event.key == pygame.K_LEFT:
                playerLStep = -5
            elif event.key == pygame.K_SPACE:
                bullets.append(Bullet())
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                playerRStep = 0
            elif event.key == pygame.K_LEFT:
                playerLStep = 0

    #移動関数の呼び出し
    move_player()
    move_enemy()
    move_bullet()

    #デイスプレイ更新
    pygame.display.flip()