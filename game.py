import pygame

class Game:
    def _init_ (self):
        self.width - 100
        self.height - 700
        self.win = pygame.display.set_mode((self.width, self.height))

    def run(self):
        self.run - True

        while run:
            for event in pygame.event.get():
                if event.type == Game.QUIT:
                    run = False

        pygame.quit()
