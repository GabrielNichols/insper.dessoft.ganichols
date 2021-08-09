import pygame
import random
import assets
from os import path

from config import IMG_DIR, FNT_DIR, BLACK, FPS, GAME, QUIT, WIDTH


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()
    botao_iniciar = pygame.font.Font(path.join(FNT_DIR, 'inicial.ttf'), 28)
    background_rect = background.get_rect()
    
    text_surface = botao_iniciar.render('Pressione qualquer tecla', True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect = (45, 450)
    

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

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        screen.blit(text_surface, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
