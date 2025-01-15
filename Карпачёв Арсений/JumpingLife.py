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
bg = pg.image.load('photos/8-bit-nature-lu-360x640.png') 
image_1 = pg.image.load('photos/pixil-frame-0 (6).png') 
image_2 = pg.image.load('photos/pixil-frame-0 (9).png') 

new_image = pg.transform.scale(image_1, (100, 100)) #лысый 
new_image_2 = pg.transform.scale(image_2, (250, 400)) #труба нижняя 

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
pg.mixer.music.load('sounds/joshua-mclean-mountain-trials.wav') 
sound = pg.mixer.music.play() 
pg.mixer.music.play(loops=-1) 
 
clock = pg.time.Clock() 
win = pg.display.set_mode((W, H)) 
pg.display.set_caption('Jumping Life') 
 
 
class Pipe: 
    def __init__(self, img, x, y, flipped=False): 
        self.img = img 
        if flipped: 
            self.img = pg.transform.flip(img, False, True) 
        self.x = x 
        self.y = y 
        self.width = img.get_width() 
        self.height = img.get_height() 
 
    def render(self, win): 
        win.blit(self.img, (self.x, self.y)) 
 
    def update(self): 
        self.x -= speed 
 
# Создаем список для хранения труб 
pipes = [] 
 
# Функция создания новой пары труб 
def create_pipe(): 
    PIPE_GAP = 5  # Расстояние между трубами 
    pipe_height = new_image_2.get_height() 
     
    # Случайная позиция для верхней трубы 
    y_pos = random.randint(-pipe_height + 100, H - PIPE_GAP - 100) 
     
    return { 
        'top': Pipe(new_image_2, W, y_pos, flipped=True),  # Верхняя труба (перевернутая) 
        'bottom': Pipe(new_image_2, W, y_pos + pipe_height + PIPE_GAP)  # Нижняя труба 
    } 
 
# Основной игровой цикл 
while True: 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            quit() 
 
    # Очищаем экран и отрисовываем фон 
    win.fill((255, 255, 255)) 
    win.blit(bg, (0, 0)) 
 
    # Отрисовываем персонажа 
    win.blit(new_image, (xCord, y1)) 
 
    # Управление трубами 
    if len(pipes) == 0 or pipes[-1]['top'].x < W - 300: 
        pipes.append(create_pipe()) 
 
    # Обновление и отрисовка труб 
    for pipe_pair in pipes[:]: 
        pipe_pair['top'].render(win) 
        pipe_pair['bottom'].render(win) 
        pipe_pair['top'].update() 
        pipe_pair['bottom'].update() 
         
        # Удаляем трубы, ушедшие за экран 
        if pipe_pair['top'].x < -pipe_pair['top'].width: 
            pipes.remove(pipe_pair) 
 
    # Обработка клавиш 
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
 
    # Проверка границ 
    if xCord > 370: 
        xCord = -80 
    if y1 >= 468: 
        y1 = 468 
    if y1 <= -3: 
        y1 = -3 
 
    # Обновление экрана 
    pg.display.flip() 
    clock.tick(40)
