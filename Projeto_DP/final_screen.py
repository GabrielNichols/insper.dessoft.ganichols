import pygame
import random
import assets
from os import path

from config import IMG_DIR, FNT_DIR, BLACK, FPS, GAME, QUIT, WIDTH

def final_screen(screen,score):
    
    clock = pygame.time.Clock()
    background = pygame.image.load(path.join(IMG_DIR, 'final.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = 2
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    state = 1
                    running = False
                    

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state