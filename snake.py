import pygame
x = pygame.init()

#Initializing Game window
width = 768
height = 600
gameWindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake-Game")
update_game  = pygame.display.update
draw_snake = pygame.draw.rect

#color
white = (255,255,255)
black  = (0,0,0)
red = (255,0,0)

#Specifying game variables
gameExit = False
gameOver = False
snake_x = 45
snake_y = 45
snake_size = 15
clock = pygame.time.clock()
fps = 30


#creating game loop
while not gameExit:
    for events in pygame.event.get():
        
        # creating Quite Event
        if events.type == pygame.QUIT:
                gameExit = True
        
        #updating-Window color 
        gameWindow.fill(white)
        update_game()

        #drawing Snake
        draw_snake(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
        update_game()
        clock.tick(fps)
        
        #moving snake right position
        
        
    
pygame.quit()
quit()


