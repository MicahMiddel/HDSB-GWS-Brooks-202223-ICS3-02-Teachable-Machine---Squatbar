import pygame
import random

#colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (70, 70, 70)
BLUE = (0, 0 , 255)
SKY_BLUE = (0, 180, 255)
BETTER_BLUE = (0, 125, 255)
RED = (255, 0, 0)
DARK_RED = (100, 0, 0)
YELLOW = (255, 255, 0)
SAND_YELLOW = (200, 170, 85)
GREEN = (0, 100, 50)
LIGHT_GREEN = (155, 200, 0)
ORANGE = (255, 120, 0)
PURPLE = (115, 15, 185)
LIGHT_PURPLE = (120, 0, 255)

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = [1200, 686]  # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize[0], surfaceSize[1]))
    
    score = 0
    timeFont = pygame.font.SysFont('Corbel', 250, True, False)
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    
    startTicks=pygame.time.get_ticks() #starter tick

    #-----------------------------Program Variable Initialization----------------------------#
    background = pygame.image.load("background.jpg").convert()

    fatShy = pygame.image.load("ShyGuy/fat shy guy.png").convert_alpha()#fat shy guy png
    neutralShy = pygame.image.load("ShyGuy/neutral shy guy.png").convert_alpha()#neutral shy guy png
    directionShy = pygame.image.load("ShyGuy/direction shy guy1.png").convert_alpha()#direction shy guy png
    
    #gives the answer to what siman says
    answer = 'neutral'
    numAnswer = 0
    gotAnswer = False
    
    
    seconds = int((pygame.time.get_ticks()-startTicks)/1000)
    
    numAnswer = random.randint(0, 2)#randomly selects the answer


    #-----------------------------Main Program Loop---------------------------------------------#
    while True:       
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop


        #-----------------------------Program Logic---------------------------------------------#
        # Update your game objects and data structures here...
        

            

        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.blit(background, (0, 0))
        
        counter=int((pygame.time.get_ticks()-startTicks)/1000) #calculates the seconds
        timeText = timeFont.render(str(counter), True, (YELLOW)) #put those seconds into text
        
        if counter > 5:
            print(numAnswer)
            if numAnswer == 0:
                answer = 'right'
            if numAnswer == 1:
                answer == 'left'
            if numAnswer == 2:
                answer = 'leave'
        
        if answer == 'right':
            mainSurface.blit(directionShy, (400, 0))
        elif answer == 'left':
            mainSurface.blit(pygame.transform.flip(directionShy, True, False), (400, 0))#, (0, 0, 300, 199)
        elif answer == 'neutral':
            mainSurface.blit(neutralShy, (0, 0))
               
               
        
        mainSurface.blit(timeText, (800, 200)) #display the timer
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower


    pygame.quit()     # Once we leave the loop, close the window.

main()