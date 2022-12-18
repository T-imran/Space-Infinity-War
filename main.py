import math
import pygame
import random
import time

# screen
height = 626
weight = 626
pygame.init()
screen = pygame.display.set_mode((height, weight))
pygame.display.set_caption("Space infinity war".upper())
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# background
background = pygame.image.load("bgfinal.jpg")

scorevalue = 0
explosion = (pygame.transform.scale(pygame.image.load("explosion.png"), (64, 64)))
# player
playerimg = pygame.image.load("plane0.png")
playerimg2 = pygame.image.load("plane1.png")
playerimg3 = pygame.image.load("plane2.png")
playerimg4 = pygame.image.load("plane3.png")
playerimg5 = pygame.image.load("plane4.png")
playerX = 293
playerY = 540
playerchange = 0
playerchangeY = 0

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemychange = []
num = 5

for i in range(num):
    enemyimg.append(pygame.image.load("ufo0.png"))
    enemyimg.append(pygame.image.load("ufo1.png"))
    enemyimg.append(pygame.image.load("ufo2.png"))
    enemyimg.append(pygame.image.load("ufo3.png"))
    enemyX.append(random.randint(0, 560))
    enemyY.append(random.randint(50, 300))
    enemychange.append(0.2)

# Bullet

bulletimg = pygame.image.load("bullet.png")
bulletimg2 = pygame.image.load("bullet2.png")
bulletimg3 = pygame.image.load("bullet4.png")

bulletX = 310
bulletY = 540
bulletchangeX = 0
bulletchangeY = -1
bulletstate = "ready"

# stone
stoneimg = []
stoneX = []
stoneY = []
stonespeed = []
stonenum = 10
for u in range(stonenum):
    stoneimg.append(pygame.transform.scale(pygame.image.load("meteor3.png"), (40, 40)))
    stoneX.append(random.randint(-800, 0))
    stoneY.append(random.randint(-500, 0))
    stonespeed.append(0.8)

# stone
meteorimg = []
meteorX = []
meteorY = []
meteorspeedx = []
meteorspeed = []
meteornum = 10
for m in range(meteornum):
    meteorimg.append(pygame.transform.scale(pygame.image.load("meteor1.png"), (40, 40)))
    meteorX.append(random.randint(0, 700))
    meteorY.append(random.randint(-50, 700))
    meteorspeedx.append(-1)
    meteorspeed.append(1)

# score

font = pygame.font.Font("freesansbold.ttf", 25)
textx = 10
texty = 40

Level = 1
levelfont = pygame.font.Font("freesansbold.ttf", 32)

tip = pygame.font.Font("freesansbold.ttf", 16)


def tips():
    tiptxt = tip.render("Tip:Power Activate.", True, (255, 255, 0))
    screen.blit(tiptxt, (130, 35))


def levelpoint():
    global Level
    if scorevalue >= 100:
        Level = 2
    if scorevalue >= 200:
        Level = 3
    if scorevalue >= 300:
        Level = 4
    if scorevalue >= 400:
        Level = 5
    if scorevalue >= 500:
        Level = 6

    leveltxt = levelfont.render("Level:" + str(Level), True, (255, 255, 255))
    screen.blit(leveltxt, (500, 10))


