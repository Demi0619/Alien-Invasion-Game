import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    ''' class to manage alien'''
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.image=pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()
        self.setting=ai_game.setting1
        self.update()
        self.check_edge()

    def update(self):
        self.x=float(self.rect.x)
        self.x+=self.setting.alien_speed*self.setting.direction
        self.rect.x=self.x

    def check_edge(self):
        if self.rect.left<=0 or self.rect.right >= self.screen_rect.right:
            return True