import pygame
x = pygame.init()

#Initializing Game window
gameWindow = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Snake-Game")

#Specifying game variables
gameExit = False
gameOver = False

#game features

#Quit game method
def quiteGame(game_event):
    if game_event.type == pygame.QUIT:
        gameExit = True


#creating game loop
while not gameExit:
    for events in pygame.event.get():
        quiteGame(events)
    
pygame.quit()
quit()


+923415234310