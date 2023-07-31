import pygame

WHITE = (255, 255, 255)
pad_width = 740
pad_height = 370

def airplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))  # blit 함수의 형식을 수정합니다.

def runGame():
    global gamepad, clock

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5  # 할당 연산자를 사용합니다(== -> =).
                elif event.key == pygame.K_DOWN:
                    y_change = 5  # 할당 연산자를 사용합니다(== -> =).
            
            if event.type == pygame.KEYUP:  # 여기에 대한 if문을 수정합니다.
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        y += y_change

        gamepad.fill(WHITE)
        airplane(x, y)
        pygame.display.update()
        clock.tick(60)  # clock 객체의 tick 메소드를 호출합니다.

    pygame.quit()

def initGame():
    global gamepad, clock, aircraft  # aircraft를 전역 변수로 지정합니다.

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFlaying')
    aircraft = pygame.image.load('C:\\Users\\mylov\\OneDrive\\바탕 화면\\pygame_sample\\image\\images\\plane.png')  # 이미지를 불러올 변수명을 수정합니다.

    clock = pygame.time.Clock()  # timeClock() -> Clock()으로 수정합니다.
    runGame()

initGame()
