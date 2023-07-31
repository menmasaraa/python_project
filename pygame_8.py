import pygame
import random
from time import sleep

WHITE = (255, 255, 255)
RED = (255, 0, 0)
pad_width = 740
pad_height = 370
background_width = 740
aircraft_width = 89
aircraft_height = 55
bat_width = 108
bat_height = 67

# ------------->ADDED

fireball1_width = 140
fireball1_height = 61
fireball2_width = 86
fireball2_height = 59
# ------------->

# ------------->ADDED
def textObj(text, font):
    textSurface = font.render(text,True, RED)
    return textSurface, textSurface.get_rect()

def dispMessage(text):
    global gamepad

    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = textObj(text, largeText)
    TextRect.center = ((pad_width/2),(pad_height/2))
    gamepad.blit(TextSurf, TextRect)
    pygame.display.update()
    sleep(2)
    runGame()

def crash():
    global gamepad
    dispMessage('Crashed!')
# ------------->


def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x,y))

def runGame():
    global gamepad, aircraft, clock, background1, background2
    global bat, fires, bullet, boom

    isShotBat = False
    boom_count = 0

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

    #------------------->ADDED
    fireball_width = 0  # 초기화
    fireball_height = 0  # 초기화
    #------------------->

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

        if background2_x == -background_width:
            background2_x = background_width

        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)

        #------------------>ADDED

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
        if fire[1] == None:   #MODIFIED
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

                #Check if bullet strike Bat
                if bxy[0] > bat_x:
                    if bxy[1] > bat_y and bxy[1] < bat_y + bat_height:
                        bullet_xy.remove(bxy)
                        isShotBat = True

                if bxy[0] >= pad_width:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass


        # --------------------> ADDED
        #Check aircraft crashed by BAT
        if x + aircraft_width > bat_x:
            if (y > bat_y and y < bat_y + bat_height) or \
               (y + aircraft_height > bat_y and  y + aircraft_height < bat_y + bat_height):
                    crash()

        # Check aircraft crashed by Fireball
        if fire[1]!=None:
            if fire[0] == 0:
                fireball_width = fireball1_width
                fireball_height = fireball1_height
            elif fire[0] == 1:
                fireball_width = fireball2_width
                fireball_height = fireball2_height

            if x + aircraft_width > fire_x:
                if (y > fire_y and y < fire_y + fireball_height) or \
                   (y + aircraft_height > fire_y and  + aircraft_height < fire_y + fireball_height):
                    crash()
                    
        # -------------------->

        drawObject(aircraft, x, y)

        if len(bullet_xy)!=0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)
        
        if not isShotBat:
            drawObject(bat, bat_x, bat_y)
        else:
            drawObject(boom, bat_x, bat_y)
            boom_count += 1
            if boom_count > 5:
                boom_count = 0
                bat_x = pad_width
                bat_y = random.randrange(0, pad_height-bat_height)
                isShotBat = False

        # --------------------> MODIFIED
        if fire != None:
            drawObject(fire[1], fire_x, fire_y)
        #--------------------->

        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    quit()

def initGame():
    global gamepad, clock, aircraft, background1, background2
    global bat, fires, bullet, boom

    fires = []

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFlying')    
    aircraft = pygame.image.load("/Users/uncledrew/Desktop/pygame/image/images/plane.png")
    background1 = pygame.image.load("/Users/uncledrew/Desktop/pygame/image/images/background.png")
    background2 = background1.copy()
    bat = pygame.image.load("/Users/uncledrew/Desktop/pygame/image/images/bat.png")
    #-----------------> MODIFIED
    fires.append((0, pygame.image.load("/Users/uncledrew/Desktop/pygame/image/images/fireball.png")))
    fires.append((1, pygame.image.load("/Users/uncledrew/Desktop/pygame/image/images/fireball2.png")))
    # ---------------->
    boom = pygame.image.load("/Users/uncledrew/Desktop/pygame/image/images/boom.png")


    #-----------------> MODIFIED
    # 빈 pygame.Surface 객체를 추가
    for i in range(5):
        fires.append((i+2, pygame.Surface((1, 1))))  # 1x1 크기의 빈 Surface 추가

    bullet= pygame.image.load("/Users/uncledrew/Desktop/pygame/image/images/bullet.png")
    
    clock = pygame.time.Clock()
    runGame()

if __name__ == '__main__':
    initGame()
