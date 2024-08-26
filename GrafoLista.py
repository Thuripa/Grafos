# Classe GrafoLista
class GrafoLista:

    # Construtor
    def __init__(self, ponderado, direcionado):

        # Lista de Vértices
        self.vertices = []

        # Lista de Arestas
        self.arestas = []

        # Se o Grafo é ponderado ou não
        self.ponderado = ponderado

        # Se o Grafo é direcionado ou não
        self.direcionado = direcionado

    # INSERIR VERTICE
    def inserirVertice(self, rotulo):

        # Cria Vertice
        vertice = Vertice(rotulo, [])

        # Insere o Vértice no GrafoLista
        self.vertices.append(vertice)    
        
        # Retorna Verdadeiro em Caso de Sucesso
        return True

    # REMOVER VERTICE
    def removerVertice(self, rotulo):

        # Remove Vizinhos
        # Para cada Vértice do Grafo
        for vertice in self.vertices:

            # Para cada Aresta em Cada Vértice do Grafo
            for aresta in vertice.arestas:

                # Se a aresta possuir o vértice a ser excluido como destino
                if aresta.destino.rotulo == rotulo:

                    # Chama a função para remover a aresta
                    self.removerAresta(vertice, rotulo)
        
    # ROTULAR VERTICE (EDITAR)
    def rotulaVertice(self, rotulo, novo_rotulo):

        # Verifica se o vértice existe no Grafo
        # Para cada Vértice no Grafo
        for vertice in self.vertices:

            # Se o vértice existir
            if vertice.rotulo == rotulo:

                # Atualiza Rótulo
                vertice.rotulo = novo_rotulo
                return True

        # Senão retona Falso
        return False

    # IMPRIMIR GRAFO
    def imprimirGrafo(self):

        # PULA UMA LINHA
        print()

        # IMPRIME VÉRTICES
        # Para cada vértice no grafo
        for vertice in self.vertices:
            
            # Pega o rótulo do vértice
            print(vertice.rotulo + ": ")

            # Percorre vizinhos do vértice
            for aresta in vertice.arestas:

                # Adiciona o rótulo do vizinho na lista
                print(" -> " + aresta.destino.rotulo, end=" ")

            # PULA UMA LINHA
            print()    
                
    # INSERIR ARESTA
    def inserirAresta(self, origem, destino, peso):

        # Existe origem
        existe_origem = False

        # Verifica se o vértice de ORIGEM existe
        for vertice_origem in self.vertices:

            # Se existir o Vértice ORIGEM no Grafo
            if vertice_origem.rotulo == origem:

                existe_origem = True

                # Verifica se o vértice de DESTINO existe
                for vertice_destino in self.vertices:

                    # Se existir o Vértice DESTINO no Grafo
                    if vertice_destino.rotulo == destino:

                        # Se o Grafo for DIRECIONADO
                        if self.direcionado:
                            
                            # Cria uma nova Aresta
                            nova_aresta = Aresta(vertice_origem, vertice_destino, peso)

                            # Insere Aresta nos Vertices
                            vertice_origem.arestas.append(nova_aresta)

                            # Insere a nova_aresta no Grafo
                            #self.arestas.append(nova_aresta)

                        # Se o Grafo for NÃO DIRECIONADO
                        else:

                            # Cria duas arestas para o grafo NÃO DIRECIONADO (vai e volta)
                            nova_aresta1 = Aresta(vertice_origem, vertice_destino, peso)
                            nova_aresta2 = Aresta(vertice_destino, vertice_origem, peso)

                            # Insere Aresta nos Vertices
                            vertice_origem.arestas.append(nova_aresta1)
                            vertice_destino.arestas.append(nova_aresta2)

                            # Insere a nova_aresta no Grafo
                            #self.arestas.append(nova_aresta1)
                            #self.arestas.append(nova_aresta2)

                        return True

        # Se não houver o vértice de ORIGEM no grafo
        if existe_origem == False:

            print("Vértice de Origem não existe!")
        
        # Se não houver o vértice de DESTINO no grafo
        else:

            print("Vértice de Destino não existe!")

        return False

    # REMOVER ARESTA
    def removerAresta(self, origem, destino):
        
        # Verifica se o vértice de ORIGEM existe
        for vertice_origem in self.vertices:

            # Se existir o Vértice ORIGEM no Grafo
            if vertice_origem.rotulo == origem:

                # Verifica se o vértice de DESTINO existe
                for vertice_destino in self.vertices:

                    # Se existir o Vértice DESTINO no Grafo
                    if vertice_destino.rotulo == destino:
                        
                        # Se for um Grafo DIRECIONADO
                        # Para cada aresta na lista de arestas do Vértice de ORIGEM
                        for aresta in vertice_origem.arestas:

                            # Se a aresta for a correspondente de ORIGEM e DESTINO
                            if aresta.destino.rotulo == vertice_destino:

                                # Remove Aresta
                                vertice_origem.arestas.remove(aresta)


                        # Se for um Grafo NÃO DIRECIONADO
                        # Para cada aresta na lista de arestas do Vértice de ORIGEM
                        for aresta in vertice_origem.arestas:

                            # Se a aresta for a correspondente de ORIGEM e DESTINO
                            if aresta.destino.rotulo == vertice_destino:

                                # Remove Aresta
                                pass

    # EXISTE ARESTA
    def existeAresta(self, origem, destino):
        
        # Verifica se o vértice de ORIGEM existe
        for vertice_origem in self.vertices:

            # Se existir o Vértice ORIGEM no Grafo
            if vertice_origem.rotulo == origem:

                # Verifica se o vértice de DESTINO existe
                for vertice_destino in self.vertices:

                    # Se existir o Vértice DESTINO no Grafo
                    if vertice_destino.rotulo == destino:
                        
                        # Busca Vizinhos do Vértice de ORIGEM
                        for aresta in vertice_origem.arestas:

                            # Se encontrar o Vértice DESTINO na lista de Arestas da ORIGEM
                            if aresta.destino.rotulo == vertice_destino.rotulo:

                                # Retorna Verdadeiro
                                return True 

    # RETORNA O PESO DA ARESTA
    def pesoAresta(self, origem, destino):

        # Verifica se o vértice de ORIGEM existe
        for vertice_origem in self.vertices:

            # Se existir o Vértice ORIGEM no Grafo
            if vertice_origem.rotulo == origem:

                # Verifica se o vértice de DESTINO existe
                for vertice_destino in self.vertices:

                    # Se existir o Vértice DESTINO no Grafo
                    if vertice_destino.rotulo == destino:
                        
                        # Busca Vizinhos do Vértice de ORIGEM
                        for aresta in vertice_origem.arestas:

                            # Se encontrar o Vértice DESTINO na lista de Arestas da ORIGEM
                            if aresta.destino.rotulo == vertice_destino.rotulo:

                                # Retorna o peso da Aresta
                                return aresta.peso 

        # Senão retorna Falso
        return False

    # RETORNA VIZINHOS
    def retornaVizinhos(rotulo):
        pass

    # VERIFICA SE O VÉRTICE EXISTE NO GRAFO
    def existeVertice(self, rotulo):
        
        # PARA CADA VERTICE NO GRAFO
        for vertice in self.vertices:

            # SE O ROTULO FOR IGUAL A UM DOS VERTICES
            if vertice.rotulo == rotulo:
                    
                # RETORNA VERDADEIRO (VERTICE EXISTE NO GRAFO)
                return True

        # SENAO, RETORNA FALSO
        return False        

# CLASSE VERTICE
class Vertice:

    # Construtor do Vértice
    def __init__(self, rotulo, arestas):

        # Rótulo (nome) do Vértice
        self.rotulo = rotulo

        # Lista de Arestas
        self.arestas = []

# CLASSE ARESTA
class Aresta:

    # Construtor da Aresta
    def __init__(self, origem, destino, peso):

        # Vértice de Origem
        self.origem = origem

        # Vértice de Destino
        self.destino = destino

        # Peso da Aresta
        self.peso = peso