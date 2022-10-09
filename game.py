import pygame

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.bgColor = pygame.Color('black')
        self.FPS = 120
        self.gameClock = pygame.time.Clock()
        self.closeClicked = False
        self.continueGame = True

    def play(self):
        while not self.closeClicked:
            self.handleEvents()
            self.draw()
            self.gameClock.tick(self.FPS)

    def handleEvents(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.closeClicked = True

    def draw(self):
        self.surface.fill(self.bgColor)
        pygame.display.update()

