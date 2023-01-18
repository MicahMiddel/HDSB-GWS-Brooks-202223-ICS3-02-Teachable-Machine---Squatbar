import pygame
import random

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = [1200, 686]  # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize[0], surfaceSize[1]))

    #-----------------------------Program Variable Initialization----------------------------#
    background = pygame.image.load("background.jpg").convert()

    fatShy = pygame.image.load("ShyGuy/fat shy guy.png").convert_alpha()#fat shy guy png
    neutralShy = pygame.image.load("ShyGuy/neutral shy guy.png").convert_alpha()#neutral shy guy png
    directionShy = pygame.image.load("ShyGuy/direction shy guy1.png").convert_alpha()#direction shy guy png
    
    #gives the answer to what siman says
    answer = 'neutral'
    numAnswer = 0
    shyAnswer = ['right', 'left', 'leave']
    gotAnswer = False
    
    counter = 0


    #-----------------------------Main Program Loop---------------------------------------------#
    while True:       
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop


        #-----------------------------Program Logic---------------------------------------------#
        # Update your game objects and data structures here...
        counter += 1
        
        while counter >= 10:
            if gotAnswer == False:
                numAnswer = random.randint(0, 1)#randomly selects the answer
                if numAnswer == 0:
                    answer = shyAnswer[0]
                if numAnswer == 1:
                    answer = shyAnswer[1]
                if numAnswer == 2:
                    answer = shyAnswer[2]
                gotAnswer = True

        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.blit(background, (0, 0))
        
        if answer == shyAnswer[0]:
            mainSurface.blit(directionShy, (400, 0))
        elif answer == shyAnswer[0]:
            mainSurface.blit(pygame.transform.flip(directionShy, True, False), (400, 0))#, (0, 0, 300, 199)
        else:
            mainSurface.blit(neutralShy, (0, 0))
               
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        clock.tick(60) #Force frame rate to be slower


    pygame.quit()     # Once we leave the loop, close the window.

main()