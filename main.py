from Algoritmos.BuscaLargura import *
from Algoritmos.Dijkstra import Dijkstra
from Algoritmos.Prim import *
from Algoritmos.Grafo.grafo import *
from Algoritmos.Prufer import *


if __name__ == "__main__":

    G = Grafo(3)

    pesos = [5,5,9]

    G.adicionarAresta(0,1,pesos[0])
    G.adicionarAresta(1,2,pesos[1])
    G.adicionarAresta(0,2,pesos[2])

    distancia, retorno  = Dijkstra(G,0)

    print(retorno, distancia)

    G.show()

    nG = Grafo(len(retorno))

    for i in range(0,len(retorno)):
        if retorno[i] != None:
            nG.adicionarAresta(i,retorno[i],G.valorPeso(i,retorno[i]))

    nG.show()

    retorno = Prim(G,0)

    print(retorno)

    G.show()

    nG = Grafo(len(retorno))

    for i in range(0,len(retorno)):
        if retorno[i] != None:
            nG.adicionarAresta(i,retorno[i],G.valorPeso(i,retorno[i]))

    nG.show()

    # #Teste Prufer
    # G = Grafo(6)
    # G.adicionarAresta(3,0,0)
    # G.adicionarAresta(3,1,0)
    # G.adicionarAresta(3,2,0)
    # G.adicionarAresta(3,4,0)
    # G.adicionarAresta(4,5,0)
    # G.show()
    # s = codigoPrufer(G)
    # for i in range(len(s)):
    #     print(s[i])

    # T = decodificadorPrufer(s)
    # T.show()
    
    # #Teste da BFS
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
    # print("Vetor D:", d)
    # print("Vetor pai:", pai)
    # PrintCaminho(grafo,pai,0,3)
    # grafo.show()


    # distancia, retorno  = Dijkstra(grafo,3)

    # print(retorno, distancia)

    # grafo.show()

    # nG = Grafo(len(retorno))

    # for i in range(0,len(retorno)):
    #     if retorno[i] != None:
    #         nG.adicionarAresta(i,retorno[i],grafo.valorPeso(i,retorno[i]))

    # nG.show()

    # distancia, pai = Dijkstra(G, 0)

    # print(distancia, pai)

    pass