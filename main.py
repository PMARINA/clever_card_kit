import RPi.GPIO as GPIO
import SimpleMFRC522
import pygame
import math
import time
from scrollText import ScrollText
pygame.init()
reader = SimpleMFRC522.SimpleMFRC522()
BLACK = (0,0,0)
WHITE = (255,255,255)
COLOR = (0,255,0)

x =250
y = 250
def display(s):
	fontObj = pygame.font.Font("freesansbold.ttf", 30)
	textSurfaceObj = fontObj.render(s, True, WHITE, BLACK)
	textRectObj= textSurfaceObj.get_rect()
	textRectObj.center = (x,y)
	windowSurface = pygame.display.set_mode((500,500), 0, 32)
	windowSurface.blit(textSurfaceObj, textRectObj)
	pygame.display.update()
def displayer(s):
	fps = 50
	surface = pygame.display.set_mode((600,600))#,pygame.FULLSCREEN)
	pygame.init()
	spheres = (
		ScrollText(surface, s, 400, pygame.Color(255,255,0)),
                )
	mWidth, totWidth = spheres[0].retVals()
	clock = pygame.time.Clock()
	print(totWidth)
	buff = math.ceil(math.ceil(totWidth/surface.get_width())/fps)
	t = time.time()
	while time.time()>t+buff:
		clock.tick(fps)
		surface.fill((0, 0, 0, 255))
		for thing in spheres:
			thing.update()
		pygame.display.flip()
def main():
        '''
        PEACH --> LUIGI
        '''
        id, text = reader.write("Hey bae! Come to my party!! Theres cake 0")
        time.sleep(1)
        id,text = reader.write(" c u there")
        time.sleep(1)
        id,text = reader.write("hey, its been a while. lets hang out")
        time.sleep(1)
        id,text = reader.write("ur bro")
        time.sleep(1)
        #id,text = reader.write("...")
        time.sleep(1)
        try:
                while True:
                        #id,text = reader.read()
                        displayer("text")
        finally:
                GPIO.cleanup()
def debugging():
        try:
                displayer("Testing")
        finally:
                GPIO.cleanup()
        
debugging()

