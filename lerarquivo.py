from visual import interface_campo

def criando_vetores():

    tudo = open("tudo.txt", "r")

    separa = []
    temp_original = []
    x = []
    y = []
    show = []

    #adicionando o arquivo txt no vetor separa.
    for i in tudo.readlines():
        Adicionar = i.split()
        separa.append(Adicionar)

    #separando os dados posicao x, y e tempo.
    for i in range(0, len(separa)):
        temp_original.append(separa[i][0])
        x.append(separa[i][1])
        y.append(separa[i][2])
        show.append(separa[i][2])


    #Deixando as listas com valores tipo float
    for i in range(0, len(temp_original), 1):
        temp_original[i] = temp_original[i].replace(",",".")
        temp_original[i] = float(temp_original[i])

    ##Utilizar no pygame
    for i in range(0, len(x), 1):
        x[i] = x[i].replace(",",".")
        x[i] = (float(x[i]) * 10)
    
    #Utilizar no pygame
    for i in range(0, len(y), 1):
        y[i] = y[i].replace(",",".")
        y[i] = 600 - (float(y[i]) * 10)

    #Mostrar no grafico
    for i in range(0, len(show), 1):
        show[i] = show[i].replace(",",".")
        show[i] = (float(show[i]) * 10)
    
    interface_campo(temp_original, x, y)
    


#funcao principal
def main():
    criando_vetores()

main()