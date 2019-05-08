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
clock = pygame.time.Clock()
fps = 30
velocity_x = 0
velocity_y = 0



#creating game loop
while not gameExit:
    for events in pygame.event.get():
        
        # creating Quite Event
        if events.type == pygame.QUIT:
                gameExit = True
        
        #moving snake right position
        if events.type == pygame.KEYDOWN:

            #moving snake right position forward
            if events.key == pygame.K_RIGHT:
                velocity_x =  10
                velocity_y = 0

            #moving snake left position backward
            if events.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0

            #moving snake upward position
            if events.key == pygame.K_UP:
                velocity_y = -10
                velocity_x = 0

            #moving snake downward position
            if events.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0  
    
    snake_x += velocity_x
    snake_y += velocity_y

    #updating-Window 
    gameWindow.fill(white)
    draw_snake(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    update_game()
    clock.tick(fps)

pygame.quit()
quit()


