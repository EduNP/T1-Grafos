import math

def BFS(grafo, vertice):
    cor = []
    d = []
    pai = []

    for i in range(grafo.vertices):
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
        u = Q.pop()
        auxVertice = grafo.lista[u]
        while auxVertice != None:
            if cor[auxVertice.valor] == "branco":
                cor[auxVertice.valor] = "cinza"
                d[auxVertice.valor] = d[u] + 1
                pai[auxVertice.valor] = u
                Q.append(auxVertice.valor)
            auxVertice = auxVertice.proximo
        cor[u] = "preto"

    return d, pai

def PrintCaminho(grafo, pai, inicio, destino):
    if inicio == destino:
        print(inicio)
    else:
        if pai[destino] == None:
            print("Não existe caminho de s a v")
        else:
            PrintCaminho(grafo, pai, inicio, pai[destino])
            print(destino)
