import pygame
import random
x = pygame.init()

#Initializing Game window
width = 1024
height = 600
gameWindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake-Game")
update_game  = pygame.display.update
draw_rect = pygame.draw.rect
draw_snake = draw_rect

#Background Image
bgimg = pygame.image.load("snake.jpg")
bgimg = pygame.transform.scale(bgimg, (width, height)).convert_alpha()



#color
white = (255,255,255)
black  = (0,0,0)
red = (255,0,0)


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])




def gameStart():
    
    
    #Specifying game variables
    gameExit = False
    gameOver = False
    snake_x = 45
    snake_y = 45
    snake_size = 15
    snk_list = []
    snk_length = 1
    fps = 50
    velocity_x = 0
    velocity_y = 0
    score = 0
    food_x = random.randint(20,width/2)
    food_y = random.randint(20,height/2)
    init_velocity = 5
    

    #creating game loop
    while not gameExit:
        
        #if Game over
        if gameOver:
            gameWindow.fill(white)

            text_screen("Game Over! Press Enter To Continue", red, 140, 250)

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    gameExit = True

                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_RETURN:
                        gameStart()
        else:

            for events in pygame.event.get():
                
                # creating Quite Event
                if events.type == pygame.QUIT:
                        gameExit = True
                
                #moving snake right position
                if events.type == pygame.KEYDOWN:

                    #moving snake right position forward
                    if events.key == pygame.K_RIGHT:
                        velocity_x =  init_velocity
                        velocity_y = 0

                    #moving snake left position backward
                    if events.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    #moving snake upward position
                    if events.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    #moving snake downward position
                    if events.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0  
            #moving snake with velocity
            snake_x += velocity_x
            snake_y += velocity_y

            #Eeting food and increasing score
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=1
                
                food_x = random.randint(20, width / 2)
                food_y = random.randint(20, height / 2)
                snk_length +=5

            #updating-Window 
            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            score_sc = f"Score: {score * 10}"
            text_screen(score_sc, white, 5, 5)
            
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            #if snake collide in itself
            if head in snk_list[:-1]:
                gameOver = True    
            
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)

            #draw_snake(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            draw_rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            
            #Game over if hits with walls
            if snake_x<0 or snake_x>width or snake_y<0 or snake_y>height:
                    gameOver = True

        update_game()
        clock.tick(fps)

    pygame.quit()
    quit()

gameStart()
