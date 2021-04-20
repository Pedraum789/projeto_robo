import pygame
import time
pygame.init()
    
i = 0
#Posicoes
pos_x = 200
pos_y = 300

pos_x_robo = 0
pos_y_robo = 0

#velocidades
velocidade_bola = 0.2
velocidade_robo = 0.3

#Adicionando imagens no jogo
fundo = pygame.image.load ('campo.png')
bola = pygame.image.load ('bola.png')
robo = pygame.image.load('robo.png')

janela = pygame.display.set_mode((490,340))
pygame.display.set_caption("Trabalho robo")

janela_aberta = True
while janela_aberta:

    for event in pygame.event.get():
        pygame.time.delay(50)
        if event.type == pygame.QUIT:
            janela_aberta = False

    #Bola andar sozinha
    pos_y += 1
    pos_x -= 1
    
    janela.blit(fundo, (0,0))
    janela.blit(bola, (pos_y, pos_x))
    janela.blit(robo, (pos_x_robo, pos_y_robo))

    time.sleep(0.2)
    pygame.display.update()

pygame.quit()
