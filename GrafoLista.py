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

        # Verifica se o vértice existe no Grafo
        existe = False
        for vertice in self.vertices:

            # Se existir
            if vertice.rotulo == rotulo:

                # Remove o vértice
                self.vertices.remove(vertice)
                return True

        # Senão
        if not existe:
            return False

    # ROTULAR VERTICE (EDITAR)
    def rotulaVertice(self, rotulo, novo_rotulo):

        # Verifica se o vértice existe no Grafo
        existe = False
        for vertice in self.vertices:

            # Se existir
            if vertice.rotulo == rotulo:
                vertice.rotulo = rotulo
                return True

        # Senão
        if not existe:
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

        # Senão
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
                        
                        # REMOVE ARESTA
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

                            # 
                            if aresta.destino.rotulo == vertice_destino.rotulo:
                                pass 

    # RETORNA O PESO DA ARESTA
    def pesoAresta(self, origem, destino):
        pass

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