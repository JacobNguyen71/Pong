import pygame

class Paddle:
    def __init__(self, color, rectX, rectY, rectW, rectH, velocity, surface):
        self.color = color
        self.rectX = rectX
        self.rectY = rectY
        self.rectW = rectW
        self.rectH = rectH
        self.velocity = velocity
        self.surface = surface
        self.rect = pygame.Rect(self.rectX, self.rectY, self.rectW, self.rectH)


    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def getRect(self):
        return self.rect

    def move(self, direction):
        if direction == 'up':
            self.rect.top -= self.velocity
        if direction == 'down':
            self.rect.top += self.velocity
        while self.rect.top > 320:
            self.rect.top = self.rect.top - self.velocity
        while self.rect.top < 0:
            self.rect.top = self.rect.top + self.velocity
