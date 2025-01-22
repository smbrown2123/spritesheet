import pygame
from spritesheet import Spritesheet

pygame.init()

screen = pygame.display.set_mode((300,300))
pygame.display.set_caption("Spritesheet Demo")

clock = pygame.time.Clock()

black =(0, 0, 0)
bgColour = (50, 50, 50)
Image = pygame.image.load('chicken.png')
Spritesheet = Spritesheet(Image, black)
AnimationFrames = Spritesheet.get_frames(0, 2, 16, 16)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(bgColour)
    
    Spritesheet.play_animation(screen,(0,0), AnimationFrames,20)
    
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()