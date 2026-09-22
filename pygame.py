import pygame

#initialise required modules
pygame.init()

#set up window geometry
screen = pygame.display.set_mode((400, 500))

#create a loop to run till the game is quit by the user
done = False

while not done:

    #clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()