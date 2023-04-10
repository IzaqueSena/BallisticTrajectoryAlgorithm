import math
import numpy as np
from metodos_numericos import trapezio_ponto_fixo
from funcoes import f

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
    p = math.log( math.sqrt( p0**2 + p1**2 ) )
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
    e = (y_h_sobre_2 - y_h)/3
    return math.sqrt(e[0]**2 + e[1]**2)

def imprimeLinhaTabela(n, h_n, erro, p, iteração):
    if iteração == 5:
        print("%5d &  %9.3e &  %9.3e &  \\\\" % (n, h_n, erro))
    else:
        print("%5d &  %9.3e &  %9.3e &  %9.3e \\\\" % (n, h_n, erro,p))