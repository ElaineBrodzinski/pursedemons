#!/usr/bin/env python
# Simple pygame program

# Import and initialize the pygame library
import pygame




pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([512, 512])

# our_image = pygame.image.load('an_image.png').convert_alpha()


# Run until the user asks to quite
running = True

red_value = 125
green_value = 125
blue_value = 125
x_axis = 100
y_axis = 100
size_value = 100

clock = pygame.time.Clock()
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

    # keys = pygame.key.get_pressed()

    clock.tick(30)

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # you don't need the {...}
    pygame.draw.circle(screen, (red_value, green_value, blue_value), (x_axis, y_axis), size_value)

    x_axis += 1

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()





    #pygame.draw.circle(screen, ({red_value}, {green_value}, {blue_value}), ({x_axis}, {y_axis}), {size_value})
    #this is amounts of red, blue, and yellow isn't it. probably in the order of red / yellow / blue
    #since 100 / 100 gives me purple.
    #100 gives me dark crimson red. I want lighter though.
    #higher numbers gives me lighter, lower darker. interesting.
    #aha 200 gives me what I want. 
    #oh interesting! I've heard of RGB before. So middle is green. I think i've heard about bs with yellow
    #and PCs before. So I'd need to do probably...hmm, not sure how I'd get to yellow. Probably fuck with it.
    #pretty sure I'm right about the third being blue tho.
    #yea i am
    #self challenge time - achieve yellow
    #175, 150, 50 gives me a dark pee yellow color. I want bright yellow though, like primary school yellow
    #225, 175, 75 is like a yellow orange mix.
    #225, 175, 100 is like a light orange.
    #225, 175, 25 is closer! Lighter yellow.
    #250, 175, 0 is too close to just an orange color even though it's brighter.
    #250, 250, 0 gives my bright yellow. Excellent.
