from Algoritmos.BuscaLargura import *
from Algoritmos.Dijkstra import Dijkstra
from Algoritmos.Prim import *
from Algoritmos.Grafo.grafo import *
from Algoritmos.Prufer import *


def teste(chars, lista, comeco,algoritmo, mostrar=False):

    G = Grafo(len(chars))

    inv_chars = {chars[k] : k for k in chars}

    for elemento in lista:
        G.adicionarAresta(*elemento)
    
    retorno = algoritmo(G,chars[comeco])

    if mostrar:

        G.show(inv_chars)

        nG = Grafo(len(retorno[0]))

        for i in range(0,len(retorno[0])):
            if retorno[0][i] != None:
                nG.adicionarAresta(retorno[0][i],i,G.valorPeso(retorno[0][i],i))

        nG.show(inv_chars)
    

    return retorno

def testeDigrafo(chars, lista, comeco, algoritmo, mostrar=False):

    G = Grafo(len(chars))

    inv_chars = {chars[k] : k for k in chars}

    for elemento in lista:
        G.adicionarArestaDigrafo(*elemento)
    
    retorno  = algoritmo(G,chars[comeco])

    if mostrar:

        G.showDigrafo(inv_chars)

        nG = Grafo(len(retorno[0]))

        for i in range(0,len(retorno[0])):
            if retorno[0][i] != None:
                nG.adicionarArestaDigrafo(retorno[0][i],i,G.valorPeso(retorno[0][i],i))

        nG.showDigrafo(inv_chars)
    

    return retorno

def retornarCasosDijkstra():

    casos = []

    chars = {'s':0,'r':1,'u':2,'w':3,'v':4,'t':5}

    pesos = [
        (chars['s'],chars['r'],10),(chars['s'],chars['u'],5),(chars['r'],chars['u'],2),
        (chars['u'],chars['r'],3),(chars['r'],chars['w'],1),(chars['u'],chars['v'],2),
        (chars['u'],chars['w'],9),(chars['w'],chars['v'],4),(chars['v'],chars['w'],6),
        (chars['w'],chars['t'],2),(chars['v'],chars['t'],5)
    
    ]

    casos.append([chars,pesos])

    chars = {'s':0,'t':1,'x':2,'y':3,'z':4}

    pesos = [
        (chars['s'],chars['t'],6),(chars['s'],chars['y'],7),(chars['t'],chars['y'],8),
        (chars['t'],chars['z'],-4),(chars['t'],chars['x'],5),(chars['y'],chars['x'],-3),
        (chars['y'],chars['z'],9),(chars['x'],chars['t'],-2),(chars['z'],chars['x'],7),
        (chars['z'],chars['s'],2)
    
    ]

    casos.append([chars,pesos])


    return casos

def retornarCasosPrim():

    casos = []

    chars = {'a':0,'b':1,'c':2}

    pesos = [
        (chars['a'],chars['b'],5),(chars['b'],chars['c'],5),(chars['a'],chars['c'],8)

    ]

    casos.append([chars,pesos])

    chars = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}

    pesos = [
        (chars['a'],chars['b'],4),(chars['a'],chars['h'],8),
        (chars['b'],chars['h'],11),(chars['b'],chars['c'],8),
        (chars['h'],chars['i'],7),(chars['h'],chars['g'],1),
        (chars['c'],chars['i'],2),(chars['c'],chars['f'],4),
        (chars['g'],chars['i'],6),(chars['g'],chars['f'],2),
        (chars['e'],chars['f'],10),(chars['e'],chars['d'],9),
        (chars['d'],chars['c'],7),(chars['d'],chars['f'],14)
    
    ]

    casos.append([chars,pesos])

    chars = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}

    pesos = [
        (chars['a'],chars['b'],6),(chars['a'],chars['c'],3),
        (chars['a'],chars['e'],9),(chars['b'],chars['d'],2),
        (chars['b'],chars['c'],4),(chars['c'],chars['d'],2),
        (chars['c'],chars['e'],9),(chars['c'],chars['f'],9),
        (chars['d'],chars['f'],8),(chars['e'],chars['f'],8)
    
    ]

    casos.append([chars,pesos])

    return casos

def executarCasos(testeTipo, casos, algoritmo):

    for caso in casos:

        print(f"Nós: {caso[0].keys()}")

        raiz = input("Digite a raiz:")

        if raiz in caso[0]:

            retorno = testeTipo(caso[0],caso[1],raiz,algoritmo, mostrar=True)

            print(retorno)
        else:

            print("raiz não encontrada!")


if __name__ == "__main__":


    casos = []

    chars = {'a':0,'b':1,'c':2}

    pesos = [
        (chars['a'],chars['b'],5),(chars['b'],chars['c'],5),(chars['a'],chars['c'],8)

    ]

    casos.append([chars,pesos])

    executarCasos(testeDigrafo,retornarCasosDijkstra(),Dijkstra)

    executarCasos(teste,casos,Dijkstra)

    executarCasos(teste,retornarCasosPrim(),Prim)