def pause():
    paused = True
    while paused:
        screen.fill((10, 50, 100))
        screen.blit(background, (0, 0))
        pausetext = pygame.font.Font("freesansbold.ttf", 64)
        ptext = ('PAUSE ')
        ptxtsrc = pausetext.render(ptext, True, (255, 255, 255))
        screen.blit(ptxtsrc, (200, 280))
        pdistext = pygame.font.Font("freesansbold.ttf", 32)
        pdi = ("Press - 'C to continue'     'X to Quit' ")
        pdisrc = pdistext.render(pdi, True, (255, 255, 255))
        screen.blit(pdisrc, (40, 350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

        pygame.display.update()


def gameover():
    global scorevalue
    global hscore
    gameover = True
    while gameover:
        screen.fill((10, 50, 100))
        screen.blit(background, (0, 0))
        gameover_text = pygame.font.Font("freesansbold.ttf", 64)
        game = gameover_text.render("YOU LOST!", True, (255, 0, 0))
        gameover_score_text = pygame.font.Font("freesansbold.ttf", 32)
        overtext = gameover_score_text.render("Your Score: " + str(scorevalue), True, (0, 255, 0))
       
        gameover_option_text = pygame.font.Font("freesansbold.ttf", 16)
        optiontext = gameover_option_text.render("Click Mouse Button to paly      or      'X to Quit'", True,
                                                 (255, 255, 255))
        screen.blit(game, (150, 300))
        screen.blit(overtext, (150, 400))
        screen.blit(hscoretxt,(150,450))
        screen.blit(optiontext, (150, 500))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # keys
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameover = False

        pygame.display.update()


def showscore(x, y):
    score = font.render("Score:" + str(scorevalue), True, (255, 255, 255))
    screen.blit(score, (x, y))


def Highscore():
    with open("High score.txt", "r") as f:
        return f.read()


def player(x, y):
    screen.blit(playerimg, (playerX, playerY))


def player2(x, y):
    screen.blit(playerimg2, (playerX, playerY))


def player3(x, y):
    screen.blit(playerimg3, (playerX, playerY))


def player4(x, y):
    screen.blit(playerimg4, (playerX, playerY))


def player5(x, y):
    screen.blit(playerimg5, (playerX, playerY))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (enemyX[i], enemyY[i]))


def bullet(x, y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletimg, (x + 17, y))


def bullet2(x, y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletimg2, (x + 17, y))


def bullet3(x, y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletimg3, (x + 17, y))


def Collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27 and bulletstate is "fire":
        return True
    else:
        return False


def collision_stone(playerX, playerY, stoneX, stoneY):
    distance_of_stone = math.sqrt(math.pow(playerX - stoneX, 2) + (math.pow(playerY - stoneY, 2)))
    if distance_of_stone < 27:
        return True
    else:
        return False


def collision_meteor(playerX, playerY, meteorX, meteorY):
    distance_of_stone = math.sqrt(math.pow(playerX - meteorX, 2) + (math.pow(playerY - meteorY, 2)))
    if distance_of_stone < 27:
        return True
    else:
        return False


def stone_speed():
    for u in range(stonenum):
        if Level >= 3:
            stoneY[u] += stonespeed[u]
            stoneX[u] += stonespeed[u]
            screen.blit(stoneimg[u], (stoneX[u], stoneY[u]))
            if stoneY[u] and stoneX[u] > 3000:
                stoneX[u] = (random.randint(-800, 0))
                stoneY[u] = (random.randint(-500, 0))


def meteor_speed():
    for m in range(meteornum):
        if Level >= 5:
            meteorY[m] += meteorspeed[m]
            meteorX[m] += meteorspeedx[m]
            screen.blit(meteorimg[m], (meteorX[m], meteorY[m]))
            if meteorX[m] < -3000:
                meteorX[m] = (random.randint(0, 900))
                meteorY[m] = (random.randint(-70, 700))


# Menu loop
runing = True
while runing:
    # clock.tick(120)
    # RGB
    screen.fill((10, 50, 100))
    screen.blit(background, (0, 0))
    overtext = "notshow"


    def menu_text():
        menu_game_name = pygame.font.Font("freesansbold.ttf", 80)
        game_name1 = menu_game_name.render("Space", True, (102, 204, 0))
        game_name2 = menu_game_name.render("Infinity", True, (204, 0, 204))
        game_name3 = menu_game_name.render("war", True, (255, 255, 0))
        screen.blit(game_name1, (60, 80))
        screen.blit(game_name2, (330, 80))
        screen.blit(game_name3, (250, 150))
        menu = pygame.font.Font("freesansbold.ttf", 32)
        name1 = ('Click Mouse Button')
        name2 = ('To Start')
        menutxt = menu.render(name1, True, (255, 255, 255))
        screen.blit(menutxt, (150, 350))
        menutxt2 = menu.render(name2, True, (255, 255, 255))
        screen.blit(menutxt2, (250, 390))
        pdistext = pygame.font.Font("freesansbold.ttf", 16)
        pdi = ("Press -      'Esc to Pause'      'R to Restart'        'X to Quit' ")
        pdisrc = pdistext.render(pdi, True, (255, 255, 255))
        pdisrc2 = pdistext.render("Control:   'Left= A'    'Right=D'    'Fire= Space' ", True, (255, 255, 255))
        screen.blit(pdisrc, (100, 520))
        screen.blit(pdisrc2, (130, 550))


    menu_text()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            scorevalue = 0
            lost = "play"
            retry = "no_retry"
            overtext = "show"
            Level = 1
            enemyX[i] = (random.randint(0, 550))
            enemyY[i] = (random.randint(50, 300))
            try:
                hscore = int(Highscore())
            except:
                hscore = 0

            # Main loop
            runing = True
            while runing:

                # 1 no. Point
                # clock.tick(120)
                # RGB
                screen.fill((10, 50, 100))
                screen.blit(background, (0, 0))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        runing = False

                    # keys
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            retry = "yes_retry"
                        if event.key == pygame.K_ESCAPE:
                            pause()

                        if event.key == pygame.K_d:
                            playerchange = 0.4
                        if event.key == pygame.K_a:
                            playerchange = -0.4
                        if event.key == pygame.K_w:
                            playerchangeY += -0.4
                        if event.key == pygame.K_s:
                            playerchangeY += 0.4
                        if event.key == pygame.K_SPACE:
                            if bulletstate is "ready":
                                bulletX = playerX
                                bulletY = playerY
                                bullet(bulletX, bulletY)

                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_d:
                                playerchange = 0.4
                            if event.key == pygame.K_a:
                                playerchange = -0.4
                            if event.key == pygame.K_w:
                                playerchangeY = -0
                            if event.key == pygame.K_s:
                                playerchangeY = 0
                playerX += playerchange

                if Level == 3:
                    tips()

                    if playerX <= -64:
                        playerX = 615
                    elif playerX >= 615:
                        playerX = -64
                else:

                    if playerX <= 0:
                        playerX = 0
                    elif playerX >= 562:
                        playerX = 562
                playerY += playerchangeY
                if playerY <= 0:
                    playerY = 0
                elif playerY >= 562:
                    playerY = 562

                # enney part
                for i in range(num):

                    # game over

                    if enemyY[i] >= 500:
                        lost = "over"
                        for j in range(num):
                            enemyY[j] = 100
                            playerchange = 0

                    if enemyX[i] >= 562:

                        if scorevalue >= 2000:
                            enemychange[i] = -0.7
                            enemyY[i] += 30

                        if scorevalue >= 1000:
                            enemychange[i] = -0.5
                            enemyY[i] += 25

                        else:
                            enemychange[i] = -0.2
                            enemyY[i] += 20

                    elif enemyX[i] <= 0:

                        if scorevalue >= 2000:
                            enemychange[i] = 0.4
                            enemyY[i] += 30

                        if scorevalue >= 1000:
                            enemychange[i] = 0.3
                            enemyY[i] += 25

                        else:
                            enemychange[i] = 0.2
                            enemyY[i] += 20
                    enemyX[i] += enemychange[i]

                    iscollision = Collision(enemyX[i], enemyY[i], bulletX, bulletY)
                    if iscollision:
                        bulletY = 480
                        bulletstate = "ready"

                        enemyX[i] = (random.randint(0, 550))
                        enemyY[i] = (random.randint(50, 300))

                        scorevalue += 100

                    enemy(enemyX[i], enemyY[i], i)

                # bullet part
                if bulletY <= 0:
                    bulletY = 540
                    bulletstate = "ready"
                if bulletstate is "fire":
                    bulletY += bulletchangeY
                    if Level == 1 or 2:
                        bullet(bulletX, bulletY)
                    if Level == 2:
                        bullet2(bulletX, bulletY)
                    if Level >= 3:
                        bullet3(bulletX, bulletY)

                # Player
                if Level == 1:
                    player(playerX, playerY)
                if Level == 2:
                    player(playerX, playerY)
                if Level == 3:
                    player2(playerX, playerY)
                if Level == 4:
                    player3(playerX, playerY)
                if Level == 5:
                    player4(playerX, playerY)
                if Level == 6:
                    player5(playerX, playerY)

                for u in range(stonenum):
                    stone = collision_stone(playerX, playerY, stoneX[u], stoneY[u])
                    if stone:
                        enemyY[i] += 2
                        screen.blit(explosion, (playerX + 10, playerY + 5))

                for m in range(meteornum):
                    meteor = collision_meteor(playerX, playerY, meteorX[m], meteorY[m])
                    if meteor:
                        enemyY[i] += 2
                        screen.blit(explosion, (playerX + 10, playerY + 5))

                stone_speed()
                meteor_speed()
                levelpoint()
                showscore(textx, texty)
                #checking high score
                if hscore<scorevalue:
                    hscore=scorevalue
                with open("High score.txt","w") as f:
                    f.write(str(hscore))
                hscoretxt = font.render("High Score:" + str(hscore), True, (255, 255, 255))
                screen.blit(hscoretxt,(10,10))
                #checking Game over
                if lost == "over":
                    gameover()
                    break
                if retry == "yes_retry":
                    break
                if lost == "play":
                    pygame.display.update()

    pygame.display.update()
