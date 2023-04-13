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
            plt.plot(x_new, y_new, 'r', label='Interpolação polinomial para o modelo completo') # plota o resultado do spline na cor azul
            plt.plot(x, y, 'ro', label='Dados tabelados para o modelo completo') # plota os pontos correspondentes aos x e y anteriores
            plt.plot(x, y_compara, 'go', label='Dados tabelados do caso simplificado') # plota os pontos correspondentes aos x e y anteriores
            plt.title("Comparação dos modelos através de interpolação polinomial para a velocidade no eixo x do projétil")
            plt.xlabel("Tempo", labelpad=10)
            plt.ylabel("Velocidade em x", labelpad=10)
            plt.plot()
            plt.legend(loc="lower left")
            plt.savefig("spline_velocidade.png")

def spline_eixos(t, x_simples, x_completo, y_simples, y_completo, z_simples, z_completo):
    x_simples_spline = CubicSpline(t, x_simples) # cria o spline
    y_simples_spline = CubicSpline(t, y_simples) # cria o spline 
    z_simples_spline = CubicSpline(t, z_simples) # cria o spline
    x_completo_spline = CubicSpline(t, x_completo) # cria o spline
    y_completo_spline = CubicSpline(t, y_completo) # cria o spline 
    z_completo_spline = CubicSpline(t, z_completo) # cria o spline
    t_new = np.linspace(t[0], t[-1]) # cria um vetor com os mesmos extremos em x, mas com menos espaco entre os dados, com o intuito de visualizar mais pontos


    x_simples_new = x_simples_spline(t_new) # o novo vetor para y deve ser todos os pontos de x calculados utilizando o spline feito, substancialmente y_new = S(x_new), para os pontos dados
    y_simples_new = y_simples_spline(t_new)
    z_simples_new = z_simples_spline(t_new)

    x_completo_new = x_completo_spline(t_new)
    y_completo_new = y_completo_spline(t_new)
    z_completo_new = z_completo_spline(t_new)

    plt.figure(figsize = (10,8))
    plt.plot(t_new, x_completo_new, 'r', label='Interpolação polinomial para o modelo completo') # plota o resultado do spline na cor azul
    plt.plot(t, x_completo, 'ro', label='Dados tabelados para o modelo completo') # plota os pontos correspondentes aos x e y anteriores
    plt.plot(t, x_simples, 'go', label='Dados tabelados do caso simplificado') # plota os pontos correspondentes aos x e y anteriores
    plt.plot(t_new, x_simples_new, 'g', label='Interpolação polinomial para o modelo simplificado') # plota o resultado do spline na cor azul
    plt.title("Comparação dos modelos através de interpolação polinomial para a posição do projétil em x")
    plt.xlabel("Tempo", labelpad=10)
    plt.ylabel("Posição em x", labelpad=10)
    plt.plot()
    plt.legend(loc="upper left")
    plt.savefig("spline_x.png")

    plt.figure(figsize = (10,8))
    plt.plot(t_new, y_completo_new, 'r', label='Interpolação polinomial para o modelo completo') # plota o resultado do spline na cor azul
    plt.plot(t, y_completo, 'ro', label='Dados tabelados para o modelo completo') # plota os pontos correspondentes aos x e y anteriores
    plt.plot(t, y_simples, 'go', label='Dados tabelados do caso simplificado') # plota os pontos correspondentes aos x e y anteriores
    plt.plot(t_new, y_simples_new, 'g', label='Interpolação polinomial para o modelo simplificado') # plota o resultado do spline na cor azul
    plt.title("Comparação dos modelos através de interpolação polinomial para a posição do projétil em y")
    plt.xlabel("Tempo", labelpad=10)
    plt.ylabel("Posição em y", labelpad=10)
    plt.plot()
    plt.legend(loc="upper left")
    plt.savefig("spline_y.png")

    plt.figure(figsize = (10,8))
    plt.plot(t_new, z_completo_new, 'r', label='Interpolação polinomial para o modelo completo') # plota o resultado do spline na cor azul
    plt.plot(t, z_completo, 'ro', label='Dados tabelados para o modelo completo') # plota os pontos correspondentes aos x e y anteriores
    plt.plot(t, z_simples, 'go', label='Dados tabelados do caso simplificado') # plota os pontos correspondentes aos x e y anteriores
    plt.plot(t_new, z_simples_new, 'g', label='Interpolação polinomial para o modelo simplificado') # plota o resultado do spline na cor azul
    plt.title("Comparação dos modelos através de interpolação polinomial para a posição do projétil em z")
    plt.xlabel("Tempo", labelpad=10)
    plt.ylabel("Posição em z", labelpad=10)
    plt.plot()
    plt.legend(loc="lower center")
    plt.savefig("spline_z.png")

def valores_simplificado():
    x_simplificado = []
    y_simplificado = []
    z_simplificado = []
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
        x_simplificado.append(y_t[0])
        y_simplificado.append(y_t[1])
        z_simplificado.append(y_t[2])
        velocidadex_simplificado.append(y_t[3])
        i+=1

    tempo.pop()
    x_simplificado.pop()
    y_simplificado.pop()
    z_simplificado.pop()
    velocidadex_simplificado.pop()
    return tempo, x_simplificado, y_simplificado, z_simplificado, velocidadex_simplificado

def valores_completo():
    tempo = []
    x_vento_resist = []
    y_vento_resist = []
    z_vento_resist = []
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
        x_vento_resist.append(y_t[0])
        y_vento_resist.append(y_t[1])
        z_vento_resist.append(y_t[2])
        velocidadex_vento_resist.append(y_t[3])
        i+=1

    tempo.pop()
    x_vento_resist.pop()
    y_vento_resist.pop()
    z_vento_resist.pop()
    velocidadex_vento_resist.pop()
    return tempo, x_vento_resist, y_vento_resist, z_vento_resist, velocidadex_vento_resist

def main():
    t, x_simples, y_simples, z_simples, velocidade = valores_simplificado()
    t, x_completo, y_completo, z_completo, velocidade_completo = valores_completo()
    # criar_spline(t, x, y, velocidade, 1)
    print(z_simples)
    criar_spline(t, velocidade_completo, velocidade, 2)
    spline_eixos(t, x_simples, x_completo, y_simples, y_completo, z_simples, z_completo)

main()