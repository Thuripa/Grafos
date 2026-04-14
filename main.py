# Trabalho de Grafos Python
# Guilherme Melo de Jesus e Rõmulo Pedro Thomsen

import GrafoLista
import GrafoMatriz

# MENU DO GRAFO CRIADO
# Esse menu serve para modificar o grafo depois de criado
def menu():

    print()
    print("1 - Inserir Vértice")
    print("2 - Remover Vértice")
    print("3 - Rotular Vértice")
    print("4 - Imprimir Grafo")
    print("5 - Inserir Aresta")
    print("6 - Remover Aresta")
    print("7 - Existe Aresta")
    print("8 - Peso Aresta")
    print("9 - Retorna Vizinhos")
    print("10 - BUSCAS")
    print("0 - SAIR")

    menuGrafo = int(input("Escolha uma opção: "))

    return menuGrafo


# INICIO DO PROGRAMA 
print("Trabalho de Grafos")
print("1 - Criar Grafo em Matriz Manualmente")
print("2 - Criar Grafo em Lista Manualmente")
print("3 - Criar Grafo Automaticamente (Matriz)")
print("4 - Criar Grafo Automaticamente (Lista)")
print()

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

        grafo = GrafoMatriz.GrafoMatriz(ponderado, direcionado)

        # LOOPING DO MENU GRAFO
        # Enquanto menuGrafo for diferente de 0 - SAIR
        menuGrafo = menu()
        while menuGrafo != 0:

            # 1 - INSERIR VÉRTICE
            if menuGrafo == 1:

                # DEFINE O RÓTULO DO NOVO VÉRTICE
                rotulo = str(input("Insira um rótulo para o Vértice: ").strip())

                # VERIFICA SE JÁ EXISTE ESSE RÓTULO NUM VÉRTICE
                existe = grafo.existeVertice(rotulo)

                # SE JÁ EXISTIR
                if (existe):
                    print()
                    print("VÉRTICE JÁ EXISTENTE")

                # SENÃO
                else:
                    grafo.inserirVertice(rotulo)
                    print()
                    print("Vértice inserido com sucesso!")

            # 2 - REMOVER VÉRTICE
            elif menuGrafo == 2:

                # DEFINE O RÓTULO DO VÉRTICE A SER EXCLUÍDO
                rotulo = str(input("Insira o rótulo do vértice a ser excluído: ")).strip()

                # Para cada Vértice no Grafo
                for vertice in grafo.vertices:

                    # Se existir o tal Vértice
                    if vertice.rotulo == rotulo:

                        # SE O VÉRTICE EXISTE NO GRAFO
                        if grafo.removerVertice(vertice):
                            print()
                            print("Vértice removido com sucesso!")

                        # SE NÃO EXISTIR
                        else:
                            print()
                            print("Vértice não existe!")

            # 3 - ROTULAR VÉRTICE (Edita o rótulo do vértice)
            elif menuGrafo == 3:

                # DEFINE O RÓTULO DO VÉRTICE A SER EDITADO
                rotulo = str(input("Insira o vértice a ser editado: ")).strip()

                # DEFINE O NOVO RÓTULO DO VÉRTICE
                novo_rotulo = str(input("Insira o novo rótulo: ")).strip()

                if grafo.rotulaVertice():
                    print()
                    print("Vértice editado com sucesso! ")
                else:
                    print()
                    print("Vértice não existe!")

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
                            print()
                            print("Aresta Inserida de " + origem + " Para " + destino)

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

                            print()
                            print("Aresta Inserida de " + origem + " Para " + destino)
                        else:
                            print("FALHA AO INSERIR ARESTA")
                            print()

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

                            print()
                            print("Aresta Inserida de " + origem + " Para " + destino)

                        else:
                            print("FALHA AO INSERIR ARESTA")

                            # SE NÃO FOR UM GRAFO PONDERADO
                    else:

                        # DEFINE O VÉRTICE DE ORIGEM
                        origem = str(input("Insira o Vértice de Origem: "))

                        # DEFINE O VÉRTICE DE DESTINO
                        destino = str(input("Insira o Vértice de Destino: "))

                        # PESO = 0 PARA GRAFO NÃO PONDERADO
                        peso = 0

                        # INSERE ARESTA NO GRAFO (Retorna True ou False)
                        # Insere aresta da ORIGEM para o DESTINO
                        if grafo.inserirAresta(origem, destino, peso):

                            # Insere aresta do DESTINO para ORIGEM
                            grafo.inserirAresta(destino, origem, peso)

                            print()
                            print("Aresta Inserida de " + origem + " Para " + destino)
                        else:
                            print("FALHA AO INSERIR ARESTA")

                            # 6 - REMOVER ARESTA

            elif menuGrafo == 6:
                pass

            # 7 - EXISTE ARESTA
            elif menuGrafo == 7:

                # DEFINE O VÉRTICE DE ORIGEM
                origem = str(input("Insira o Vértice de Origem: "))

                # DEFINE O VÉRTICE DE DESTINO
                destino = str(input("Insira o Vértice de Destino: "))

                if grafo.existeAresta(origem, destino) == True:

                    print()
                    print("Existe aresta entre " + origem + " e " + destino)
                else:

                    print()
                    print("NÃO Existe aresta entre " + origem + " e " + destino)

            # 8 - PESO ARESTA
            elif menuGrafo == 8:

                # DEFINE O VÉRTICE DE ORIGEM
                origem = str(input("Insira o Vértice de Origem: "))

                # DEFINE O VÉRTICE DE DESTINO
                destino = str(input("Insira o Vértice de Destino: "))

                # Pega o peso da aresta
                peso = grafo.pesoAresta(origem, destino)

                # Se o retorno for diferente de Falso
                if peso != False:

                    print()
                    print("O peso da aresta é de: " + str(peso))
                else:

                    print()
                    print("NÃO Existe aresta entre " + origem + " e " + destino)


            # 9 - RETORNA VIZINHOS
            elif menuGrafo == 9:

                # DEFINE O VÉRTICE DE DESTINO
                origem = input("insira o Vértice de Origem: ")

                # SE EXISTIR VÉRTICE NO GRAFO RETORNA TODOS OS VIZINHOS
                if grafo.existeVertice(origem):

                    # PERCORRE A LISTA DE VIZINHOS DA ORIGEM
                    i = self.vertices.index(origem)
                    j = self.vertices.index(destino)
                        # Printa o Destino da Aresta e o Peso do Caminho


            # 0 - SAIR
            elif menuGrafo == 0:
                break

            # LOOPING DO MENU DO GRAFO
            menuGrafo = menu()

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
                existe = grafo.existeVertice(rotulo)

                # SE JÁ EXISTIR
                if (existe):
                    print()
                    print("VÉRTICE JÁ EXISTENTE")

                # SENÃO
                else: 
                    grafo.inserirVertice(rotulo)
                    print()
                    print("Vértice inserido com sucesso!")

                

            # 2 - REMOVER VÉRTICE
            elif menuGrafo == 2:

                # DEFINE O RÓTULO DO VÉRTICE A SER EXCLUÍDO
                rotulo = str(input("Insira o rótulo do vértice a ser excluído: ")).strip()

                # Para cada Vértice no Grafo
                for vertice in grafo.vertices:

                    # Se existir o tal Vértice
                    if vertice.rotulo == rotulo:

                        # SE O VÉRTICE EXISTE NO GRAFO
                        if grafo.removerVertice(vertice):
                            print()
                            print("Vértice removido com sucesso!")

                        # SE NÃO EXISTIR
                        else:
                            print()
                            print("Vértice não existe!")


            # 3 - ROTULAR VÉRTICE (Edita o rótulo do vértice)
            elif menuGrafo == 3:

                # DEFINE O RÓTULO DO VÉRTICE A SER EDITADO
                rotulo = str(input("Insira o vértice a ser editado: ")).strip()

                # DEFINE O NOVO RÓTULO DO VÉRTICE
                novo_rotulo = str(input("Insira o novo rótulo: ")).strip()

                if grafo.rotulaVertice():
                    print()
                    print("Vértice editado com sucesso! ")
                else:
                    print()
                    print("Vértice não existe!")

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

                            print()
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

                            print()
                            print("Aresta Inserida de "+origem+" Para "+destino)
                        else:
                            print("FALHA AO INSERIR ARESTA")   
                            print()

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

                            print()
                            print("Aresta Inserida de "+origem+" Para "+destino)

                        else:
                            print("FALHA AO INSERIR ARESTA")  

                    # SE NÃO FOR UM GRAFO PONDERADO
                    else:

                        # DEFINE O VÉRTICE DE ORIGEM
                        origem = str(input("Insira o Vértice de Origem: "))

                        # DEFINE O VÉRTICE DE DESTINO
                        destino = str(input("Insira o Vértice de Destino: "))
                        
                         # PESO = 0 PARA GRAFO NÃO PONDERADO
                        peso = 0
                        
                        # INSERE ARESTA NO GRAFO (Retorna True ou False)
                        # Insere aresta da ORIGEM para o DESTINO
                        if grafo.inserirAresta(origem, destino, peso):
                           
                           # Insere aresta do DESTINO para ORIGEM
                           grafo.inserirAresta(destino, origem, peso)

                           print()
                           print("Aresta Inserida de "+origem+" Para "+destino)
                        else:
                            print("FALHA AO INSERIR ARESTA")   

            # 6 - REMOVER ARESTA
            elif menuGrafo == 6:

                # Define Origem e Destino
                origem = input("Insira o Vértice de Origem")
                destino = input("Insira o Vértice de Destino")

                # Remove Aresta
                grafo.removerAresta(origem, destino)

            # 7 - EXISTE ARESTA
            elif menuGrafo == 7:
                        
                # DEFINE O VÉRTICE DE ORIGEM
                origem = str(input("Insira o Vértice de Origem: "))

                # DEFINE O VÉRTICE DE DESTINO
                destino = str(input("Insira o Vértice de Destino: "))

                # Se existir Aresta printa origem e destino
                if grafo.existeAresta(origem, destino) == True:
                    print()
                    print("Existe aresta entre " + origem + " e " + destino )

                # Senão printa que não existe origem e destino
                else:
                    print()
                    print("NÃO Existe aresta entre " + origem + " e " + destino )

            # 8 - PESO ARESTA
            elif menuGrafo == 8:
                
                # DEFINE O VÉRTICE DE ORIGEM
                origem = str(input("Insira o Vértice de Origem: "))

                # DEFINE O VÉRTICE DE DESTINO
                destino = str(input("Insira o Vértice de Destino: "))

                # PEGA O PESO DA ARESTA
                peso = grafo.retornarPeso(origem, destino)

                # SE O RETORNO FOR DIFERENTE DE FALSO PRINTA O PESO DA ARESTA
                if peso != False:
                    print()
                    print("O peso da aresta é de: "+ str(peso))

                # SENÃO PRINTA QUE NÃO EXISTE
                else:
                    print()
                    print("NÃO Existe aresta entre " + origem + " e " + destino )


            # 9 - RETORNA VIZINHOS
            elif menuGrafo == 9:

                # DEFINE O VÉRTICE DE DESTINO
                origem = input("insira o Vértice de Origem: ")

                # SE EXISTIR VÉRTICE NO GRAFO RETORNA TODOS OS VIZINHOS
                if grafo.existeVertice(origem):

                    # PERCORRE A LISTA DE VIZINHOS DA ORIGEM
                    for aresta in grafo.retornaVizinhos(origem):

                        # Printa o Destino da Aresta e o Peso do Caminho
                        print("Destino: "+aresta.destino+" Peso: "+aresta.peso)


            # 0 - SAIR
            elif menuGrafo == 0:
                break

            # LOOPING DO MENU DO GRAFO
            menuGrafo = menu()

    # CRIA GRAFO AUTOMATICAMENTE MATRIZ
    if opcao == 3:

        # INICIA O GRAFO
        grafo = GrafoMatriz.GrafoMatriz(ponderado, direcionado)

        # INSERE VERTICES
        grafo.inserirVertice("A")
        grafo.inserirVertice("B")
        grafo.inserirVertice("C")
        grafo.inserirVertice("D")
        grafo.inserirVertice("E")

        # INSERE ARESTAS
        grafo.inserirAresta("A", "B", 15)

        grafo.inserirAresta("A", "C", 10)

        grafo.inserirAresta("B", "C", 10)

        grafo.inserirAresta("C", "D", 15)

        grafo.inserirAresta("D", "E", 10)

    # CRIA GRAFO AUTOMATICAMENTE LISTA
    if opcao == 4:
        pass