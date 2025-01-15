import pygame as pg
import random

pg.init()

# Настройки окна и игры
W, H = 360, 640
speed = 4
gravity = 0.6
jump_force = -8
PIPE_GAP = 200  # Расстояние между верхней и нижней трубами
PIPE_DISTANCE = 400  # Расстояние между трубами по горизонтали

# Загрузка изображений
bg = pg.image.load('photos/8-bit-nature-lu-360x640.png') # Задний фон
player_image = pg.image.load('photos/pixil-frame-0 (6).png')  # Персонаж
pipe_image = pg.image.load('photos/pixil-frame-0 (9).png')  # Труба

# Корректировка размеров
player_image = pg.transform.scale(player_image, (50, 50))
pipe_image = pg.transform.scale(pipe_image, (70, 400))

# Музыка
pg.mixer.init()
pg.mixer.music.load('sounds/joshua-mclean-mountain-trials.wav')
pg.mixer.music.play(loops=-1) # Бесконечный цикл музыки

# Настройки Pygame
clock = pg.time.Clock()
win = pg.display.set_mode((W, H))
pg.display.set_caption('Jumping Life')

# Класс трубы
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

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.width, self.height)

# Создание новой пары труб
def create_pipe():
    pipe_height = pipe_image.get_height()
    min_y = -pipe_height + 50  # Максимальная высота появления верхней трубы
    max_y = H - PIPE_GAP - 450  # Минимальная высота для верхней трубы
    y_pos = random.randint(min_y, max_y)
    return {
        'top': Pipe(pipe_image, W, y_pos, flipped=True),
        'bottom': Pipe(pipe_image, W, y_pos + pipe_image.get_height() + PIPE_GAP),
    }


# Проверка столкновений
def check_collision(player_rect, pipes):
    for pipe_pair in pipes:
        if player_rect.colliderect(pipe_pair['top'].get_rect()) or player_rect.colliderect(pipe_pair['bottom'].get_rect()):
            return True
    return False

# Переменные персонажа
xCord, yCord = 100, H // 2
y_velocity = 0
pipes = []

# Основной игровой цикл
running = True
frame_counter = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Обработка нажатий
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        y_velocity = jump_force

    # Физика
    y_velocity += gravity
    yCord += y_velocity

    # Ограничения по вертикали
    if yCord < 0:  # Ограничение сверху
        yCord = 0
        y_velocity = 0
    if yCord > H - player_image.get_height():  # Ограничение снизу
        yCord = H - player_image.get_height()
        y_velocity = 0

    # Управление трубами
    if frame_counter % PIPE_DISTANCE == 0:  # Создаем новую пару труб через определенные интервалы
        pipes.append(create_pipe())
    frame_counter += speed

    # Обновление труб
    for pipe_pair in pipes[:]:
        pipe_pair['top'].update()
        pipe_pair['bottom'].update()

        if pipe_pair['top'].x < -pipe_pair['top'].width:  # Удаляем трубы за пределами экрана
            pipes.remove(pipe_pair)

    # Проверка столкновений
    player_rect = pg.Rect(xCord, yCord, player_image.get_width(), player_image.get_height())
    if check_collision(player_rect, pipes):
        font = pg.font.Font(None, 74)
        text = font.render("Проигрыш", True, (255, 0, 0))
        win.blit(text, (W // 2 - text.get_width() // 2, H // 2 - text.get_height() // 2))
        pg.display.flip()
        pg.time.wait(2000)
        running = False

    # Отрисовка
    win.blit(bg, (0, 0))  # Фон
    win.blit(player_image, (xCord, yCord))  # Персонаж
    for pipe_pair in pipes:  # Трубы
        pipe_pair['top'].render(win)
        pipe_pair['bottom'].render(win)

    pg.display.flip()
    clock.tick(30)

pg.quit()
