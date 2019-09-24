import pygame
import sys
from plane import Plane
from bullet1 import Bullet1

class Bluesky:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200,500))
        pygame.display.set_caption('Blue Sky')
        self.bg_color=(0,0,255)
        self.plane=Plane(self)
        self.bullets=pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events_()
            self.plane.update_plane()
            self.bullets.update()
            self._remove_invalid()
            self._update_screen_()

    def _check_events_(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.plane.move_to_right = True
                elif event.key == pygame.K_LEFT:
                    self.plane.move_to_left = True
                elif event.key == pygame.K_UP:
                    self.plane.move_up = True
                elif event.key == pygame.K_DOWN:
                    self.plane.move_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.plane.move_to_right = False
                if event.key == pygame.K_LEFT:
                    self.plane.move_to_left = False
                if event.key == pygame.K_UP:
                    self.plane.move_up = False
                if event.key == pygame.K_DOWN:
                    self.plane.move_down = False

    def _update_screen_(self):
        self.screen.fill(self.bg_color)
        self.plane.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _fire_bullet(self):
        new_bullet=Bullet1(self)
        self.bullets.add(new_bullet)

    def _remove_invalid(self):
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    bs=Bluesky()
    bs.run_game()