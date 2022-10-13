import pygame
from ball import Ball
import random

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.bgColor = pygame.Color('black')
        self.FPS = 120
        self.gameClock = pygame.time.Clock()
        self.closeClicked = False
        self.continueGame = True

        "Width and height of our surface"
        width = self.surface.get_width()
        height = self.surface.get_height()

        "Game colors"
        colorWhite = 'white'

        "sizes for objects in our game"
        ballRadius = 5

        "Determine the center of the screen"
        centerX = width//2
        centerY = height//2

        "Generate a random velocity between the two numbers"
        ballVelocity = [-5, 5]
        self.ball = Ball(colorWhite, ballRadius, [centerX, centerY], ballVelocity, self.surface)

    def play(self):
        while not self.closeClicked:
            self.handleEvents()
            self.draw()
            if self.continueGame:
                self.update()
            self.gameClock.tick(self.FPS)

    def handleEvents(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.closeClicked = True

    def draw(self):
        self.surface.fill(self.bgColor)
        self.ball.draw()
        pygame.display.update()

    def update(self):
        self.ball.move()

