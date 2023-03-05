# validation of the direction

import pygame, time, sys, random

error = pygame.init()

if error[1] > 0 :
    print ("[!] initialization error.. exiting")
    sys.exit()
else:
    print ("[+] initialization completed")

surface = pygame.display.set_mode((720,480))

pygame.display.set_caption("Sanke Game!!")

snakePos = [100,40]
snakeBody = [[100,60],[90,60],[80,60]]

foodPos = [random.randrange(1,72)*10, random.randrange(1,48)*10]
foodStatus = True


red=pygame.Color(255,0,0)
white=pygame.Color(255,255,255)
green=pygame.Color(0,255,0)
brown=pygame.Color(0,0,255)
black = pygame.Color(0,0,0)

fps = pygame.time.Clock()

direction = 'RIGHT'
changeto = direction

score = 0

def GameOver():
    myFont=pygame.font.SysFont("monaco",72)
    GOsurf = myFont.render("GAme Over!", True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop=(340, 180)
    surface.blit(GOsurf,GOrect)
    pygame.display.flip()
    Score(5)
    time.sleep(10)
    pygame.quit()
    sys.exit()

def Score(choice=1):
    sFont=pygame.font.SysFont("monaco",30)
    ssurf = sFont.render("score :"+str(score), True, black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop=(80, 10)
    else :
        srect.midtop=(360, 240) 
    surface.blit(ssurf,srect)
    pygame.display.flip()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    #validation of direction
    if changeto == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = "LEFT"
    if changeto == "UP" and not direction == "DOWN":
        direction = "UP"
    if changeto == "DOWN" and not direction == "UP":
        direction = "DOWN"

    # updating the snake
    if direction == "RIGHT":
        snakePos[0] += 10
    if direction == "LEFT":
        snakePos[0] -= 10
    if direction == "UP":
        snakePos[1] -= 10
    if direction == "DOWN":
        snakePos[1] += 10

    #snake machanisem
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodStatus = False
    else:
        snakeBody.pop()

    if foodStatus == False :
        foodPos = [random.randrange(1,72)*10, random.randrange(1,48)*10]
    foodStatus = True

    #Graphics

    surface.fill(white)
    for pos in snakeBody:
        a= pygame.Rect(pos[0],pos[1],10,10)
        pygame.draw.rect(surface, green, a)
    pygame.draw.rect(surface, brown,pygame.Rect(foodPos[0],foodPos[1],10,10))

    if snakePos[0] > 710 or snakePos[0] < 0:
        GameOver()
    if snakePos[1] > 470 or snakePos[1] < 0:
        GameOver()
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            GameOver()
                     
    pygame.display.flip()
    Score()
    fps.tick(25)

    
        
        
        
            
