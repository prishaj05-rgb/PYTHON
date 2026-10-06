import pygame
import random

#initialise pygame
pygame.init()

# custom event IDs for colour changing events
SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 2

#define basic colours using pygame.color
#background colour
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

#sprite colours
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):


#constructor method
    def _init_(self, color, height, width):
        #call to the parent class (Sprite) contructor
        super()._init_()
        #create sprites surface with dimension and colour
        self.image = pygame.Surface(width,height)
        self.image.fill (color)
        #get the sprites rect defining its position and size
        self.rect = self.image.get.rect()
        #set initial velocity with random directions
        self.velocity = [random.choice([-1,1])], random.choice([-1,1])

    #method to update the sprites position
    def update(self):
        #move sprite by its velocity
        self.rect.move_ip(self.velocity)
        #flag to track if the sprite hits boundary
        boundary_hit = False
        #check for collision with left or right boundaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >=500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        #check for collision with top or bottom boundaries and reverse direction
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        #if a boundary was hit post events to change colour
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE_EVENT))

        #mehthod to change the sprites colour
    def change_color(self):
        self.image.fill(random.choice[YELLOW, MAGENTA, ORANGE, WHITE])

#change background
def change_background_color():
    