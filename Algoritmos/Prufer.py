"""
Possui 2 partes, codificação e decodificação

encoderPrufer(T) //T é uma árvore com vértices rotulados {1, 2, ..., n}
    for i = 1 to 𝑛 − 2 do
        procurar vértice v terminal (folha) com menor em rótulo em T
        u = vértice vizinho de v
        s[i] = u
        T = T – {v} //remove o vértice v da árvore
    return 𝑠 //𝑠 contém a sequência de Prüfer

decoderPrufer(s) //s é o vetor com o código de Prüfer
    n = length(s)
    T = criarGrafo(n+2) //grafo com n+2 vértices isolados rotulados de 1 a n+2

    for each i in T do
        d[i] = 1

    for each j in s do //d armazenará o grau de cada vértice
        d[j] = d[j] + 1

    for each j in s do
        for each i in T do //ordem crescente
            if d[i] == 1 then
                insereAresta(i,j,T) //aresta (i,j) em T
                d[i] = d[i] – 1
                d[j] = d[j] - 1
                break

        u = v = 0
       
        for each i in T do //procura arestas que sobraram com grau 1
       
        if d[i] == 1 then
            if u == 0 then
                u = i
            else
                v = i
            break
        insereAresta(u,v,T)
        return 𝑇 //𝑇 contém a árvore reconstruída

"""