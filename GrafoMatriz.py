# Classe GrafoLista
class GrafoLista:

    # Construtor
    def __init__(self, ponderado, direcionado):

        # Se o Grafo é ponderado ou não
        self.ponderado = ponderado

        # Se o Grafo é direcionado ou não
        self.direcionado = direcionado

    # INSERIR VERTICE
    def inserirVertice(self, rotulo):

        # Verifica se o Vértice já existe
        for vertice in self.vertices:

            # Se existir
            if vertice.rotulo == rotulo:
                
                # Retorna Falso em Caso de Falha
                return False

        # Se não existir

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

        # Imprime vértices
        for vertice in self.vertices:
            
            # Imprime o rótulo do vértice
            print(vertice.rotulo)

            # FALTA IMPRIMIR AS ARESTAS DE CADA VERTICE
                


            

    # INSERIR ARESTA
    def inserirAresta(self, origem, destino, peso):

        # Existe origem
        existe_origem = False

        # Verifica se o vértice de ORIGEM existe
        for vertice in self.vertices:

            # Se existir o Vértice ORIGEM no Grafo
            if vertice.origem == origem:

                existe_origem = True

                # Verifica se o vértice de DESTINO existe
                for vertice in self.vertices:

                    # Se existir o Vértice DESTINO no Grafo
                    if vertice.destino == destino:

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
        self.arestas = arestas

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