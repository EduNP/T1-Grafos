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

import Grafo

def Dijkstra():

    pass