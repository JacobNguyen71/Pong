import pygame
from ball import Ball
from paddle import Paddle
import random


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.bgColor = pygame.Color('black')
        self.FPS = 120
        self.gameClock = pygame.time.Clock()
        self.closeClicked = False
        self.continueGame = True

        "width and height of our surface"
        width = self.surface.get_width()
        height = self.surface.get_height()

        "game colors"
        colorWhite = 'white'

        "sizes for objects in our game"
        ballRadius = 5

        "determine the center of the screen"
        centerX = width // 2
        centerY = height // 2

        "paddle dimensions"
        boxWidth = 10
        boxHeight = 80

        "determine the position of paddle"
        leftX = width - (14 * (width // 15))
        rightX = width - width // 15
        top = height // 2 - (boxHeight // 2)

        "velocity of items in our game"
        ballVelocity = random.randint(-2, 2)
        paddleVelocity = 20
        "generate a random velocity between the two numbers"
        ballVelocity = [-ballVelocity, ballVelocity]
        self.ball = Ball(colorWhite, ballRadius, [centerX, centerY], ballVelocity, self.surface)
        self.leftPaddle = Paddle(colorWhite, leftX, top, boxWidth, boxHeight, paddleVelocity, self.surface)
        self.rightPaddle = Paddle(colorWhite, rightX, top, boxWidth, boxHeight, paddleVelocity, self.surface)
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
        self.leftPaddle.draw()
        self.rightPaddle.draw()
        pygame.display.update()

    def update(self):
        self.ball.move()
