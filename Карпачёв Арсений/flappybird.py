import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
w = 30
h = 30
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

FPS = 30
GRAVITY = 1
JUMP = -15
PIPE_WIDTH = 70
PIPE_GAP = 150

bird_img = pygame.Surface(w, h, 30, 30) 
bird_img.fill(255, 255, 0) 

class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.vel = 0
        self.rect = pygame.Rect(self.x, self.y, 30, 30)

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.vel = JUMP

    def draw(self, win):
        win.blit(bird_img, (self.x, self.y))