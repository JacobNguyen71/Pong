import pygame
from game import Game

def main():
    "Width and height for our pygame display"
    width = 500
    height = 400

    pygame.init()
    pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pong')
    surface = pygame.display.get_surface()
    game = Game(surface)
    game.play()
    pygame.quit()

main()