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
        self.colorWhite = 'white'

        "game font size"
        self.fontSize = 36

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
        self.ball = Ball(self.colorWhite, ballRadius, [centerX, centerY], ballVelocity, self.surface)
        self.leftPaddle = Paddle(self.colorWhite, leftX, top, boxWidth, boxHeight, paddleVelocity, self.surface)
        self.rightPaddle = Paddle(self.colorWhite, rightX, top, boxWidth, boxHeight, paddleVelocity, self.surface)
        self.player_one_score = 0
        self.player_two_score = 0

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.leftPaddle.move('up')
                if event.key == pygame.K_a:
                    self.leftPaddle.move('down')
                if event.key == pygame.K_p:
                    self.rightPaddle.move('up')
                if event.key == pygame.K_l:
                    self.rightPaddle.move('down')

    def draw(self):
        self.surface.fill(self.bgColor)
        self.ball.draw()
        self.leftPaddle.draw()
        self.rightPaddle.draw()
        self.draw_score_1()
        self.draw_score_2()
        pygame.display.update()

    def update(self):
        end_score = 10
        self.ball.move()
        if self.leftPaddle.getRect().collidepoint(self.ball.getCenter()) or self.rightPaddle.getRect().collidepoint(
                self.ball.getCenter()):
            self.ball.reverseVelocity()
        if self.ball.center[0] > self.surface.get_width() - 5:
            self.player_two_score += 1
        if self.ball.center[0] < 5:
            self.player_one_score +=1
        if self.player_one_score == end_score or self.player_two_score == end_score:
            self.continue_game = False

    def draw_score_1(self):
        test_string = str(self.player_one_score)
        font = pygame.font.SysFont('', self.fontSize)
        image = font.render(test_string, True, self.colorWhite)
        text_position = (self.surface.get_width() - image.get_width(), 0)
        self.surface.blit(image, text_position)

    def draw_score_2(self):
        test_string = str(self.player_two_score)
        font = pygame.font.SysFont('', self.fontSize)
        image = font.render(test_string, True, self.colorWhite)
        text_position = (0, 0)
        self.surface.blit(image, text_position)