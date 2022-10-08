import pygame
import random
import math
from pygame import mixer
pygame.init()
bg=pygame.image.load('res\\bg.jpg')
hr=pygame.image.load('res\\hr.png')

mixer.music.load("res\\bgm.wav")
mixer.music.play(-1)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space_Invader")
icon=pygame.image.load('res\\icon.png')
pygame.display.set_icon(icon)
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
def showscore(x,y):
    score=font.render("Score: "+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


overfont=pygame.font.Font('freesansbold.ttf',62)

def gameover():
    mixer.music.stop()
    bullet_sound.stop()
    overtext=overfont.render("GAME OVER ",True,(255,255,255))
    screen.blit(overtext,(200,250))

playerimg=pygame.image.load('res\\astronomy.png')
playerX=365
playerY=480
a=0
def player(x,y):
    screen.blit(playerimg,(x,y))

bullet=pygame.image.load('res\\bullet.png')
bulletX=0
bulletY=480
state="Ready!"
c=5.5
def fire(x,y):
    global state
    state="Fire"
    screen.blit(bullet,(x+16,y+10))    

enemyimg=[]
enemyX=[]
enemyY=[]
b=[]
num=6
for i in range(num):
    enemyimg.append(pygame.image.load('res\\enemy.png'))
    enemyX.append(random.randint(0,700))
    enemyY.append(random.randint(50,300))
    b.append(0.8)
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))


def iscollision(ex,ey,bx,by):
    distance=math.sqrt(math.pow(ex-bx,2)+math.pow(ey-by,2))
    if distance<27:
        return True
    else:
        False

running= True
while running:
    screen.fill((15, 2, 102)) 
    screen.blit(bg,(0,0))
    screen.blit(hr,(0,300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        else:
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if state=="Ready!":
                        bulletX=playerX
                        bullet_sound=mixer.Sound("res\\laser.wav")
                        bullet_sound.play()
                        fire(bulletX,bulletY)       
                if event.key==pygame.K_LEFT:
                    a=-2.5
                if event.key==pygame.K_RIGHT:
                    a=2.5
            else:
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                     a=0 
                
               
    playerX+=a
    if playerX>=765:
        playerX=-35
    elif playerX<-35:
        playerX=765    
    player(playerX,playerY)

    if bulletY<=0:
        bulletY=480
        state="Ready!"
    if state=="Fire":
        fire(bulletX,bulletY)
        bulletY-=c


    for i in range(num):

        if enemyY[i]>400:
            for j in range(num):
                enemyY[j]=2000
            gameover()
            break

        enemyX[i]+=b[i]
        if enemyX[i]>=765:
            enemyY[i]+=20
            b[i]=-1.5
        elif enemyX[i]<-35:
            enemyY[i]+=20
            b[i]+=1.5
        
        collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=480
            state="Ready!"
            enemyX[i]=random.randint(0,700)
            enemyY[i]=random.randint(50,300)
            score_value+=1
        enemy(enemyX[i],enemyY[i],i)
    showscore(textX,textY)
    pygame.display.update()  
