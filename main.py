from Algoritmos.BuscaLargura import *
from Algoritmos.Dijkstra import Dijkstra
from Algoritmos.Prim import *
from Algoritmos.Grafo.grafo import *
from Algoritmos.Prufer import *

if __name__ == "__main__":

    #Teste Dijkstra
    G = Grafo(6)


    chars = {'s':0,'r':1,'u':2,'w':3,'v':4,'t':5}

    inv_chars = {chars[k] : k for k in chars}

    G.adicionarArestaDigrafo(chars['s'],chars['r'],10)
    G.adicionarArestaDigrafo(chars['s'],chars['u'],5)
    G.adicionarArestaDigrafo(chars['r'],chars['u'],2)
    G.adicionarArestaDigrafo(chars['u'],chars['r'],3)
    G.adicionarArestaDigrafo(chars['r'],chars['w'],1)
    G.adicionarArestaDigrafo(chars['u'],chars['v'],2)
    G.adicionarArestaDigrafo(chars['u'],chars['w'],9)
    G.adicionarArestaDigrafo(chars['w'],chars['v'],4)
    G.adicionarArestaDigrafo(chars['v'],chars['w'],6)
    G.adicionarArestaDigrafo(chars['w'],chars['t'],3)
    G.adicionarArestaDigrafo(chars['v'],chars['t'],5)

    distancia, retorno  = Dijkstra(G,chars['u'])

    print(retorno, distancia)

    G.showDigrafo(inv_chars)

    nG = Grafo(len(retorno))

    for i in range(0,len(retorno)):
        if retorno[i] != None:
            nG.adicionarArestaDigrafo(retorno[i],i,G.valorPeso(retorno[i],i))

    nG.showDigrafo(inv_chars)

    # retorno = Prim(G,0)

    # print(retorno)

    # G.show()

    # nG = Grafo(len(retorno))

    # for i in range(0,len(retorno)):
    #     if retorno[i] != None:
    #         nG.adicionarAresta(i,retorno[i],G.valorPeso(i,retorno[i]))

    # nG.show()

    # #Teste Prufer
    # print("Teste 1 - Prufer:")
    # GP = Grafo(6)
    # GP.adicionarAresta(3,0,0)
    # GP.adicionarAresta(3,1,0)
    # GP.adicionarAresta(3,2,0)
    # GP.adicionarAresta(3,4,0)
    # GP.adicionarAresta(4,5,0)
   
    # s = codigoPrufer(GP)
    # print("Codigo de prufer:")
    # for i in range(len(s)):
    #     print(s[i])

    # GP.show()
    # T = decodificadorPrufer(s)
    # T.show()
    
    # print("Teste 2 - Prufer:")
    # GP2 = Grafo(6)
    # GP2.adicionarAresta(3,0,0)
    # GP2.adicionarAresta(3,1,0)
    # GP2.adicionarAresta(3,4,0)
    # GP2.adicionarAresta(4,2,0)
    # GP2.adicionarAresta(4,5,0)
   
    # s2 = codigoPrufer(GP2)
    # print("Codigo de prufer:")
    # for i in range(len(s2)):
    #     print(s2[i])

    # GP2.show()
    # T2 = decodificadorPrufer(s2)
    # T2.show()


    # #Teste da Busca Largura
    # print("Teste 1 - BFS:")
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
    # print("Caminho de 0 até 3:")
    # PrintCaminho(grafo,pai,0,3)
    # grafo.show()

    # print("Teste 2 - BFS:")
    # grafo2 = Grafo(6)
    # grafo2.adicionarAresta(0,1,0)
    # grafo2.adicionarAresta(0,4,0)
    # grafo2.adicionarAresta(1,2,0)
    # grafo2.adicionarAresta(1,4,0)
    # grafo2.adicionarAresta(2,3,0)
    # grafo2.adicionarAresta(3,4,0)
    # grafo2.adicionarAresta(3,5,0)

    # d2, pai2 = BFS(grafo2,0)
    # print("Vetor D:", d2)
    # print("Vetor pai:", pai2)
    # print("Caminho de 1 até 5:")
    # PrintCaminho(grafo2,pai2,1,5)
    # grafo2.show()

    # # distancia, retorno  = Dijkstra(grafo,3)

    # # print(retorno, distancia)

    # # grafo.show()

    # # nG = Grafo(len(retorno))

    # # for i in range(0,len(retorno)):
    # #     if retorno[i] != None:
    # #         nG.adicionarAresta(i,retorno[i],grafo.valorPeso(i,retorno[i]))

    # # nG.show()

    # # distancia, pai = Dijkstra(G, 0)

    # # print(distancia, pai)

    # pass