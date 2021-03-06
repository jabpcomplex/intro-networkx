# -*- coding: utf-8 -*-
"""random_walks_redes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZppFxsANuqQAXsBxKMByptHg3r8dIqUF

# Introducción a las caminatas aleatoria en REDES
# Introducción al modelo Albert-Barabasi
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# red barabasi con 150 nodo y 1 
G = nx.barabasi_albert_graph(150, 1)

plt.figure(figsize = [10,8]) #tamaño imagen
nx.draw(G, node_size = 50, with_labels = True)

nodo = 1
G.neighbors(nodo)

#Vecinos del nodo 1
list(G.neighbors(nodo))

def Paso(nodo):
  vecinos = list(G.neighbors(nodo))
  nuevo = np.random.choice(vecinos) #elige un vecino al azar
  return nuevo

def Caminata(inicial, N):
  camino = [inicial]
  nodo = inicial
  for i in range(N):
    nodo = Paso(nodo)
    camino.append(nodo)
  return camino

"""##**Caminata Aleartoria en la RED**"""

#nodo inicial | numero de pasos
walk = Caminata(50,1000)

# y cuenta por donde paso 
# x son los bins de G
y,x = np.histogram(walk, bins = range(len(G)+1))

plt.figure(figsize = [10,5])
plt.title("Nodo que visito mas el caminante")
plt.xlabel("Nodo");plt.ylabel("Número de visitas");
plt.bar(x[:-1], y)

