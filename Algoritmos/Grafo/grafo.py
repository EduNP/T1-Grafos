
class AdjuntaNo():
    def __init__(self, valor, peso):
        self.vertice = valor
        self.proximo = None
        self.peso = peso

class Grafo():
    def __init__(self, vertices):
        self.vertices = vertices
        self.lista = [None] * self.vertices #Lista de adjacencia do grafo

    def adicionarAresta(self, inicio, destino, peso):
        no = AdjuntaNo(destino, peso) #cria um novo no
        no.proximo = self.lista[inicio] #insere na lista de Inicio para destino
        self.lista[inicio] = no

        no = AdjuntaNo(inicio, peso)
        no.proximo = self.lista[destino] #insere na lsita de Destino para Inicio
        self.lista[destino] = no
    
    def valorPeso(self, inicio, destino):

        atual = self.lista[inicio]

        if atual == None:
            return 0

        while atual.vertice != destino:

            atual = atual.proximo
            if atual == None:
                break
        
        return atual.peso
    
    def retornarElementos(self):

        retorno = [i for i in range(0,len(self.lista))]

        return retorno

    def xRetornarElementos(self, elemento):

        lista = []
        
        lista.append(self.lista[elemento].vertice)

        proximo = self.lista[elemento].proximo

        while proximo != None:

            lista.append(proximo.vertice)
            proximo = proximo.proximo
 
        return lista