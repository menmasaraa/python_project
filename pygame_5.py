import pygame
import random

WHITE = (255, 255, 255)
pad_width = 740
pad_height = 370
background_width = 740

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x,y))

def runGame():
    global gamepad, aircraft, clock, background1, background2
    global bat, fires

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
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        y += y_change
        gamepad.fill(WHITE)

        background1_x-=1
        background2_x-=1

        bat_x-=7
        if bat_x <=0:
            bat_x = pad_width
            bat_y = random.randrange(0, pad_height)

        if fire == None:
            fire_x-=30
        else:
            fire_x-=15

        if fire_x<=0:
            fire_x = pad_width
            fire_y = random.randrange(0, pad_height)
            random.shuffle(fires)
            fire = fires[0]
            

        if background1_x == -background_width:
            background1_x = background_width

        if background2_x == -background_width:
            background2_x = background_width

        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)
        drawObject(bat, bat_x, bat_y)
        if fire!=None:
            drawObject(fire, fire_x, fire_y)
        drawObject(aircraft, x, y)

        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    quit()

def initGame():
    global gamepad, clock, aircraft, background1, background2
    global bat, fires

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

    clock = pygame.time.Clock()
    runGame()

if __name__ == '__main__':
    initGame()
