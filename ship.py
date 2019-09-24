import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    ''' a class to manage ship'''
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        #load the ship image and get its react
        self.image=pygame.image.load('image/ship.bmp')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.move_to_right=False
        self.move_to_left=False
        self.settings=ai_game.setting1
        self.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update_ship(self):
        if self.move_to_right and self.rect.right<self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_to_left and self.rect.left>0:
            self.x -= self.settings.ship_speed
        self.rect.x=self.x

    def recenter_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x=float(self.rect.x)
