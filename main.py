import pygame

def main():
    "Width and height for our pygame display"
    width = 500
    height = 400

    pygame.init()
    pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pong')
    surface = pygame.display.get_surface()
    game = Game(surface)
