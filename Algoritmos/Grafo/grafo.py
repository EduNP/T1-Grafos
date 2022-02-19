
class AdjuntaNo():
    def __init__(self, valor):
        self.vertice = valor
        self.proximo = None

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.lista = [None] * self.vertices #Lista de adjacencia do grafo

    def adicionarAresta(self, inicio, destino):
        no = AdjuntaNo(destino) #cria um novo no
        no.proximo = self.lista[inicio] #insere na lista de Inicio para destino
        self.lista[inicio] = no

        no = AdjuntaNo(inicio)
        no.proximo = self.lista[destino] #insere na lsita de Destino para Inicio
        self.lista[destino] = no