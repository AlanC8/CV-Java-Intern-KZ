import pygame
from pygame import mixer

mixer.init()
pygame.init()
screen = pygame.display.set_mode((600,600))
mixer.music.load('Playlist/1.mp3')
mixer.music.play()
play = True
k = 1
clock = pygame.time.Clock()

while True:
    screen.fill((0,0,0))
    screen.blit(pygame.image.load('Playlist/player.png'), (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if play == True:
               mixer.music.pause()
            elif play == False:
               mixer.music.unpause()
            play = not play
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            mixer.music.stop()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if k == 3:
                k = 1
            else:
                k += 1
            mixer.music.load(f'Playlist/{k}.mp3')
            mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if k == 1:
                k = 3
            else:
                k -= 1
            mixer.music.load(f'Playlist/{k}.mp3')
            mixer.music.play()
    
    pygame.display.flip()
    clock.tick(60)
            


