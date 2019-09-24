import pygame
import sys
from setting import Setting
from ship import Ship
from bullets import Bullets
from alien import Alien
from game_stats import Gamestats
from time import sleep
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    '''overall class to manage game assets and behavior'''
    def __init__(self):
        pygame.init()
        self.setting1 = Setting()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect=self.screen.get_rect()
        pygame.display.set_caption('Alien Invasion')
        self.stats=Gamestats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button=Button(self,'PLAY')
        self.sb=Scoreboard(self)

    def run_game(self):
        while True:
            self._check_event()
            if self.stats.game_active:
                self.ship.update_ship()
                self._update_bullet()
                self._update_alien()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.move_to_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.move_to_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.move_to_right=False
                elif event.key == pygame.K_LEFT:
                    self.ship.move_to_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and self.stats.game_active == False:
            self.stats.game_active = True
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_ship()
            self.aliens.empty()
            self.bullets.empty()
            self.setting1.initialized_dynamic_setting()
            self._create_fleet()
            self.ship.recenter_ship()
            pygame.mouse.set_visible(False)

    def _update_screen(self):
        self.screen.fill(self.setting1.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.draw_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.setting1.max_valid_bullet:
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        self.bullets.update()
        self._remove_invalid_bullet()
        self._hit_alien()
        self._refill_fleet()

    def _remove_invalid_bullet(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _refill_fleet(self):
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.setting1.increase_speed()
            self.stats.level+=1
            self.sb.prep_level()

    def _hit_alien(self):
        collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += len(aliens)*self.setting1.hit_score
            self.sb.prep_score()
        if self.stats.score > self.stats.high_score:
            self.stats.high_score=self.stats.score
            self.sb.high_score()

    def _create_fleet(self):
        alien=Alien(self)
        alien.width,alien.height=alien.rect.size
        avalible_y=self.screen_rect.height-3*alien.height-self.ship.rect.height
        row_numbers=avalible_y // (2*alien.height)
        avalible_x=self.screen_rect.width-2*alien.width
        column_numbers=avalible_x // (2*alien.width)

        for row_number in range(row_numbers):
            for column_number in range(column_numbers):
                self._add_alien(row_number,column_number)

    def _add_alien(self,row_number,column_number):
        alien=Alien(self)
        alien.rect.x=alien.rect.width+2*alien.rect.width*column_number
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
        self.aliens.add(alien)

    def _check_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_direction()
            break

    def _change_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.setting1.alien_drop_speed
        self.setting1.direction*=-1

    def _update_alien(self):
        self._check_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._hit_ship()
        for alien in self.aliens:
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._hit_ship()
            break

    def _hit_ship(self):
        if self.stats.ship_left>0:
            self.stats.ship_left-=1
            self.sb.prep_ship()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.recenter_ship()
            sleep(0.5)
        else:
            self.stats.game_active=False
            pygame.mouse.set_visible(True)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

