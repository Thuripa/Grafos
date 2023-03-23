# Classe Grafo
class GrafoLista:

    # Construtor do Grafo
    def __init__(self, direcionado, ponderado):

        # Valor de ID do vértice
        self.index = 0

        # Lista de vértices
        self.vertices = {}

        # Se o Grafo é direcionado ou não
        self.direcionado = direcionado

        # Se o Grafo é ponderado (arestas com pesos) ou não
        self.ponderado = ponderado


    def inserirVertice(self, rotulo):
        self.GrafoLista[self.GrafoLista.]


    def removerVertice(self):
        pass


    def rotulaVertice(self):
        pass


    def imprimeGrafo(self):
        pass


    def inserirAresta(self):
        pass


    def removerAresta(self):
        pass


    def existeAresta(self):
        pass


    def pesoAresta(self):
        pass


    def retornaVizinhos(self):
        pass

class Vertice:

    def __init__(self, id, rotulo, arestas):

        # ID do vértice
        self.id = id

        # Rótulo do vértice
        self.rotulo = rotulo

        # Lista de arestas do vértice (vizinhos)
        self.arestas = arestas




# Classe Aresta
class Aresta:

    # Construtor
    def __init__(self, origem, destino, peso):

        # Define o vértice de origem
        self.origem = origem

        # Define o vértice de destino
        self.destino = destino

        # Define o peso da aresta
        self.peso = peso
