import time
import pygame
import os

set_min = int(input('Введите количество минут: '))
secund = set_min * 60


while secund != 0:
    secund -= 1  # every iteration minus 1 second
    print(time.strftime("Осталось: %M:%S", time.localtime(secund)))
    time.sleep(1)  # 1 second delay
    os.system('CLS')  # clear console
    
print('time =)')

# cycle was complete, play music
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('media/daddy_cool.mp3')  # source music
pygame.mixer.music.play()  # launch
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
