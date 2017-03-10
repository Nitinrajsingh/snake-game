import pygame
import time
import random
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green= (0,155,0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game')


clock = pygame.time.Clock()

font=pygame.font.SysFont(None,25)

def snake(block_size,snakelist):
    for xny in snakelist:
     pygame.draw.rect(gameDisplay, black, [xny[0], xny[1], 10,block_size])

def message_to_screen(msg,color):
    screen_text=font.render(msg ,True, color )
    gameDisplay.blit(screen_text,[175,300])
    pygame.display.update()
def gameloop():
    gameExit = False
    gameover= False
    lead_x = 300
    lead_y = 300
    lead_x_change = 0
    lead_y_change = 0
    block_size=10
    snakeList = []
    snakeLength= 10
    randApplex= round(random.randrange(0,800-10)/10.0)*10
    randAppley= round((random.randrange(0,600-10))/10.0)*10

    while not gameExit:
        while gameover ==True:
            gameDisplay.fill(white)
            message_to_screen("game over ,press p to play again or q to quit",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key== pygame.QUIT:
                        gameExit =True
                        gameover =False
                    if event.key ==pygame.K_p:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    lead_x_change = -10
                    lead_y_change =0
                elif event.key==pygame.K_RIGHT:
                    lead_x_change = 10
                    lead_y_change =0
                elif event.key == pygame.K_UP:
                    lead_y_change = -10
                    lead_x_change=0
                elif event.key == pygame.K_DOWN:
                    lead_y_change= 10
                    lead_x_change =0

        if lead_x+10>=800 or lead_x<=0 or lead_y<=0 or lead_y+snakeLength>=600:
            gameover=True

        lead_x+=lead_x_change
        lead_y+=lead_y_change
        gameDisplay.fill(white)



        pygame.draw.rect(gameDisplay,red,[randApplex,randAppley,10,10])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachsegment in snakeList[:-1]:
            if eachsegment == snakeHead and snakeLength>10:
                gameover=True
        snake(block_size, snakeList)
        pygame.display.update()
        if lead_x==randApplex and lead_y==randAppley:
            randApplex = round(random.randrange(0, 800 - 10) / 10.0) * 10
            randAppley = round((random.randrange(0, 600 - 10)) / 10.0) * 10
            snakeLength+=10
        clock.tick(20)

    pygame.quit()
    quit()

gameloop()