import pygame
x = pygame.init()

#Initializing Game window
gameWindow = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Snake-Game")

#Specifying game variables
gameExit = False
gameOver = False
