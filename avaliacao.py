import math
import numpy as np
from metodos_numericos import trapezio_ponto_fixo
from funcoes import f
from metodos_numericos import trapezio_ponto_fixo_manufaturada
from funcoes import f_manufaturada

'''
Função Python para o tamanho do passo h_n
h_n = (t_n-t_0)/n
'''
def h_n(t_0, t_n, n):
    return (t_n - t_0)/n

'''
Estimativa da ordem de convergencia p
p =~ log_2( | (y_k(2h) - y_k(h))/(y_k(h) - y_k(h/2)) | )
y_k(h): é o resultado do nosso modelo para t=tk, e tamanho de passo h
'''
def p(n_trapezio, n_pontofixo, y_0, t_0, t_n, a):
    y_2h = trapezio_ponto_fixo(int(n_trapezio/2), t_0, t_n, y_0, f, n_pontofixo, a)
    y_h = trapezio_ponto_fixo(n_trapezio, t_0, t_n, y_0, f, n_pontofixo, a)
    y_h_sobre_2 = trapezio_ponto_fixo(int(2*n_trapezio), t_0, t_n, y_0, f, n_pontofixo, a)
    p0 = (y_2h - y_h)[0]/(y_h - y_h_sobre_2)[0]
    p1 = (y_2h - y_h)[1]/(y_h - y_h_sobre_2)[1]
    p2 = (y_2h - y_h)[2]/(y_h - y_h_sobre_2)[2]
    p3 = (y_2h - y_h)[3]/(y_h - y_h_sobre_2)[3]
    p4 = (y_2h - y_h)[4]/(y_h - y_h_sobre_2)[4]
    p5 = (y_2h - y_h)[5]/(y_h - y_h_sobre_2)[5]
    p = math.log( math.sqrt( p0**2 + p1**2 + p2**2 + p3**2 + p4**2 + p5**2))
    return p

'''
Estimativa do erro de discretização global e
e =~ ( y_k(h/2) - y_k(h) )/( 2^p - 1 )
Como o método de trapezio tem ordem de convergencia p=2
então
e =~ ( y_k(h/2) - y_k(h) )/3
'''
def erro(n_trapezio, n_pontofixo, y_0, t_0, t_n, a):
    y_h = trapezio_ponto_fixo(n_trapezio, t_0, t_n, y_0, f, n_pontofixo, a)
    y_h_sobre_2 = trapezio_ponto_fixo(int(2*n_trapezio), t_0, t_n, y_0, f, n_pontofixo, a)
    e = abs((y_h_sobre_2 - y_h))/3
    return math.sqrt(e[0]**2 + e[1]**2 + e[2]**2 + e[3]**2 + e[4]**2 + e[5]**2)

def imprimeLinhaTabela(n, h_n, erro, p, iteração):
    if iteração == 5:
        print("%5d &  %9.3e &  %9.3e &  \\\\" % (n, h_n, erro))
    else:
        print("%5d &  %9.3e &  %9.3e &  %9.3e \\\\" % (n, h_n, erro,p))


def tabela_sem_solucao():
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
    a = [gama, massa, vento[0], vento[1], vento[2], 9.806]
    y_00 = posicao_0[0]
    y_01 = posicao_0[1]
    y_02 = posicao_0[2]
    y_03 = v_0 * math.cos(math.radians(angulos[0])) * math.cos(math.radians(angulos[1]))
    y_04 = v_0 * math.cos(math.radians(angulos[0])) * math.sin(math.radians(angulos[1]))
    y_05 = v_0 * math.sin(math.radians(angulos[0]))
    y_0 = np.array([y_00, y_01, y_02, y_03, y_04, y_05])
    n_pontofixo = 3
    t_n = 1
    for i in range (5, 14):
        n_trapezio = 2**i
        erro_n = erro(n_trapezio, n_pontofixo, y_0, t_0, t_n, a)
        p_n = p(n_trapezio, n_pontofixo, y_0, t_0, t_n, a)
        h = h_n(t_0, t_n, n_trapezio)
        imprimeLinhaTabela(n_trapezio, h, erro_n, p_n, i)

tabela_sem_solucao()
