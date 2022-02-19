//BFS(lista G, vértice s) //s é o vértice fonte //G como lista de adjacências

//Inicialização
// for each 𝑢 ∈ 𝑉 − {𝑠} do{
//     cor[u] = branca
//     d[u] = ∞
//     𝜋[u] = NULL
// }
//  
// cor[s] = cinza
// d[s] = 0
// 𝜋[s] = NULL
// 𝑄 = ∅ //𝑄 é a fila
// ENQUEUE(Q,s) -> Enfileira vértice fonte na fila Q

// while 𝑄 ≠ ∅ do //Enquanto fila não vazia
//     u = DEQUEUE(Q) //tira vertice da fila
//     for each 𝑣 ∈ 𝐴𝑑𝑗[𝑢] do 
//         if (cor[v] == branca) then
//             cor[v] = cinza
//             d[v] = d[u] + 1
//             𝜋[v] = u
//     ENQUEUE(Q,v)
//     cor[u] = preta

// return 𝑑, 𝜋 //𝑑 contém as distâncias de s a v; 𝜋 contém a árvore BFS