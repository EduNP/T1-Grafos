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

def Prim(Grafo, raiz):

    V = Grafo.retornarElementos()

    chave = [] 

    pai = []

    Q = []

    for u in V:

        chave.insert(u, math.inf)
        pai.insert(u, None)
        print(u)
        pass

    chave.insert(raiz, 0)

    Q = V

    while not Q ==  None:

        u = extrairMenor(Q)

        for v in Grafo.xRetornarElementos(u):

            print(u,v,Grafo.valorPeso(u,v),chave[v])
            if v in Q and Grafo.valorPeso(u,v) < chave[v]:
                pai.insert(v, u)
                chave.insert(v, Grafo.valorPeso(u,v))
                pass

            pass
        
        pass

    return pai
    
def extrairMenor(Q):

    menor = Q[0]

    for valor in Q:

        if menor > valor:
            menor = valor

    return menor