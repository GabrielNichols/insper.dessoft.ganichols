import pygame
import random
import assets
from sprites import texto_init
from os import path

from config import IMG_DIR, FNT_DIR, BLACK, FPS, GAME, QUIT, WIDTH


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    texto = texto_init()
    all_sprites.add(texto)

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()

    background_rect = background.get_rect()
    

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
        
        all_sprites.update()

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
