# //BFS(lista G, vértice s) //s é o vértice fonte //G como lista de adjacências

# //Inicialização
# // for each 𝑢 ∈ 𝑉 − {𝑠} do{
# //     cor[u] = branca
# //     d[u] = ∞
# //     𝜋[u] = NULL
# // }
# //  
# // cor[s] = cinza
# // d[s] = 0
# // 𝜋[s] = NULL

# // 𝑄 = ∅ //𝑄 é a fila
# // ENQUEUE(Q,s) -> Enfileira vértice fonte na fila Q

# // while 𝑄 ≠ ∅ do //Enquanto fila não vazia
# //     u = DEQUEUE(Q) //tira vertice da fila
# //     for each 𝑣 ∈ 𝐴𝑑𝑗[𝑢] do 
# //         if (cor[v] == branca) then
# //             cor[v] = cinza
# //             d[v] = d[u] + 1
# //             𝜋[v] = u
# //     ENQUEUE(Q,v)
# //     cor[u] = preta

# // return 𝑑, 𝜋 //𝑑 contém as distâncias de s a v; 𝜋 contém a árvore BFS

import math


class AdjuntaNo():
    def __init__(self, valor):
        self.vertice = valor
        self.proximo = None

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [None] * self.vertices #Lista de adjacencia do grafo

    def adicionarAresta(self, inicio, destino):
        no = AdjuntaNo(destino) #cria um novo no
        no.proximo = self.grafo[inicio] #insere na lista de Inicio para destino
        self.grafo[inicio] = no

        no = AdjuntaNo(inicio)
        no.proximo = self.grafo[destino] #insere na lsita de Destino para Inicio
        self.grafo[destino] = no

def BFS(grafo, vertice):
    # for u in range(grafo.numV):
    #     print("Vertice" + str(u) + " : ")
    #     noAux = grafo.grafo[u]
    #     while noAux:
    #         print(" -> {}".format(noAux.vertice))
    #         noAux = noAux.next
    cor = []
    d = []
    pai = []

    for i in range(grafo.numV):
        if i != vertice:
            cor.insert(i,"branco")
            d.insert(i, math.inf)
            pai.insert(i, None)
    
    cor.insert(vertice,"cinza")
    d.insert(vertice,0)
    pai.insert(vertice,None)

    Q = []
    Q.append(vertice)
    while len(Q) != 0:
        u = Q.pop
        

if __name__ == "__main__":
    
    graph = Grafo(3)
    graph.adicionarAresta(0,1)
    graph.adicionarAresta(1,2)

    BFS(graph,0)
