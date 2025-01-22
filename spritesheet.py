import pygame 
import consts

# class used to extract and play animations from a spritesheet 
class Spritesheet():
    def __init__(self, image, colour):
        self.sheet = image 
        self.colour = colour 
        self.scale = consts.SPRITE_SCALE
        self.frameCounter = 0 
        self.animationCounter = 0 
        self.startUpCounter = 0 

    # extracts a single frame from a spritesheet, flipping vertically or horizontally if necessary
    def get_frame(self, frame_x, frame_y, width, height, flip_x, flip_y):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet, consts.ORIGIN, ((frame_x * width), (frame_y * height), width, height))
        image = pygame.transform.scale(image, (width * self.scale, height * self.scale))
        if flip_x or flip_y:
            image = pygame.transform.flip(image, flip_x, flip_y)
        image.set_colorkey(self.colour)
    
        return image

    # retruns a series of frames as a list
    def get_frames(self, frameHeight, framesLength, width, height, flipX = 0, flipY = 0):
        frames = []
        for i in range(framesLength):
            frame = self.get_frame(i, frameHeight, width, height, flipX, flipY)
            frames.append(frame)
        return frames

    # blits a list of frames to a given surface as an animation, animationTimer controls the speed, startUpPause can be used to insert a delay before the animation plays again
    def play_animation(self, screen, pos, frames, animationTimer, startUpPause = 0):
        screen.blit(frames[self.frameCounter], pos)
        self.startUpCounter  += 1
        if self.startUpCounter >= startUpPause:
            self.animationCounter += 1
            if self.animationCounter >= animationTimer:
                self.frameCounter += 1
                self.animationCounter = 0
            if self.frameCounter >= len(frames):
                self.frameCounter  = 0
                self.startUpCounter = 0
