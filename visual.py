import time
import pygame
from math import sqrt
from graphics import graficos_xy, graficos_x_t ,graficos_y_t, graficos_vx_t, graficos_vy_t, graficos_d_t

def interface_campo(temp, x, y):
    #Vetores para receber informações da posição do robo e da bola na intersecção
    view_x_bola = []
    view_y_bola = []
    view_x_robo = []
    view_y_robo = []

    #Verificar a distancia
    distancia = 10
    dist = []

    #Verificar o tempo
    tempo = []
    tempo_for3 = []

    #Contadores
    i = 0

    pygame.init()

    #Posições da bola em x e y
    x_bola = x[i]
    y_bola = 600 - y[i]

    #Posições Robo (XMAX = 900 e YMAX = 600)
    x_robo = 70
    y_robo = 50

    #Velocidades
    vel_x_bola = []
    vel_y_bola = []
    vel_x_robo = []
    vel_y_robo = []

    #Adicionando imagens no jogo
    fundo = pygame.image.load ('campo.png')
    bola = pygame.image.load ('bola.png')
    robo = pygame.image.load('robo.png')


    janela = pygame.display.set_mode((900,600))
    pygame.display.set_caption("Trabalho robo")

    janela_aberta = True
    while janela_aberta:

        for event in pygame.event.get():
            pygame.time.delay(50)
            if event.type == pygame.QUIT:
                janela_aberta = False

        if(distancia > 10):

            #Bola andar sozinha
            y_bola = y[i]
            x_bola = x[i]

            #Distancia
            distancia = sqrt((x_bola - x_robo)**2 + (y_bola - y_robo)**2)
            porcent_y = ((abs(y_robo - y_bola) * 100) / distancia) / 100
            total = 1
            porcent_x = abs(total - porcent_y)
            
            #Posição de Y
            if(y_bola > y_robo):
                y_robo += (porcent_y * 2.8)
            elif(y_bola < y_robo):
                y_robo -= (porcent_y * 2.8)

            #Posição de X
            if(x_bola > x_robo):
                x_robo += (porcent_x * 2.8)
            elif(x_bola < x_robo):
                x_robo -= (porcent_x * 2.8)

            '''
            #X e Y do robo
            y_robo += (porcent_y * 2.8)
            x_robo -= (porcent_x * 2.8)
            '''

            #Pegar distancia entre a bola e o robo / tempo
            dist.append(distancia)
            tempo.append(temp[i])

            #Pegar posição da bola
            view_x_bola.append(x_bola)
            view_y_bola.append(600 - y_bola)

            #Pegar posição do robo
            view_x_robo.append(x_robo)
            view_y_robo.append(600 - y_robo)

            if(temp[i] > 0):
                tempo_for3.append(temp[i])
                #Pegar velocidade da bola
                vel_x_bola.append(x_bola / temp[i])
                vel_y_bola.append((600 - y_bola) / temp[i])

                #Pegar velocidade do robo
                vel_x_robo.append(x_robo / temp[i])
                vel_y_robo.append(((600 - y_robo) / (temp[i] * 1000)))

        else:
            x_robo = x_bola
            y_robo = y_bola

        janela.blit(fundo, (0,0))
        janela.blit(bola, (x_bola, y_bola))
        janela.blit(robo, (x_robo, y_robo))

        time.sleep(0.02)

        if i != len(x):
            i += 1        

        pygame.display.update()

    pygame.quit()

    #Grafico 1
    graficos_xy(view_x_bola, view_y_bola, view_x_robo, view_y_robo)

    #Grafico 2
    graficos_x_t(view_x_bola, view_x_robo, tempo)
    graficos_y_t(view_y_bola, view_y_robo, tempo)

    #Grafico 3
    graficos_vx_t(vel_x_bola, vel_x_robo, tempo_for3)
    graficos_vy_t(vel_y_bola, vel_y_robo, tempo_for3)

    #Grafico 4

    #Grafico 5
    graficos_d_t(dist, tempo)