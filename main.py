from Algoritmos.BuscaLargura import *
from Algoritmos.Dijkstra import Dijkstra
from Algoritmos.Prim import *
from Algoritmos.Grafo.grafo import *
from Algoritmos.Prufer import *


if __name__ == "__main__":

    # G = Grafo(4)

    # G.adicionarAresta(0,1,10)
    # G.adicionarAresta(1,2,5)
    # G.adicionarAresta(2,3,12)
    # G.adicionarAresta(3,1,7)

    # retorno = Prim(G,0)

    # print(retorno)

    #Teste Prufer
    G = Grafo(6)
    G.adicionarAresta(3,0,0)
    G.adicionarAresta(3,1,0)
    G.adicionarAresta(3,2,0)
    G.adicionarAresta(3,4,0)
    G.adicionarAresta(4,5,0)
    G.show()
    s = codigoPrufer(G)
    for i in range(len(s)):
        print(s[i])

    T = decodificadorPrufer(s)
    T.show()
    
    #Teste da BFS
    grafo = Grafo(6)
    grafo.adicionarAresta(0,1,0)
    grafo.adicionarAresta(0,2,0)
    grafo.adicionarAresta(1,3,0)
    grafo.adicionarAresta(1,4,0)
    grafo.adicionarAresta(2,4,0)
    grafo.adicionarAresta(3,4,0)
    grafo.adicionarAresta(3,5,0)
    grafo.adicionarAresta(4,5,0)

    d, pai = BFS(grafo,0)
    print("Vetor D:", d)
    print("Vetor pai:", pai)
    PrintCaminho(grafo,pai,0,3)
    grafo.show()


    # distancia, pai = Dijkstra(G, 0)

    # print(distancia, pai)

    pass