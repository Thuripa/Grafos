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
        Grafo = GrafoLista.criaGrafo(direcionado, ponderado)

        # Looping do Menu do Grafo
        while menu() != 0:

            # 1 - Inserir Vértice
            if 1:

                rotulo = str(input("Insira o rótulo do vértice: "))
                Grafo

            # 2 - Remover Vértice
            elif 2:
                pass
            # 3 - Rotular Vértice
            elif 3:
                pass
            # 4 - Imprimir Grafo
            elif 4:
                pass
            # 5 - Inserir Aresta
            elif 5:
                pass
            # 6 - Remover Aresta
            elif 6:
                pass
            # 7 - Existe Aresta
            elif 7:
                pass
            # 8 - Peso Aresta
            elif 8:
                pass
            # 9 - Retorna Vizinhos
            elif 9:
                pass
