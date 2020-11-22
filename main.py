from PIL import Image
from glitches import GlitchWrapper
import random
import pygame

def save():
    img.save("temp.png")

img = Image.open("image.jpg")
pixels = img.load() # load pixels
width, height = img.size

wrapper = GlitchWrapper(pixels, width, height)

screen = pygame.display.set_mode((width, height))

running = True

while running:
    pressed = pygame.key.get_pressed() # get pressed key
    for e in pygame.event.get(): # get all events
        if e == pygame.QUIT or pressed[pygame.K_q]: # exit program
            running = False
        if pressed[pygame.K_r]: # restart glitching
            img = Image.open("image.jpg")
            pixels = img.load()
            width, height = img.size

            wrapper = GlitchWrapper(pixels, width, height)
    
    save() # save temp picture
    new_img = pygame.image.load("temp.png") # load temp picture
    rect = new_img.get_rect(topleft=(0, 0))
    
    screen.blit(new_img, rect) # put temp picture in top left corner
    pygame.display.flip() # update screen

    wrapper.random_glitch()