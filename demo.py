#imports
import pandas as pd
import numpy as np
import copy
import random
import matplotlib.pyplot as plt
from scipy.linalg import svd, diagsvd
from funções import *

#criação da matriz A
df = pd.read_csv("ratings_small.csv")

#cria tabela com as médias de classificação de cada usuário, substituindo os valores nulos por 0, e transforma em array
matriz_a = df.pivot_table(index='userId', columns='movieId', values='rating')
matriz_a = matriz_a.fillna(0)
matriz_a = matriz_a.to_numpy()
print(matriz_a)
matriz_a.shape

#aplica repetidamente o sistema preditor e calcula o erro

#contador de iterações
contador=0 
#lista para armazenar os erros
tabela = [] 

for contador in range(100):
    #chama funções para criar matriz b e aplicar o sistema
    matriz_b, i, j = criacao_matriz_b(matriz_a)
    matriz_b_alterada = sistema(matriz_b, i, j)
    #adiciona iteração
    contador +=1
    #calcula diferença entre o valor original e o predito
    erro = matriz_a[i][j] - matriz_b_alterada
    #adiciona o erro à lista
    tabela.append(erro)

#cria histograma com dados da lista
plt.hist(tabela, bins=30)
plt.title("Histograma de erros do sistema preditor")
plt.xlabel("Diferença entre valor original e predito")
plt.ylabel("Frequência")
plt.savefig("histograma.png")
plt.show()