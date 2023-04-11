import numpy as np

'''
Método numérico implicito de passo unico - Método Trapezio

Parametros:
n_trapezio: numero de passos de integração do método do trapézio
t_0, t_n: intervalo de tempo de integração
y_0: condição inicial da variável
f: função f do problema de cauchy
n_pontofixo: numero de iterações do metodo do ponto fixo
a: parametros da função f
'''
def trapezio_ponto_fixo(n_trapezio, t_0, t_n, y_0, f, n_pontofixo, a):
    h = (t_n - t_0)/n_trapezio
    y_k = y_0
    for i in range(n_trapezio):
        t_k = t_0 + i*h
        
        # ponto fixo
        y_k_mais_um = y_k + h*f(t_k, y_k, a)
        t_k_mais_um = t_k + h
        for j in range(n_pontofixo):
            y_k_mais_um = y_k + (h/2) * (f(t_k, y_k, a) + f(t_k_mais_um, y_k_mais_um, a))
        # fim do ponto fixo

        y_k = y_k_mais_um
    return y_k_mais_um

def trapezio_ponto_fixo_manufaturada(n_trapezio, t_0, t_n, y_0, f_manufaturada, n_pontofixo, a):
    h = (t_n - t_0)/n_trapezio
    y_k = y_0
    for i in range(n_trapezio):
        t_k = t_0 + i*h
        
        # ponto fixo
        y_k_mais_um = y_k + h*f_manufaturada(t_k, y_k, a)
        t_k_mais_um = t_k + h
        for j in range(n_pontofixo):
            y_k_mais_um = y_k + (h/2) * (f_manufaturada(t_k, y_k, a) + f_manufaturada(t_k_mais_um, y_k_mais_um, a))
        # fim do ponto fixo
        y_k = y_k_mais_um
    return y_k_mais_um

