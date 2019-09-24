import pygame


class Plane:
    def __init__(self,bs):
        self.screen=bs.screen
        self.screen_rect=bs.screen.get_rect()
        self.image=pygame.image.load('image/plane.bmp')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.move_to_right=False
        self.move_to_left=False
        self.move_up=False
        self.move_down=False

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update_plane(self):
        if self.move_to_right and self.rect.right<self.screen_rect.right:
            self.rect.x +=1
        if self.move_to_left and self.rect.left>0:
            self.rect.x -=1
        if self.move_up and self.rect.top>0:
            self.rect.y -=1
        if self.move_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.y +=1

