from matplotlib import pyplot as plt

#Primeiro Grafico
def graficos_xy(x_bola, y_bola, x_robo, y_robo):

    #Tipos de gráficos
    #print(plt.style.available)
    plt.style.use('ggplot')
    plt.axis([0, 900, 0, 600])

    #Bola
    plt.plot(x_bola, y_bola, color='b', marker='.', label='Movimento bola')
    #Robo
    plt.plot(x_robo, y_robo, color='black', marker='.', label='Movimento robo')

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.title("Posições de X e Y")

    plt.legend()
    plt.show()

#Segundo Grafico #1
def graficos_x_t(x_bola, x_robo, temp):

    plt.style.use('ggplot')

    #Bola
    plt.plot(temp, x_bola, color='blue', label='X da bola x Tempo')
    #Robo
    plt.plot(temp, x_robo, color='black', label='X do robo x Tempo')
    #Tempo

    plt.xlabel("T")
    plt.ylabel("X")

    plt.title("Posições de X e T")

    plt.legend()

    plt.show()

#Segundo Grafico #2
def graficos_y_t(y_bola, y_robo, temp):
    plt.style.use('ggplot')

    #Bola
    plt.plot(temp, y_bola, color='blue', label='Y da bola x Tempo')
    #Robo
    plt.plot(temp, y_robo, color='black', label='Y do robo x Tempo')
    #Tempo

    plt.xlabel("T")
    plt.ylabel("Y")

    plt.title("Posições de X e T")

    plt.legend()

    plt.show()

#Terceiro Grafico #1
def graficos_vx_t(vel_x_ball, vel_x_robot, temp):

    plt.style.use('ggplot')

    #Bola
    plt.plot(temp, vel_x_ball, color='blue', label='Vx bola com T')
    #Robo
    plt.plot(temp, vel_x_robot, color='black', label='Vx robo com T')

    plt.xlabel("T")
    plt.ylabel("Vx")

    plt.title("Posições de Vx e T")

    plt.legend()

    plt.show()

#Terceiro Grafico #2
def graficos_vy_t(vel_y_ball, vel_y_robot, temp):

    plt.style.use('ggplot')

    #Bola
    plt.plot(temp, vel_y_ball, color='blue', label='Vy bola com T')
    #Robo
    plt.plot(temp, vel_y_robot, color='black', label='Vy robo com T')

    plt.xlabel("T")
    plt.ylabel("Vy")

    plt.title("Posições de Vy e T")

    plt.legend()

    plt.show()

def graficos_axay_t(temp, x, show):

    plt.style.use('ggplot')


    plt.axis([0, 900, 0, 25])

    #Bola
    plt.plot(x, temp, color='k', label='ax com ay')
    #Robo
    plt.plot(x, temp, color='k', label='ax com ay')

    plt.xlabel("X")
    plt.ylabel("T")

    plt.title("Posições de X e T")

    plt.legend()

    plt.show()

def graficos_d_t(distancia, temp):

    plt.style.use('ggplot')

    #Distancia
    plt.plot(temp, distancia, color='k', label='Distancia')

    plt.xlabel("Tempo")
    plt.ylabel("Distancia")

    plt.title("Distancia em função do tempo")

    plt.legend()

    plt.show()