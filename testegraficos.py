from matplotlib import pyplot as plt

eixoxt= 20
eixoyv = 10
temp = 0

plt.style.use('ggplot')
#Tipos de gráficos
#print(plt.style.available)


#criando o gráfico com as listas do arquivo lerarquivo
plt.plot(eixoxt, eixoyv, color='b', marker='.', label='Velocidade ')

plt.plot(eixoxt, temp, color='k', label='Velocidade robo')

plt.plot(eixoyv, temp, color='y', label='Velocidade bola')

plt.xlabel("Tempo")
plt.ylabel("Velocidade")

plt.title("Velocidade do robô e da bola")

plt.legend()

plt.show()