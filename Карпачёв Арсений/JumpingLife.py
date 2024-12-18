#TODO: Добавить классы
#TODO: Раскидать все по папкам и модулям (файлам) +-
#TODO: Загрузить все на GitHub +

#L = length - длина 
#B = breadth - ширина 
#W = width - ширина 
#H = height - высота 

#Хочу сделать:
#1. Бесконечное кол-во труб.
#2. При столкновении основного объекта (лысый) с второстепенными объектами (трубы) всё
# останавливалось и на главном экране появлялось дополнительное окно с надписью "Проигрыш".

import pygame as pg
import random

pg.init()

W = 360
H = 640
isJump = False
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

pg.mixer.init()
pg.mixer.music.load('sounds\joshua-mclean-mountain-trials.wav')
sound = pg.mixer.music.play()
pg.mixer.music.play(loops=-1)

clock = pg.time.Clock()
win = pg.display.set_mode((W, H))
pg.display.set_caption('Jumping Life')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    win.blit(bg, (0, 0))
    win.blit(new_image, (0, y1))
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

    class Pipe:
        def __init__(self, img2, img3, img4, img5, img6, img7, x, y):
            self.img2 = img2
            self.img3 = img3
            self.img4 = img4
            self.img5 = img5
            self.img6 = img6
            self.img7 = img7
            self.x = x
            self.y = y
        def render(self, win):
            win.blit(self.img2, (self.x, self.y))
            win.blit(self.img3, (self.x, self.y))
            win.blit(self.img4, (self.x, self.y))
            win.blit(self.img5, (self.x, self.y))
            win.blit(self.img6, (self.x, self.y))
            win.blit(self.img7, (self.x, self.y))
        def update(self):
            self.x -= speed
            if self.x < -250:
                self.x = 360
            self.y = random.randint(0, 640)

        xx -= speed
        xxx -= speed
        xxxx -= speed


        clock.tick(40)

        pg.display.update()