import RPi.GPIO as GPIO
import SimpleMFRC522
import pygame
import time
pygame.init()
reader = SimpleMFRC522.SimpleMFRC522()
'''
PEACH --> LUIGI
'''
id, text = reader.write("Hey bae! Come to my party!! There's cake 0")
time.sleep(1)
id,text = reader.write("...          c u there")
time.sleep(1)
id,text = reader.write("hey, it's been a while. let's hang out")
time.sleep(1)
id,text = reader.write("ur bro")
time.sleep(1)
id,text = reader.write("...")
time.sleep(1)
x = 50
y = 50
def display(s):
	fontObj = pygame.font.Font("freesandbold.ttf", 10)
	textSurfaceObj = fontObj.render(s, True, pygame.BLACK, pygame.WHITE)
	textRectObj.get_rect()
	textRectObj.center = (x,y)
	windowSurface = pygame.display.set_mode((500,500), 0, 32)
	windowSurface.blit(textSurfaceObj, textRectObj)
try:
	while True:
		id,text = reader.read()
		display(text)
finally:
	GPIO.cleanup()



