from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

from trajetoria import calcula_posicao

# Funcao que, dado um conjunto de dados, cria o gráfico do spline correspondente
# Ideia do teste: pegar um array simples com três pontos, e criar o spline que aproxima um polinômio cubico
def criar_spline(x, y):
    spline = CubicSpline(x, y) # cria o spline 
    x_new = np.linspace(x[0], x[-1], (x[1] - x[0]) * 100) # cria um vetor com os mesmos extremos em x, mas com menos espaco entre os dados, com o intuito de visualizar mais pontos
    y_new = spline(x_new) # o novo vetor para y deve ser todos os pontos de x calculados utilizando o spline feito, substancialmente y_new = S(x_new), para os pontos dados

    plt.figure(figsize = (10,8))
    plt.plot(x_new, y_new, 'b') # plota o resultado do spline na cor azul
    plt.plot(x, y, 'ro') # plota os pontos correspondentes aos x e y anteriores
    plt.savefig("spline.png")

def main():
    x = [0, 1, 2]
    y = [1, 3, 2]
    criar_spline(x, y)

main()