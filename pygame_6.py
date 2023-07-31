#ctrl누르면 총알 발사

import pygame
import random
from time import sleep

WHITE = (255, 255, 255)
pad_width = 740
pad_height = 370
background_width = 740
bat_width = 110 
aircraft_width = 90
aircraft_height = 55

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x,y))

def runGame():
    global gamepad, aircraft, clock, background1, background2
    global bat, fires, bullet

    bullet_xy = []

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

    background1_x = 0
    background2_x = background_width

    bat_x = pad_width
    bat_y = random.randrange(0, pad_height)

    fire_x = pad_width
    fire_y = random.randrange(0, pad_height)
    random.shuffle(fires)
    fire = fires[0]

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

                elif event.key == pygame.K_LCTRL:
                    bullet_x = x + aircraft_width
                    bullet_y = y + aircraft_height/2
                    bullet_xy.append([bullet_x, bullet_y])

                elif event.key == pygame.K_SPACE:
                    sleep(5)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        #Clear gamepad
        gamepad.fill(WHITE)

        #Draw Background
        background1_x-=2    # background1_x = background1_x - 2 
        background2_x-=2

        if background1_x == -background_width:
            background1_x = background_width

        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)

        # Aircraft Position
        y += y_change
        if y < 0:
            y = 0
        elif y > pad_height - aircraft_height:
            y = pad_height - aircraft_height

        #Bat Position
        bat_x -= 7
        if bat_x <= 0:
            bat_x = pad_width
            bat_y = random.randrange(0, pad_height)

        #Fireball Position
        if fire == None:
            fire_x -= 30
        else:
            fire_x -= 15

        if fire_x <= 0:
            fire_x = pad_width
            fire_y = random.randrange(0, pad_height)
            random.shuffle(fires)
            fire = fires[0]

        # Bullets Position
        if len(bullet_xy)!=0:
            for i, bxy in enumerate(bullet_xy):
                bxy[0] += 15
                bullet_xy[i][0] = bxy[0]
                if bxy[0] >= pad_width:
                    bullet_xy.remove(bxy)

    
        drawObject(aircraft, x, y)
        drawObject(bat, bat_x, bat_y)
        
        if fire!=None:
            drawObject(fire, fire_x, fire_y)

        if len(bullet_xy)!=0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)

        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    quit()

def initGame():
    global gamepad, clock, aircraft, background1, background2
    global bat, fires, bullet

    fires = []

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFlying')    
    aircraft = pygame.image.load('C:\\Users\\mylov\\OneDrive\\바탕 화면\\pygame_sample\\image\\images\\plane.png')
    background1 = pygame.image.load('C:\\Users\\mylov\\OneDrive\\바탕 화면\\pygame_sample\\image\\images\\background.png')
    background2 = background1.copy()
    bat = pygame.image.load('C:\\Users\\mylov\\OneDrive\\바탕 화면\\pygame_sample\\image\\images\\bat.png')
    fires.append(pygame.image.load('C:\\Users\\mylov\\OneDrive\\바탕 화면\\pygame_sample\\image\\images\\fireball.png'))
    fires.append(pygame.image.load('C:\\Users\\mylov\OneDrive\\바탕 화면\\pygame_sample\\image\\images\\fireball2.png'))



    for i in range(5):
        fires.append(None)

    bullet= pygame.image.load('C:\\Users\\mylov\\OneDrive\\바탕 화면\\pygame_sample\\image\\images\\bullet.png')
    
    clock = pygame.time.Clock()
    runGame()

if __name__ == '__main__':
    initGame()
