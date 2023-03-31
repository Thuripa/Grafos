# Trabalho de Grafos Python
# Guilherme Melo de Jesus

import GrafoLista


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

    menuGrafo = int(input("Escolha uma opção: "))

    return menuGrafo


print("Trabalho de Grafos")
print("1 - Criar Grafo em Matriz")
print("2 - Criar Grafo em Lista")
print("0 - SAIR")

opcao = int(input("Escolha uma opção:  "))
dir = str(input("O Grafo é Direcionado? (S/N) : "))
pond = str(input("O Grafo é Ponderado? (S/N) : "))
print("")

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
        pass
    # Cria Grafo numa Lista
    if opcao == 2:

        # Constrói o Grafo
        grafo = GrafoLista.GrafoLista(ponderado, direcionado)

        # Looping do Menu do Grafo
        menuGrafo = menu()
        while menuGrafo != 0:

            # 1 - Inserir Vértice
            if menuGrafo == 1:

                # Define o rótulo do vértice
                rotulo = str(input("Insira um rótulo para o Vértice: ").strip())

                # Insere o vértice no Grafo
                grafo.inserirVertice(rotulo)
                print("Vértice inserido com sucesso")
                print()

            # 2 - Remover Vértice
            elif menuGrafo == 2:

                # Define o rótulo do vértice a ser inserido
                rotulo = str(input("Insira o rótulo do vértice a ser excluído: ")).strip()

                # Se o vértice existe no Grafo
                if grafo.removerVertice(rotulo):

                    print("Vértice removido")

                # Se não existir
                else:
                    print("Vértice não existe!")

            # 3 - Rotular Vértice
            elif menuGrafo == 3:

                # Define o vértice a ser editado
                rotulo = str(input("Insira o vértice a ser editado: ")).strip()

                # Define o vértice
                novo_rotulo = str(input("Insira o novo rótulo: ")).strip()

                # Edita o rótulo do vértice

            # 4 - Imprimir Grafo
            elif menuGrafo == 4:
                grafo.imprimirGrafo()

            # 5 - Inserir Aresta
            elif menuGrafo == 5:

                # Se for um Grafo Direcionado
                if direcionado:

                    # Se for um Grafo Ponderado
                    if ponderado:

                        # Define o Vértice de Origem
                        origem = str(input("Insira o Vértice de Origem: ")).strip()

                        # Define o Vértice de Destino
                        destino = str(input("Insira o Vértice de Destino: ")).strip()

                        # Define o Peso do Vértice
                        peso = int(input("Insira o Peso da Aresta: "))

                        # Insere Aresta no Grafo
                        if grafo.inserirAresta(origem, destino, peso):

                           print("Aresta Inserida de "+origem+" Para "+destino)

                    # Se Não for um Grafo Ponderado
                    else:

                        # Define o Vértice de Origem
                        origem = str(input("Insira o Vértice de Origem: "))

                        # Define o Vértice de Destino
                        destino = str(input("Insira o Vértice de Destino: "))

                # Se for um Grafo Não Direcionado
                else:
                    pass

            # 6 - Remover Aresta
            elif menuGrafo == 6:
                pass
            # 7 - Existe Aresta
            elif menuGrafo == 7:
                pass
            # 8 - Peso Aresta
            elif menuGrafo == 8:
                pass
            # 9 - Retorna Vizinhos
            elif menuGrafo == 9:
                pass

            # Looping do Menu do Grafo
            menuGrafo = menu()
