"""
Achar menor caminho, possui 2 algoritmos de suporte:

INITIALIZE-SINGLE-SOURCE (lista G,vértice s) //G é um grafo ponderando (como lista de adjacências); s é vértice fonte
    for each 𝑣 ∈ 𝑉 do
        𝑑[𝑣] = ∞
        𝜋[𝑣] = NULL
    𝑑[s]= 0

RELAX (u, v, w) //keep calm and Relax
    if 𝑑 𝑣 > 𝑑 𝑢 + 𝑤(𝑢, 𝑣) then
        //caminho mais curto encontrado, atualizar
        𝑑[𝑣] = 𝑑 𝑢 + 𝑤(𝑢, 𝑣)
        𝜋[𝑣] = u

Dijkstra(lista G,vértice s) //G como lista de adjacências, ponderado (info em w); s é o vértice fonte
    INITIALIZE-SINGLE-SOURCE(G,s)

    𝑆 = ∅
    𝑄 = 𝑉 //𝑄 é a fila

    while 𝑄 ≠ ∅ do
        u = EXTRACT-MIN(Q)
        𝑆 = 𝑆 ∪ {𝑢}
        for each 𝑣 ∈ 𝐴𝑑𝑗[𝑢] do
            RELAX(u,v,w)
    return 𝑑, 𝜋 //𝑑 contém as distâncias de s a v; 𝜋 contém a árvore de caminhos mínimos

"""

import math

def Dijkstra(grafo, vertice):

    V = grafo.retornarElementos()

    distancia = []

    pai = []

    S = []

    Q = V

    for v in V:

        if v < len(distancia):
            distancia[v] = math.inf

        else:
            distancia.insert(v,math.inf)

        if v < len(pai):
            pai[v] = None
        else:
            pai.insert(v,None)
    
    distancia[vertice] = 0

    while len(Q) != 0:

        u = extrairMenor(Q, distancia)

        print(f"U:{u}, Adj[u]:{grafo.xRetornarElementos(u)}")

        S.append(u)

        print(f"S:{S}")
        for v in grafo.xRetornarElementos(u):
            
            relax(u,v, grafo, distancia, pai)
    
    pass

    return distancia, pai

# def inicizalizarFonte(distancia, pai, fonte, V):

#     for v in V:
#         distancia.insert(v,math.inf)
#         pai.insert(v, None)
    
#     distancia[fonte] = 0

def relax(u, v, grafo, distancia, pai):

    print("distancia: {} > {} == {}".format(distancia[v],distancia[u] + grafo.valorPeso(u,v),distancia[v] > distancia[u] + grafo.valorPeso(u,v)))

    if distancia[v] > distancia[u] + grafo.valorPeso(u,v):
        distancia[v] = distancia[u] + grafo.valorPeso(u,v)
        pai[v] = u

def extrairMenor(Q, distancia):

    menor = [ math.inf, 0 ]

    for indice, valor in enumerate(distancia):

        print(f"menor[0]({menor[0]}) > valor({valor}):{menor[0] > valor} and indice({indice}) in Q({Q}):{indice in Q}")

        if menor[0] > valor and indice in Q:
            menor = [valor, indice]

    print(menor, Q)

    return Q.pop(Q.index(menor[1]))