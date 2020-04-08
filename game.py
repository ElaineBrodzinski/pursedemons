#!/usr/bin/env python3.8
import pygame
import pygame.display
import pygame.freetype
import pygame.image
import pygame.mouse
import pygame.time

# Initialize pygame, so it can open a window and start listening for input.
pygame.init()

# Initialize a clock we'll use to set the framerate.
clock = pygame.time.Clock()
fps = 60

# Set up the window we'll be drawing in
window = pygame.display.set_mode([768, 512])
pygame.display.set_caption("Boo!")

# We'll run until the user asks to quit.
running = True

# We adjust these variables to control the Boo we draw below.
x_position = 128.0
y_position = 256.0

# The amount to change the x and y positions of the Boo per second.
x_speed = 0.0
y_speed = 0.0

# Load the image of Boo we'll be displaying.
boo_image = pygame.image.load("assets/boo.png").convert_alpha()

# Load the font we'll use for text.
font = pygame.freetype.SysFont(pygame.font.get_default_font(), 32)

# Loop forever until we set running to False, when the user tries to exit.
while running:
    # Wait until it's time for the next frame to be drawn.
    clock.tick(fps)

    # Loop over every input or event that has happened since the last frame.
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            print("Exiting because the user told us to.")
            running = False
            break  # immediately jump out of loop

        if event.type == pygame.MOUSEMOTION:
            # if you move mouse over the window, center Boo on it
            x_position = event.pos[0] - boo_image.get_width() / 2
            y_position = event.pos[1] - boo_image.get_height() / 2

    keys = pygame.key.get_pressed()
    x_speed = 0.0
    y_speed = 0.0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x_speed -= 256

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x_speed += 256

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y_speed -= 256

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y_speed += 256

    # Update position using the speed in pixels per second),
    # divided by the number of frames per second.
    x_position += x_speed / fps
    y_position += y_speed / fps

    # Fill the background, overwriting the previous frame.
    if pygame.mouse.get_focused():
        # white if mouse is over window
        background_color = 255, 255, 255
    else:
        # slightly grey if not
        background_color = 225, 225, 255
    window.fill(background_color)

    text, dimensions = font.render("Boo!", (0, 0, 0))
    text_position = 32, 32
    window.blit(text, text_position)

    # Draw a Boo with the current position, color, and size.
    position = int(round(x_position)), int(round(y_position))
    window.blit(boo_image, position)

    # Take the new frame we've drawn and display it.
    pygame.display.flip()

# Running is now False. Time to quit, close the window and stop listening for events.
pygame.quit()
