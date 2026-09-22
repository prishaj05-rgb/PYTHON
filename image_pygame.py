#import important libraries
import pygame
pygame.init()
white = (255, 255, 255)

#clock
clock = pygame.time.Clock()

#creating the display surface object
# of specific dimension..e (x.y)
display_surface = pygame.display.set_mode((500,500))

#set the pygame window name
pygame.display.set_caption('Image')

#creating a surface object, image is drawn on it.
image = pygame.image.load('turtle.jpg')

#set the size for image
default_image_size = (200, 200)

#scale image to the desired size
image = pygame.transform.scale(image, default_image_size)

#set default position for image
default_image_position = (150, 150)

#infinate loop
while True:
    display_surface.fill(white)
    display_surface.blit(image, default_image_position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            quit()

    pygame.display.flip()
    clock.tick(30)