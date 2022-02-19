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

        chave.insert(u, math.inf)
        pai.insert(u, None)
        pass

    chave[raiz] = 0

    Q = V

    while not len(Q) == 0:

        u = extrairMenor(Q)

        for v in grafo.xRetornarElementos(u):

            if v in Q and grafo.valorPeso(u,v) < chave[v]:
                pai[v] = u
                chave[v] = grafo.valorPeso(u,v)
                pass

            pass
        
        pass

    return pai
    
def extrairMenor(Q):

    menor = [ Q[0], 0 ]

    for indice, valor in enumerate(Q):

        if menor[0] > valor:
            menor = [valor, indice]

    del Q[menor[1]]

    return menor[0]