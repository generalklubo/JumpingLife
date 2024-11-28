#TODO: Добавить классы
#TODO: Раскидать все по папкам и модулям (файлам) +
#TODO: Загрузить все на GitHub

import pygame as pg

pg.init()

W = 360
H = 640
bg = pg.image.load('photos\8-bit-nature-lu-360x640.png')
image_1 = pg.image.load('photos\pixil-frame-0 (6).png')
image_2 = pg.image.load('photos\pixil-frame-0 (9).png')
image_3 = pg.image.load('photos\pixil-frame-0 (11).png')
new_image = pg.transform.scale(image_1, (100, 100))
new_image_2 = pg.transform.scale(image_2, (250, 400))
new_image_3 = pg.transform.scale(image_3, (250, 400))
speed = 3
jumpCount = 10
isJump = False
x = 150
xx = 130
y = 323
xCord = -45
yCord = 465
y1 = 323
yy = 120
#object1 = new_image = pg.Rect(100, 100, 50, 50)
#object2 = new_image_2 = pg.Rect(100, 100, 50, 50)
#object3 = new_image_3 = pg.Rect(100, 100, 50, 50)

pg.mixer.init()
pg.mixer.music.load('sounds\joshua-mclean-mountain-trials.wav')
sound = pg.mixer.music.play()

clock = pg.time.Clock()
win = pg.display.set_mode((W, H))
pg.display.set_caption('Jumping Life')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    win.blit(bg, (0, 0))
    win.blit(new_image, (xCord, y1))
    win.blit(new_image_2, (xx, yy))
    win.blit(new_image_3, (xx, 0))
    pg.draw.line(win, (0, 0, 0), (0, 520), (360, 520), 5)
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        xCord -= 3
    if keys[pg.K_d]:
        xCord += 3
    if not(isJump): 
        if keys[pg.K_UP]:
            y1 -= 3
        if keys[pg.K_DOWN]:
            y1 += 3
        if keys[pg.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            yCord -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False


    xCord += speed
    if xCord > 370: #370 - граница справа
        xCord = -80
    if y1 >= 468: #468 - граница снизу
        y1 = 468
    if y1 >= 468:
        ()
    elif xCord == 400:
        quit()
    clock.tick(40)

    pg.display.update()