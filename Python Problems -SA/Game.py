import pygame
from Ship import Ship
from pygamegame import PygameGame


class Game(PygameGame):
    def init(self):
        Ship.init()
        self.shipGroup = pygame.sprite.Group(Ship(self.width, self.height))

    def timerFired(self, dt):
        self.shipGroup.update(self.isKeyPressed, self.width, self.height)

    def redrawAll(self, screen):
        self.shipGroup.draw(screen)

Game(600, 600).run()