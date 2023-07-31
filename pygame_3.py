import pygame

WHITE = (255, 255, 255)
pad_width = 740
pad_height = 370

def back(x, y):
    global gamepad, background
    gamepad.blit(background, (x, y))  # blit 함수의 형식을 수정합니다.

def airplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))

def runGame():
    global gamepad, aircraft, clock, background

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

    background_x = 0

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
        back(background_x, 0)
        airplane(x, y)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def initGame():
    global gamepad, clock, aircraft, background

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFlying')
    aircraft = pygame.image.load('C:\\Users\\mylov\\OneDrive\\바탕 화면\\pygame_sample\\image\\images\\plane.png')
    background = pygame.image.load('C:\\Users\\mylov\\OneDrive\\바탕 화면\\pygame_sample\\image\\images\\background.png')

    clock = pygame.time.Clock()
    runGame()

initGame()
