#L = length - длина 
#B = breadth - ширина 
#W = width - ширина 
#H = height - высота 

#Хочу сделать:
#1. Бесконечное количество труб.
#2. При столкновении основного объекта (лысый) с второстепенными объектами (трубы) всё останавливалось и на главном экране появлялся дополнительный объект с надписью "Проигрыш".
#3. Бесконечный проигрыш музыки.

import pygame as pg

pg.init()

W = 360
H = 640
isJump = False
speed = 3
x = 150
xx = 130
y = 323
xxx = 430
xxxx = 750
xCord = -45
yCord = 465
y1 = 323
yy = 120
bg = pg.image.load('photos\8-bit-nature-lu-360x640.png')
image_1 = pg.image.load('photos\pixil-frame-0 (6).png')
image_2 = pg.image.load('photos\pixil-frame-0 (9).png')
image_3 = pg.image.load('photos\pixil-frame-0 (11).png')
image_4 = pg.image.load('photos\pixil-frame-0 (7).png')
image_5 = pg.image.load('photos\pixil-frame-0 (21).png')
image_6 = pg.image.load('photos\pixil-frame-0 (47).png')
image_7 = pg.image.load('photos\pixil-frame-0 (97).png')
new_image = pg.transform.scale(image_1, (100, 100)) #лысый
new_image_2 = pg.transform.scale(image_2, (250, 400)) #труба нижняя
new_image_3 = pg.transform.scale(image_3, (250, 400)) #труба верхняя
new_image_4 = pg.transform.scale(image_4, (250, 400)) #труба верхняя
new_image_5 = pg.transform.scale(image_5, (250, 400)) #труба нижняя
new_image_6 = pg.transform.scale(image_6, (250, 400)) #труба нижняя 
new_image_7 = pg.transform.scale(image_7, (250, 400)) #труба верхняя

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
    ni = win.blit(new_image, (0, y1))
    ni2 = win.blit(new_image_2, (xx, yy))
    ni3 = win.blit(new_image_3, (xx, 0)) 
    ni4 = win.blit(new_image_4, (xxx, 0))
    ni5 = win.blit(new_image_5, (xxx, yy)) 
    ni6 = win.blit(new_image_6, (xxxx, yy)) 
    ni7 = win.blit(new_image_7, (xxxx, 0)) 
    line = pg.draw.line(win, (0, 0, 0), (0, 520), (360, 520), 5)
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
    variables = [ni, ni2, ni3, ni4, ni5, ni6, ni7]
    for ni2 in variables:
        win.blit(new_image_2, (1500, 0))

    if xCord > 370: #370 - граница справа
        xCord = -80
    if y1 >= 468: #468 - граница снизу
        y1 = 468
    if y1 <= -3:
        y1 = -3
    if y1 >= 468:
        ()
    elif xCord == 400:
        quit()
    xx -= speed
    xxx -= speed
    xxxx -= speed
    clock.tick(40)

    pg.display.update()