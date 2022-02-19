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

    pass