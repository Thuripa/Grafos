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

    # Inserir Vértice
    def inserirVertice(self, rotulo):

        # Verifica se o Vértice já existe
        for vertice in self.vertices:

            # Se existir
            if vertice.rotulo == rotulo:

                # Cria Vertice
                vertice = Vertice(rotulo, [])

                # Insere o Vértice no GrafoLista
                self.vertices.append(vertice)

    # Remover Vértice
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

    # Rotular Vértice
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

    # Imprimir Grafo
    def imprimirGrafo(self):

        # Imprime vértices
        for vertice in self.vertices:
            print(vertice.rotulo)

    # Inserir Aresta
    def inserirAresta(self, origem, destino, peso):

        existe_origem = False
        existe_destino = False

        # Verifica se o vértice de ORIGEM existe
        for aresta in self.arestas:

            # Se existir o Vértice ORIGEM no Grafo
            if aresta.origem == origem:

                existe_origem = True

                # Verifica se o vértice de DESTINO existe
                for aresta in self.arestas:

                    # Se existir o Vértice DESTINO no Grafo
                    if aresta.destino == destino:

                        existe_destino = True

                        # Cria Aresta
                        nova_aresta = Aresta(origem, destino, peso)

                        # Insere a nova_aresta no Grafo
                        self.arestas.append(nova_aresta)

                        return True

        # Senão

        if existe_origem:
            print("Vértice de Origem não existe!")
        else:
            print("Vértice de Destino não existe!")
        return False




class Vertice:

    # Construtor do Vértice
    def __init__(self, rotulo, arestas):

        # Rótulo (nome) do Vértice
        self.rotulo = rotulo

        # Lista de Arestas
        self.arestas = arestas


class Aresta:

    # Construtor da Aresta
    def __init__(self, origem, destino, peso):

        # Vértice de Origem
        self.origem = origem

        # Vértice de Destino
        self.destino = destino

        # Peso da Aresta
        self.peso = peso