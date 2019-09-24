import pygame
from pygame import font
from ship import Ship
from pygame import sprite


class Scoreboard:
    '''to manage score,level,ships remained'''
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.ai_game=ai_game
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.setting1
        self.stats=ai_game.stats

        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        self.prep_score()
        self.high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        score_str=str(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        self.score_image_rect=self.score_image.get_rect()
        self.score_image_rect.right=self.screen_rect.right-20
        self.score_image_rect.y=20

    def draw_score(self):
        self.screen.blit(self.score_image,self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def high_score(self):
        high_score=round(self.stats.high_score,-1)
        high_score_str="{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.top=self.score_image_rect.top
        self.high_score_rect.centerx=self.screen_rect.centerx

    def prep_level(self):
        str_level=str(self.stats.level)
        self.level_image=self.font.render(str_level,True,self.text_color,self.settings.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.top=self.score_image_rect.bottom+20
        self.level_rect.right=self.score_image_rect.right

    def prep_ship(self):
        self.ships=pygame.sprite.Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x=10+ship.rect.width*ship_number
            ship.rect.y=10
            self.ships.add(ship)


