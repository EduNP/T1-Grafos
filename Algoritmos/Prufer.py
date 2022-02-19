from Algoritmos.Grafo.grafo import Grafo

#grafo como arvore 
def codigoPrufer(grafo):
    s = []
    visitados = set()
    
    for j in range(len(grafo.lista)-2):
        #procura menor folha
        folha = -1
        for i in range(len(grafo.lista)):
            if i not in visitados:
                if len(grafo.xRetornarElementos(i)) == 1:
                    folha = i
                    break
        if folha == -1:
            print("Não há nó folha")
            return None
        s.append(grafo.lista[folha].vertice)
        visitados.add(folha)
    return s

def decodificadorPrufer(s):
    n = len(s)
    T = Grafo(n+2)

    d = []
    for i in range(n+2):
        d.append(1)
    
    for j in s:
        d[j] += 1
    
    for k in s:
        for l in T.retornarElementos():
            if d[l] == 1:
                T.adicionarAresta(l,k,0)
                d[l] -= 1
                d[k] -= 1
                break
    
    u = v = 0

    for i in T.retornarElementos():
        if d[i] == 1:
            if u == 0:
                u = i
            else:
                v = i
                break
    T.adicionarAresta(u,v,0)
    return T