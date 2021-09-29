import pygame
import os

class Game:
    def _init_ (self):
        self.width - 100
        self.height - 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives =10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))

    def run(self):
        run - True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == Game.QUIT:
                    run = False

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
