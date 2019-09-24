import pygame
from pygame.sprite import Sprite


class Bullet1(Sprite):
    def __init__(self,bs):
        super().__init__()
        self.screen=bs.screen
        self.color=(60,60,60)
        self.rect=pygame.Rect(0,0,10,3)
        self.rect.midright=bs.plane.rect.midright
        self.x=float(self.rect.x)

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

    def update(self):
        self.x+=1.5
        self.rect.x=self.x

