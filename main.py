# Trabalho de Grafos Python
# Guilherme Melo de Jesus e Rõmulo Pedro Thomsen

import GrafoLista

# MENU DO GRAFO CRIADO
# Esse menu serve para modificar o grafo depois de criado
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


# INICIO DO PROGRAMA
print("Trabalho de Grafos")
print("1 - Criar Grafo em Matriz")
print("2 - Criar Grafo em Lista")
print("0 - SAIR")

opcao = int(input("Escolha uma opção:  "))
dir = str(input("O Grafo é Direcionado? (S/N) : "))
pond = str(input("O Grafo é Ponderado? (S/N) : "))
print("")

# DEFINE SE O GRAFO É OU NÃO DIRECIONADO
if dir == "S" or dir == "s":
    direcionado = True
else:
    direcionado = False    

# DEFINE SE O GRAFO É OU NÃO PONDERADO
if pond == "S" or pond == "s":
    ponderado = True
else: 
    ponderado = False

# LOOPING DO MENU INICIAL
# Enquanto o usuário não escolher 0 - SAIR
while opcao != 0:

    # CRIA GRAFO NUMA MATRIZ - A SER IMPLEMENTADO
    if opcao == 1:

        # A SER IMPLEMENTADO
        print("A FUNÇÃO AINDA NÃO FOI IMPLEMENTADA!")
        break

    # CRIA GRAFO NUMA LISTA
    if opcao == 2:

        # CONSTRÓI O GRAFO
        grafo = GrafoLista.GrafoLista(ponderado, direcionado)

        # LOOPING DO MENU GRAFO
        # Enquanto menuGrafo for diferente de 0 - SAIR
        menuGrafo = menu()
        while menuGrafo != 0:

            # 1 - INSERIR VÉRTICE
            if menuGrafo == 1:

                # DEFINE O RÓTULO DO NOVO VÉRTICE
                rotulo = str(input("Insira um rótulo para o Vértice: ").strip())

                # VERIFICA SE JÁ EXISTE ESSE RÓTULO NUM VÉRTICE
                existe = GrafoLista.existeVertice(grafo, rotulo)

                # SE JÁ EXISTIR
                if (existe):
                    print("VÉRTICE JÁ EXISTENTE")

                # SENÃO
                else: 
                    grafo.inserirVertice(rotulo)    
                    print("Vértice inserido com sucesso!")

                

            # 2 - REMOVER VÉRTICE
            elif menuGrafo == 2:

                # DEFINE O RÓTULO DO VÉRTICE A SER INSERIDO
                rotulo = str(input("Insira o rótulo do vértice a ser excluído: ")).strip()

                # SE O VÉRTICE EXISTE NO GRAFO
                if grafo.removerVertice(rotulo):

                    print("Vértice removido")

                # SE NÃO EXISTIR
                else:
                    print("Vértice não existe!")

            # 3 - ROTULAR VÉRTICE
            # Edita o rótulo do vértice
            elif menuGrafo == 3:

                # DEFINE O RÓTULO DO VÉRTICE A SER EDITADO
                rotulo = str(input("Insira o vértice a ser editado: ")).strip()

                # DEFINE O NOVO RÓTULO DO VÉRTICE
                novo_rotulo = str(input("Insira o novo rótulo: ")).strip()

                

            # 4 - IMPRIMIR GRAFO
            elif menuGrafo == 4:
                grafo.imprimirGrafo()

            # 5 - INSERIR ARESTA
            elif menuGrafo == 5:

                # SE FOR UM GRAFO DIRECIONADO
                if direcionado:

                    # SE FOR UM GRAFO PONDERADO
                    if ponderado:

                        # DEFINE O VÉRTICE DE ORIGEM
                        origem = str(input("Insira o Vértice de Origem: ")).strip()

                        # DEFINE O VÉRTICE DE DESTINO
                        destino = str(input("Insira o Vértice de Destino: ")).strip()

                        # DEFINE O PESO DA ARESTA
                        peso = int(input("Insira o Peso da Aresta: "))

                        # INSERE ARESTA NO GRAFO
                        if grafo.inserirAresta(origem, destino, peso):

                           print("Aresta Inserida de "+origem+" Para "+destino)

                    # SE NÃO FOR UM GRAFO PONDERADO
                    else:

                        # DEFINE O VÉRTICE DE ORIGEM
                        origem = str(input("Insira o Vértice de Origem: "))

                        # DEFINE O VÉRTICE DE DESTINO
                        destino = str(input("Insira o Vértice de Destino: "))
                        
                        # PESO = 0 PARA GRAFO NÃO PONDERADO
                        peso = 0
                        # INSERE ARESTA NO GRAFO
                        if grafo.inserirAresta(origem, destino, peso):

                           print("Aresta Inserida de "+origem+" Para "+destino)
                        else:
                            print("FALHA AO INSERIR ARESTA")   

                # SE FOR UM GRAFO NÃO DIRECIONADO
                else:

                    # SE FOR UM GRAFO PONDERADO 
                    if ponderado:

                        # DEFINE O VÉRTICE DE ORIGEM
                        origem = str(input("Insira o Vértice de Origem: ")).strip()

                        # DEFINE O VÉRTICE DE DESTINO
                        destino = str(input("Insira o Vértice de Destino: ")).strip()

                        # DEFINE O PESO DA ARESTA
                        peso = int(input("Insira o Peso da Aresta: "))

                        # INSERE ARESTA NO GRAFO
                        if grafo.inserirAresta(origem, destino, peso):

                           print("Aresta Inserida de "+origem+" Para "+destino)

                    # SE NÃO FOR UM GRAFO PONDERADO
                    else:

                        # DEFINE O VÉRTICE DE ORIGEM
                        origem = str(input("Insira o Vértice de Origem: "))

                        # DEFINE O VÉRTICE DE DESTINO
                        destino = str(input("Insira o Vértice de Destino: "))
                        
                         # PESO = 0 PARA GRAFO NÃO PONDERADO
                        peso = 0
                        
                        # INSERE ARESTA NO GRAFO
                        if grafo.inserirAresta(origem, destino, peso):

                           print("Aresta Inserida de "+origem+" Para "+destino)
                        else:
                            print("FALHA AO INSERIR ARESTA")   

            # 6 - REMOVER ARESTA
            elif menuGrafo == 6:
                pass
            # 7 - EXISTE ARESTA
            elif menuGrafo == 7:
                pass
            # 8 - PESO ARESTA
            elif menuGrafo == 8:
                pass
            # 9 - RETORNA VIZINHOS
            elif menuGrafo == 9:
                pass

            # LOOPING DO MENU DO GRAFO
            menuGrafo = menu()
