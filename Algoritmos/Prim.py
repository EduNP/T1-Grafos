"""

Algoritmo pra gerar árvore minima

Prim(lista G, r) //G ponderado como lista de adjacências //r é o vértice raiz

    //Inicialização
    for each 𝑢 ∈ 𝑉 do
        key[u] = ∞
        𝜋[u] = NULL
    
    key[r] = 0 //Chave da raiz
  
    while 𝑄 ≠ ∅ do
        u = Extrai_Min(Q) //Pega 1º da fila
        for each v ∈ 𝐴𝑑𝑗[𝑢] do
            if v ∈ 𝑄 and W(u,v) < key[v] then //se vizinho está na fila e o peso da aresta for menor que a chave atual
            𝜋[v] = u //atualiza pai de U
            key[v] = W(u,v) //atualiza peso
    return 𝜋 //𝜋 contém a árvore geradora mínima

"""

import math

def Prim(grafo, raiz):

    V = grafo.retornarElementos()

    chave = [] 

    pai = []

    Q = []

    for u in V:

        # chave.insert(u, math.inf)
        # pai.insert(u, None)
        # pass

        if u < len(chave):
            chave[u] = math.inf
        else:
            chave.insert(u,math.inf)

        if u < len(pai):
            pai[u] = None
        else:
            pai.insert(u,None)

    chave[raiz] = 0

    Q = V

    while not len(Q) == 0:

        u = extrairMenor(Q, chave)

        for v in grafo.xRetornarElementos(u):

            if v in Q and grafo.valorPeso(u,v) < chave[v]:
                pai[v] = u
                chave[v] = grafo.valorPeso(u,v)
                pass

            pass
        
        pass

    return [pai]
    
def extrairMenor(Q, chave):

    menor = [ math.inf, 0 ]

    for indice, valor in enumerate(chave):

        if menor[0] > valor and indice in Q:
            menor = [valor, indice]

    return Q.pop(Q.index(menor[1]))