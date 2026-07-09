import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Jude's Really Good, Really Fun Platformer Game")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(window, all_tiles):
    window.fill((135, 206, 235))
    
    dirt_tile = all_tiles[0] 
    grass_tile = all_tiles[1]
    crate_tile = all_tiles[15]
    
    for x in range(0, WIDTH, 16):
        window.blit(grass_tile, (x, HEIGHT - 16))
        
    window.blit(crate_tile, (300, 500))
    
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    
    base_dir = os.path.dirname(__file__)
    image_path = os.path.join(base_dir, "brackeys_platformer_assets", "sprites", "wall_tile.png")
    
    all_tiles = split_sprite_sheet(image_path, 14, 14)
    
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        draw(window, all_tiles)

if __name__ == "__main__":
    main(window)