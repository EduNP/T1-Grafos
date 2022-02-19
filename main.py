from Algoritmos.BuscaLargura import *
from Algoritmos.Prim import *
from Algoritmos.Grafo.grafo import *

if __name__ == "__main__":

    G = Grafo(4)

    G.adicionarAresta(0,1,10)
    G.adicionarAresta(1,2,5)
    G.adicionarAresta(2,3,12)
    G.adicionarAresta(3,1,7)

    retorno = Prim(G,0)

    print(retorno)

    #Teste da BFS
    # grafo = Grafo(6)
    # grafo.adicionarAresta(0,1,0)
    # grafo.adicionarAresta(0,2,0)
    # grafo.adicionarAresta(1,3,0)
    # grafo.adicionarAresta(1,4,0)
    # grafo.adicionarAresta(2,4,0)
    # grafo.adicionarAresta(3,4,0)
    # grafo.adicionarAresta(3,5,0)
    # grafo.adicionarAresta(4,5,0)
    # d, pai = BFS(grafo,0)
    # PrintCaminho(grafo,pai,0,3)

    pass