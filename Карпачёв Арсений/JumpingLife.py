import pygame as pg
import random

# Инициализация Pygame
pg.init()

# Настройки окна и игры
W, H = 360, 640  # Ширина и высота окна
speed = 4  # Скорость движения труб
gravity = 0.6  # Сила притяжения
jump_force = -8  # Сила прыжка
PIPE_GAP = 200  # Расстояние между верхней и нижней трубами
PIPE_DISTANCE = 400  # Расстояние между парами труб

# Загрузка изображений
bg_game = pg.image.load('photos/8-bit-nature-lu-360x640.png')  # Задний фон для игры
bg_menu = pg.image.load('photos/3b54191d83179b231a20125790af21b5.jpg')  # Задний фон для меню
player_image = pg.image.load('photos/pixil-frame-0 (6).png')  # Изображение игрока
pipe_image = pg.image.load('photos/pixil-frame-0 (9).png')  # Изображение трубы

# Корректировка размеров изображений
player_image = pg.transform.scale(player_image, (50, 50))  # Изменение размера игрока
pipe_image = pg.transform.scale(pipe_image, (70, 400))  # Изменение размера трубы

# Загрузка музыки
game_music = pg.mixer.Sound('sounds/joshua-mclean-mountain-trials.wav')  # Музыка во время игры
menu_music = pg.mixer.Sound('sounds/menu.mp3')  # Музыка в меню
lose_music = pg.mixer.Sound('sounds/game over.mp3')  # Музыка при проигрыше

# Настройки Pygame
clock = pg.time.Clock()  # Объект для контроля частоты кадров
win = pg.display.set_mode((W, H))  # Создание окна игры
pg.display.set_icon(pg.image.load('photos/pixil-frame-0 (6).png'))
pg.display.set_caption('Jumping Life')  # Установка заголовка окна


# Класс трубы
class Pipe:
    def __init__(self, img, x, y, flipped=False):
        self.img = img  # Изображение трубы
        if flipped:  # Если труба перевернута, отражаем изображение
            self.img = pg.transform.flip(img, False, True)
        self.x = x  # X-координата
        self.y = y  # Y-координата
        self.width = img.get_width()  # Ширина трубы
        self.height = img.get_height()  # Высота трубы

    def render(self, win):
        win.blit(self.img, (self.x, self.y))  # Отображение трубы

    def update(self):
        self.x -= speed  # Смещение трубы влево

    def get_rect(self):
        return pg.Rect(self.x, self.y, self.width, self.height)  # Возвращает прямоугольник


# Функция для создания новой пары труб
def create_pipe():
    pipe_height = pipe_image.get_height()  # Высота изображения трубы
    min_y = -pipe_height + 50  # Минимальная Y-координата верхней трубы
    max_y = H - PIPE_GAP - 450  # Максимальная Y-координата верхней трубы
    y_pos = random.randint(min_y, max_y)  # Случайная Y-координата для верхней трубы
    return {
        'top': Pipe(pipe_image, W, y_pos, flipped=True),  # Создаем верхнюю трубу
        'bottom': Pipe(pipe_image, W, y_pos + pipe_image.get_height() + PIPE_GAP),  # Создаем нижнюю трубу
    }


# Проверка столкновений
def check_collision(player_rect, pipes):
    for pipe_pair in pipes:  # Проходимся по всем парам труб
        if player_rect.colliderect(pipe_pair['top'].get_rect()) or player_rect.colliderect(
                pipe_pair['bottom'].get_rect()):
            return True  # Если произошло столкновение, возвращаем True
    return False  # Если столкновения нет, возвращаем False


# Функция для создания кнопки
def create_button(text, x, y, width, height, color, hover_color, action=None):
    font = pg.font.Font(None, 36)  # Шрифт для текста
    text_surface = font.render(text, True, (255, 255, 255))  # Создание текста
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))  # Координаты текста
    rect = pg.Rect(x, y, width, height)  # Создание прямоугольника для кнопки
    button = {"rect": rect, "text": text_surface, "text_rect": text_rect, "color": color, "hover_color": hover_color,
              "action": action}  # Собираем информацию о кнопке
    return button


# Функция для отрисовки кнопки
def render_button(win, button, mouse_pos):
    if button["rect"].collidepoint(mouse_pos):  # Проверяем, наведена ли мышь на кнопку
        pg.draw.rect(win, button["hover_color"], button["rect"])  # Отображаем кнопку при наведении мыши
    else:
        pg.draw.rect(win, button["color"], button["rect"])  # Отображаем кнопку в обычном состоянии
    win.blit(button["text"], button["text_rect"])  # Отображаем текст на кнопке


# Переменные персонажа
xCord, yCord = 100, H // 2  # Начальные координаты игрока
y_velocity = 0  # Начальная вертикальная скорость
pipes = []  # Список труб

# Создание кнопки "Start Game"
button_start = create_button("Start Game", W // 2 - 100, H // 2 - 30, 200, 60, (0, 128, 0), (0, 200, 0),
                             action="start_game")

