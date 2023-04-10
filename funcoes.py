import numpy as np
import math

'''
Função f da modelagem matematica do problema de determinação da trajetória balística

Parametros:
t: instante
y: vetor Y do problema de cauchy que modela o problema
y[0]: posicao x, y[1]: posicao y, y[2]: posicao z, y[3]: velocidade x, y[4]: velocidade y, y[5]: velocidade z
a: vetor de parametros constantes da função f
a[0]: gama, a[1]: massa m, a[2]: velocidade vento x, a[3]: velocidade vento y, a[4]: velocidade vento z, a[5]: gravidade
'''
def f(t, y, a):
    f_1 = y[3]
    f_2 = y[4]
    f_3 = y[5]
    f_4 = -(a[0]/a[1]) * (y[3] - a[2]) * math.sqrt(math.pow((y[3]-a[2]), 2) + math.pow((y[4]-a[3]), 2) + math.pow((y[5]-a[4]), 2))
    f_5 = -(a[0]/a[1]) * (y[4] - a[3]) * math.sqrt(math.pow((y[3]-a[2]), 2) + math.pow((y[4]-a[3]), 2) + math.pow((y[5]-a[4]), 2))
    f_6 = -(a[0]/a[1]) * (y[5] - a[4]) * math.sqrt(math.pow((y[3]-a[2]), 2) + math.pow((y[4]-a[3]), 2) + math.pow((y[5]-a[4]), 2)) - a[5]
    f = np.array([f_1, f_2, f_3, f_4, f_5, f_6])
    return f

def f_manufaturada(y):
    f_6 = y[5]
    f_5 = 2*y[4] + 4*y[5]
    f_4 = 3*y[3] + y[4] + 3*y[5]
    f_3 = y[2] + 3*y[3] + y[4] + 2*y[5]
    f_2 = 2*y[1] + 2*[2] + y[3] + 2*y[4] + y[5]
    f_1 = y[0] + 2*y[1] + 4*y[2] + 3*y[3] + 2*y[4] + y[5]
    f = np.array([f_1, f_2, f_3, f_4, f_5, f_6])
    return f
