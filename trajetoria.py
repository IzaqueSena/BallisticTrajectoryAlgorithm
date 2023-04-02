from metodos_numericos import trapezio_ponto_fixo
from funcoes import f
import math
import numpy as np

'''
Funcao que calcula posicao x, y, z e velocidade vx, vy, vz em um instante t de um projetil balistico

Parametros:
y_0: valores iniciais
y_0[0] = x0, y_0[1] = y0, y_0[2] = z0, y_0[3] = vx0, y_0[4] = vy0, y_0[5] = vz0
t_0: instante inicial
t: instante desejado
epsilon: precisao
a: parametros constantes
a[0]: gama, a[1]: massa m, a[2]: velocidade vento x, a[3]: velocidade vento y, a[4]: velocidade vento z, a[5]: gravidade
'''
def calcula_posicao(y_0, t_0, t, epsilon, a):
    n = int( (t - t_0)/(math.sqrt(epsilon)) )
    y_t = trapezio_ponto_fixo(n, t_0, t, y_0, f, 3, a)
    return y_t


'''
Funcao que exibe trajetoria x, y, z e velocidade vx, vy, vz em 11 pontos no intervalo de tempo t_0, t 
dada sua posição inicial em coordenadas polares e constantes do ambiente

Parametros:
t_0: instante inicial
posicao_0: posicoes iniciais
posicao_0[0] = x0, posicao_0[1] = y0, posicao_0[2] = z0
v_0: modulo da velocidade inicial
angulos: direção do vetor de velocidade inicial
angulos[0]: angulo alfa, posicao angular vertical da velocidade inicial  
angulos[1]: angulo beta, posição angular da velocidade inicial no plano xy
t: instante desejado
epsilon: precisao
a: parametros constantes
a[0]: gama, a[1]: massa m, a[2]: velocidade vento x, a[3]: velocidade vento y, a[4]: velocidade vento z, a[5]: gravidade
'''
def exibe_trajetoria(t_0, posicao_0, v_0, angulos, t, epsilon, a):
    # y_0: condicoes iniciais
    # y_0[0]: x0, y_0[1]: y0, y_0[2]: z0, y_0[3]: vx0, y_0[4]: vy0, y_0[5]: vz0
    y_00 = posicao_0[0]
    y_01 = posicao_0[1]
    y_02 = posicao_0[2]
    y_03 = v_0 * math.cos(math.radians(angulos[0])) * math.cos(math.radians(angulos[1]))
    y_04 = v_0 * math.cos(math.radians(angulos[0])) * math.sin(math.radians(angulos[1]))
    y_05 = v_0 * math.sin(math.radians(angulos[0]))
    y_0 = np.array([y_00, y_01, y_02, y_03, y_04, y_05])

    print('t     x     y     z     vx    vy    vz   ')
    i = 0
    while (i == 0 or y_t[2] >= 0):
        if(i != 0): 
            t_n = t_0 + i*0.1
            n = int( (t_n - t_0)/(math.sqrt(epsilon)) )
            y_t = trapezio_ponto_fixo(n, t_0, t_n, y_0, f, 3, a)
        else:
            t_n = 0
            y_t = y_0
        print("{:.2f}  {:.2f}  {:.2f}  {:.2f}  {:.2f}  {:.2f}  {:.2f}".format(t_n, y_t[0], y_t[1], y_t[2], y_t[3], y_t[4], y_t[5]))
        i += 1

def main():
    # teste
    t_0 = 0
    posicao_0 = [0, 0, 0]
    v_0 = 15
    angulos = [45, 0]
    t = 10
    epsilon = 0.01
    a = [0, 0.1, 0, 0, 0, 9.8]

    exibe_trajetoria(t_0, posicao_0, v_0, angulos, t, epsilon, a)

main()