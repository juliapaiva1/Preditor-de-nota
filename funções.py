#imports
import pandas as pd
import numpy as np
import copy
import random
import matplotlib.pyplot as plt
from scipy.linalg import svd, diagsvd

#criação da matriz B
def criacao_matriz_b(matriz_a):
    # Copiar A para B
    matriz_b = copy.deepcopy(matriz_a)
    #inicia um loop para encontrar um elemento diferente de 0
    elemento_diferente_de_0 = False
    while elemento_diferente_de_0 == False:
        #sorteia elementos aleatórios para i e j
        i = random.randint(0, 670)
        j = random.randint(0, 9065)

        #modifica um valor da matriz, multiplicando por um número aleatório entre 1 e 5, se este for diferente de zero
        if matriz_b[i][j] != 0:
            matriz_b[i][j] = random.randint(1, 5)
            elemento_diferente_de_0 = True

        #se não for diferente de 0, volta o loop
        else:
            elemento_diferente_de_0 = False
    #retorna a matriz b com ruído e os valores de i e j utilizados
    return matriz_b, i, j


#sistema preditor em função
def sistema(matriz_b, i, j):

    #faz a decomposição svd da matriz b
    u, s, vt = svd(matriz_b)

    #sorteia um valor aleatório para k
    k = random.randint(0, 671)

    #cria as matrizes u_, s_ e vt_ com k elementos
    u_ = u[:,0:k]
    s_ = s[:k]
    vt_ = vt[:k,:]

    #cria a matriz b com ruído diminuído
    matriz_b_alterada = u_ @ diagsvd(s_, u_.shape[1], vt_.shape[0]) @ vt_

    #devolve a matriz b com ruído diminuído
    return matriz_b_alterada[i][j]
