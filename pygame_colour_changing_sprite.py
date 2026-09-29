import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Colour Changing Sprite")

    #mapping colour names to RGB values
    colours = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white'),

    }
    current_colour = colours['white']

    x,y = 30,30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3


        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        #change colour based on boundry
        if x == 0:
            current_colour = colours['red']
        elif x == screen_width - sprite_width:
            current_colour = colours['green']
        elif y == 0:
            current_colour = colours['blue']
        elif y == screen_height - sprite_height:
            current_colour = colours['yellow']
        else:
            current_colour = colours['white']
    