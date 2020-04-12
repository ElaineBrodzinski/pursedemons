#!/usr/bin/env python3.8
from glob import glob
import random
import math
from itertools import count

import pygame
import pygame.image
import pygame.display
import pygame.freetype
import pygame.image
import pygame.mouse
import pygame.time
from pygame import Surface, Rect

import sprite_sheet

# Initialize pygame, so it can open a window and start listening for input.
pygame.init()

# Initialize a clock we'll use to set the framerate.
clock = pygame.time.Clock()
fps = 60

# Set up the window we'll be drawing in
window = pygame.display.set_mode([256 * 4, 256])
pygame.display.set_caption("Smells Like Spam")

# We'll run until the user asks to quit.
running = True

# We adjust these variables to control the player we draw below.
x_position = 128.0
y_position = 128.0

# The amount to change the x and y positions of the player per second.
x_speed = 0.0
y_speed = 0.0

# Load our sprite sheet.
sprites = sprite_sheet.load("assets/sprites")

# Load the player image we'll be displaying.
player_image = sprites[
    random.choice(
        [name for name in sprites if ("Ursus" in name or "Horribilis" in name)]
    )
]

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

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player_image = sprites[
                random.choice(
                    [
                        name
                        for name in sprites
                        if ("Ursus" in name or "Horribilis" in name)
                    ]
                )
            ]

        if event.type == pygame.MOUSEMOTION:
            # if you move mouse over the window, center the player on it
            x_position = event.pos[0] - player_image.get_width() / 2
            y_position = event.pos[1] - player_image.get_height() / 2

    keys = pygame.key.get_pressed()
    x_speed = 0.0
    y_speed = 0.0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x_speed -= 256.0

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x_speed += 256.0

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y_speed -= 256.0

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y_speed += 256.0

    # Update position using the speed in pixels per second),
    # divided by the number of frames per second.
    x_position += x_speed / fps
    y_position += y_speed / fps

    # Fill the background
    window.fill((0, 0, 0))

    text, dimensions = font.render("Boo!", (0, 0, 0))
    text_position = 32, 32
    window.blit(text, text_position)

    # Draw background layers
    for sprite in (sprites["Space"], sprites["Floor"], sprites["Darkness"]):
        for x in range(0, 256 * 4, sprite.get_rect().width):
            window.blit(sprite, (x, 0))

    for (x, sprite) in zip(
        count(),
        (
            sprites["Ursus 0"],
            sprites["Ursus 1"],
            sprites["Ursus 2"],
            sprites["Ursus 3"],
            sprites["Horribilis 0"],
            sprites["Horribilis 1"],
            sprites["Horribilis 2"],
            sprites["Horribilis 3"],
            sprites["Trophy 0"],
            sprites["Little Magic 0"],
            sprites["Little Magic 1"],
            sprites["Little Magic 2"],
            sprites["Lepus 8 0"],
            sprites["Lepus 8 1"],
            sprites["Lepus 8 2"],
        ),
    ):
        r = sprite.get_rect()
        r.center = (25 + x * 50, 128)
        window.blit(sprite, r)

    position = int(round(x_position)), int(round(y_position))
    window.blit(player_image, position)

    # Take the new frame we've drawn and display it.
    pygame.display.flip()

# Running is now False. Time to quit, close the window and stop listening for events.
pygame.quit()
