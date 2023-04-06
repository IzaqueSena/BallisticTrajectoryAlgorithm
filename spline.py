from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
import math

from trajetoria import calcula_posicao

# Funcao que, dado um conjunto de dados, cria o gráfico do spline correspondente
# Ideia do teste: pegar um array simples com três pontos, e criar o spline que aproxima um polinômio cubico
def criar_spline(x, y, y_compara, caso):
    spline = CubicSpline(x, y) # cria o spline 
    x_new = np.linspace(x[0], x[-1]) # cria um vetor com os mesmos extremos em x, mas com menos espaco entre os dados, com o intuito de visualizar mais pontos
    y_new = spline(x_new) # o novo vetor para y deve ser todos os pontos de x calculados utilizando o spline feito, substancialmente y_new = S(x_new), para os pontos dados
    match caso:
        case 1:
            plt.figure(figsize = (10,8))
            plt.plot(x_new, y_new, 'b', label='Interpolação polinomial') # plota o resultado do spline na cor azul
            plt.plot(x, y, 'ro', label='Dados tabelados') # plota os pontos correspondentes aos x e y anteriores
            plt.title("Interpolação polinomial para a altura do projétil")
            plt.xlabel("Tempo", labelpad=10)
            plt.ylabel("Altura", labelpad=10)
            plt.plot()
            plt.legend(loc="upper right")
            plt.savefig("spline_altura.png")
        
        case 2:
            plt.figure(figsize = (10,8))
            plt.plot(x_new, y_new, 'b', label='Interpolação polinomial para o modelo completo') # plota o resultado do spline na cor azul
            plt.plot(x, y, 'ro', label='Dados tabelados para o modelo completo') # plota os pontos correspondentes aos x e y anteriores
            plt.plot(x, y_compara, 'go', label='Dados tabelados do caso simplificado') # plota os pontos correspondentes aos x e y anteriores
            plt.title("Comparação dos modelos através de interpolação polinomial para a velocidade do projétil")
            plt.xlabel("Tempo", labelpad=10)
            plt.ylabel("Velocidade em x", labelpad=10)
            plt.plot()
            plt.legend(loc="lower left")
            plt.savefig("spline_velocidade.png")

def valores_simplificado():
    alturas_simplificado = []
    velocidadex_simplificado = []
    tempo = []
    t_0 = 0
    posicao_0 = [0, 0, 0]
    v_0 = 15
    angulos = [45, 0]
    epsilon = 0.0001
    a = [0, 0.1, 0, 0, 0, 9.8]
    y_00 = posicao_0[0]
    y_01 = posicao_0[1]
    y_02 = posicao_0[2]
    y_03 = v_0 * math.cos(math.radians(angulos[0])) * math.cos(math.radians(angulos[1]))
    y_04 = v_0 * math.cos(math.radians(angulos[0])) * math.sin(math.radians(angulos[1]))
    y_05 = v_0 * math.sin(math.radians(angulos[0]))
    y_0 = np.array([y_00, y_01, y_02, y_03, y_04, y_05])

    i = 0
    while (i == 0 or y_t[2] >= 0):
        if(i != 0): 
            t = t_0 + i * 0.1
            y_t = calcula_posicao(y_0, t_0, t, epsilon, a)
        else:
            t = t_0
            y_t = y_0
        tempo.append(t)
        alturas_simplificado.append(y_t[2])
        velocidadex_simplificado.append(y_t[3])
        i+=1

    return tempo, alturas_simplificado, velocidadex_simplificado

def valores_completo():
    tempo = []
    alturas_vento_resist = []
    velocidadex_vento_resist = []

    coef_arrasto = 0.35
    massa = 0.15
    diametro = 0.07
    massa_especifica_ar = 1.22
    vento = [-1.5, 1.5, 0]
    gama = 0.5*coef_arrasto*massa_especifica_ar*(math.pi*math.pow((diametro/2), 2))
    t_0 = 0
    posicao_0 = [0, 0, 0]
    v_0 = 15
    angulos = [45, 0]
    t = 10
    epsilon = 0.0001
    a = [gama, massa, vento[0], vento[1], vento[2], 9.806]
    y_00 = posicao_0[0]
    y_01 = posicao_0[1]
    y_02 = posicao_0[2]
    y_03 = v_0 * math.cos(math.radians(angulos[0])) * math.cos(math.radians(angulos[1]))
    y_04 = v_0 * math.cos(math.radians(angulos[0])) * math.sin(math.radians(angulos[1]))
    y_05 = v_0 * math.sin(math.radians(angulos[0]))
    y_0 = np.array([y_00, y_01, y_02, y_03, y_04, y_05])

    i = 0
    while (i == 0 or y_t[2] >= 0):
        if(i != 0): 
            t = t_0 + i * 0.1
            y_t = calcula_posicao(y_0, t_0, t, epsilon, a)
        else:
            t = t_0
            y_t = y_0
        tempo.append(t)
        alturas_vento_resist.append(y_t[2])
        velocidadex_vento_resist.append(y_t[3])
        i+=1

    return tempo, alturas_vento_resist, velocidadex_vento_resist

def main():
    t, alturas, velocidade = valores_simplificado()
    t, alturas_completo, velocidade_completo = valores_completo()
    criar_spline(t, alturas, velocidade, 1)
    criar_spline(t, velocidade_completo, velocidade, 2)

main()