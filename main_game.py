# import the pygame module, so you can use it
import pygame

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()





def button(button_text,x,y,width,height,inactive,active, action = None): #function that makes buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active,(x,y,width,height))

        if click[0] == 1 and action != None:
            gameDisplay.fill((0,0,0))
            action() 
    else:
        pygame.draw.rect(gameDisplay, inactive,(x,y,width,height))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(button_text, smallText)
    textRect.center = ( (x+(width/2)), (y+(height/2)) )
    gameDisplay.blit(textSurf, textRect)


# define a main function

 
    # define a variable to control the main loop

def main_menu():
    running = True

     
    # main loop
    while running:
        button("PLAY", 450, 400, 100, 50, (100, 100, 100), (200, 200, 200), game_loop)
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            pygame.display.update()
            #if event.type == pygame.k
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pygame.quit()
                quit()


def game_loop():
    running = True

    while running:
        
        for event in pygame.event.get():
            pygame.display.update()
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pygame.quit()
                quit()  
        button("VOIDWEAVER", 20, 200, 200, 50, (100, 100, 100), (200, 200, 200))
        button("WEAPONMASTER", 20, 250, 200, 50, (100, 100, 100), (200, 200, 200))
        button("TRICKSTER", 20, 300, 200, 50, (100, 100, 100), (200, 200, 200))    
        pygame.display.update()

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
pygame.init()
     
    # initialize the pygame module


gameDisplay = pygame.display.set_mode((1000,800))
main_menu()