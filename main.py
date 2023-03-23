# Trabalho de Grafos Python
# Guilherme Melo de Jesus

import numpy as np

import GrafoLista
import GrafoMatriz




def menu():

    print("1 - Inserir Vértice")
    print("2 - Remover Vértice")
    print("3 - Rotular Vértice")
    print("4 - Imprimir Grafo")
    print("5 - Inserir Aresta")
    print("6 - Remover Aresta")
    print("7 - Existe Aresta")
    print("8 - Peso Aresta")
    print("9 - Retorna Vizinhos")
    print("0 - SAIR")

    menu = int(input("Escolha uma opção: "))

    if menu == 1:
        pass


print("Trabalho de Grafos")
print("1 - Criar Grafo em Matriz")
print("2 - Criar Grafo em Lista")
print("0 - SAIR")

opcao = int(input("Escolha uma opção:  "))
dir = str(input("O Grafo é Direcionado? (S/N)"))
pond = str(input("O Grafo é Ponderado? (S/N)"))

# Se o Grafo for Direcionado
if dir == "S" or dir == "s":
    direcionado = True

# Se o Grafo for Ponderado
if pond == "S" or pond == "s":
    ponderado = True

# Enquanto o usuário não escolher 0 - SAIR
while opcao != 0:

    # Cria Grafo numa Matriz
    if opcao == 1:

        # Constrói o Grafo em MATRIZ de Adjacências
        GrafoMatriz.criaGrafo(direcionado, ponderado)

        GrafoMatriz.menu()

    # Cria Grafo numa Lista
    if opcao == 2:

        # Constrói o Grafo em LISTA de Adjacências
        GrafoLista.criaGrafo(direcionado, ponderado)

        GrafoLista.menu()