# Переменная состояния игры
game_state = "menu"  # Начальное состояние игры - меню
menu_music_playing = False  # Флаг для музыки в меню
game_music_playing = False  # Флаг для музыки в игре

# Основной игровой цикл
running = True  # Флаг для работы цикла
frame_counter = 0  # Счетчик кадров
while running:
    mouse_pos = pg.mouse.get_pos()  # Получаем позицию мыши
    for event in pg.event.get():  # Проходимся по всем событиям
        if event.type == pg.QUIT:  # Если нажали на кнопку закрытия окна
            running = False  # Завершаем цикл
        if event.type == pg.MOUSEBUTTONDOWN and game_state == "menu":  # Если нажали кнопку мыши в меню
            if button_start["rect"].collidepoint(mouse_pos) and button_start["action"] == "start_game":  # Если нажали на кнопку start game
                game_state = "playing"  # Переходим в состояние игра
                pipes = []  # Обновляем трубы
                xCord, yCord = 100, H // 2  # Обновляем позицию игрока
                y_velocity = 0  # Обновляем скорость игрока
                frame_counter = 0  # Обновляем счетчик кадров

    # Управление музыкой
    if game_state == "menu":  # Если находимся в меню
        if not menu_music_playing:  # Если музыка меню еще не играет
            if game_music_playing:  # Если музыка игры играет
                pg.mixer.music.stop()  # Останавливаем музыку игры
                game_music_playing = False  # Меняем флаг
            menu_music.play(loops=-1)  # Запускаем музыку меню
            menu_music_playing = True  # Меняем флаг

    elif game_state == "playing":  # Если находимся в игре
        if not game_music_playing:  # Если музыка игры еще не играет
            if menu_music_playing:  # Если музыка меню играет
                menu_music.stop()  # Останавливаем музыку меню
                menu_music_playing = False  # Меняем флаг
            game_music.play(loops=-1)  # Запускаем музыку игры
            game_music_playing = True  # Меняем флаг

    # Отрисовка меню ИЛИ игры
    if game_state == "menu":
        win.blit(bg_menu, (0, 0))  # Отображаем фон меню
        render_button(win, button_start, mouse_pos)  # Отображаем кнопку старта
        pg.display.flip()  # Обновляем экран
    elif game_state == "playing":
        win.blit(bg_game, (0, 0))  # Отображаем фон игры

        # Обработка нажатий
        keys = pg.key.get_pressed()  # Получаем все нажатые кнопки
        if keys[pg.K_SPACE]:  # Если нажат пробел
            y_velocity = jump_force  # Применяем силу прыжка

        # Физика
        y_velocity += gravity  # Добавляем гравитацию
        yCord += y_velocity  # Меняем вертикальную позицию

        # Ограничения по вертикали
        if yCord < 0:  # Если игрок выше верха экрана
            yCord = 0  # Приравниваем к верху экрана
            y_velocity = 0  # Обнуляем вертикальную скорость
        if yCord > H - player_image.get_height():  # Если игрок ниже низа экрана
            yCord = H - player_image.get_height()  # Приравниваем к низу экрана
            y_velocity = 0  # Обнуляем вертикальную скорость

        # Управление трубами
        if frame_counter % PIPE_DISTANCE == 0:  # Если пришло время создавать новые трубы
            pipes.append(create_pipe())  # Создаем новую пару труб
        frame_counter += speed  # Увеличиваем счетчик кадров

        # Обновление труб
        for pipe_pair in pipes[:]:  # Проходимся по всем парам труб
            pipe_pair['top'].update()  # Обновляем верхнюю трубу
            pipe_pair['bottom'].update()  # Обновляем нижнюю трубу

            if pipe_pair['top'].x < -pipe_pair['top'].width:  # Если труба ушла за пределы экрана
                pipes.remove(pipe_pair)  # Удаляем пару труб из списка

        player_rect = pg.Rect(xCord, yCord, player_image.get_width(),
                              player_image.get_height())  # Получаем прямоугольник игрока
        if check_collision(player_rect, pipes):  # Если произошло столкновение
            game_music.stop()  # Останавливаем музыку игры
            lose_music.play()  # Проигрываем звук проигрыша
            font = pg.font.Font(None, 74)  # Создаем шрифт для надписи
            text = font.render("Game Over", True, (255, 0, 0))  # Создаем текст "Game Over"
            win.blit(text, (W // 2 - text.get_width() // 2, H // 2 - text.get_height() // 2))  # Выводим на экран
            pg.display.flip()  # Обновляем экран
            pg.time.wait(2000)  # Ждем 2 секунды
            running = False  # Завершаем игровой цикл

        # Отрисовка игры
        win.blit(player_image, (xCord, yCord))  # Отображаем игрока
        for pipe_pair in pipes:  # Проходимся по всем парам труб
            pipe_pair['top'].render(win)  # Отображаем верхнюю трубу
            pipe_pair['bottom'].render(win)  # Отображаем нижнюю трубу

        pg.display.flip()  # Обновляем экран

    clock.tick(30)  # Ограничиваем FPS

pg.quit()  # Завершаем Pygame
