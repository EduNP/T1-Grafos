//Algoritmo pra gerar árvore minima

// Prim(lista G, r) //G ponderado como lista de adjacências //r é o vértice raiz

//     //Inicialização
//     for each 𝑢 ∈ 𝑉 do
//         key[u] = ∞
//         𝜋[u] = NULL
    
//     key[r] = 0 //Chave da raiz
  
//     while 𝑄 ≠ ∅ do
//         u = Extrai_Min(Q) //Pega 1º da fila
//         for each v ∈ 𝐴𝑑𝑗[𝑢] do
//             if v ∈ 𝑄 and W(u,v) < key[v] then //se vizinho está na fila e o peso da aresta for menor que a chave atual
//             𝜋[v] = u //atualiza pai de U
//             key[v] = W(u,v) //atualiza peso
//     return 𝜋 //𝜋 contém a árvore geradora mínima
