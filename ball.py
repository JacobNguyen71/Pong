import pygame.draw


class Ball:
    def __init__(self, color, radius, center, velocity, surface):
        self.color = color
        self.radius = radius
        self.center = center
        self.velocity = velocity
        self.surface = surface

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius