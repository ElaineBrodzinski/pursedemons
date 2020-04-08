#!/usr/bin/env python3.8
import pygame

# Initialize pygame, so it can open a window and start listening for input.
pygame.init()

# Initialize a clock we'll use to set the framerate.
clock = pygame.time.Clock()
fps = 30

# Set up the window we'll be drawing in
window = pygame.display.set_mode([512, 512])

# We'll run until the user asks to quit.
running = True

# We adjust these variables to control the Boo we draw below.
x_position = 100.0
y_position = 200.0

# The amount to change the x and y positions of the Boo per second.
x_speed = 0.0
y_speed = 0.0

# Load the image of Boo we'll be displaying.
boo_image = pygame.image.load("boo.png").convert_alpha()

# Loop forever until we set running to False, when the user tries to exit.
while running:
    # Wait until it's time for the next frame to be drawn.
    clock.tick(fps)

    # Loop over every input or event that has happened since the last frame.
    for event in pygame.event.get():
        # If the user pressed the close button or alt+F4 or whatever, then...
        if event.type == pygame.QUIT:
            print("Exiting because the user told us to")
            running = False

        # ...otherwise, log a message about the unrecognized event in case it's useful later.
        else:
            print("An event happened that I don't recognize:", event)

    keys = pygame.key.get_pressed()
    x_speed = 0
    y_speed = 0
    if keys[pygame.K_LEFT]:
        x_speed -= 50
    if keys[pygame.K_RIGHT]:
        x_speed += 50
    if keys[pygame.K_UP]:
        y_speed -= 50
    if keys[pygame.K_DOWN]:
        y_speed += 50
    # note that this is "if" instead of "elif", because multiple can happen at the same time,
    # one doesn't exclude the following ones, like it did when we were looking at a single key
    # event at the same time.

    # Update position using the speed (per second), divided by the number of frames per second.
    x_position += x_speed / fps
    y_position += y_speed / fps

    # Fill the background with white, overwriting the previous frame.
    window.fill((255, 255, 255))

    # Draw a Boo with the current position, color, and size.
    position = int(round(x_position)), int(round(y_position))
    window.blit(boo_image, position)

    # Take the new frame we've drawn and display it.
    pygame.display.flip()

# Running is now False. Time to quit, close the window and stop listening for events.
pygame.quit()
