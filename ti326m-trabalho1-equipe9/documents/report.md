# Modelagem formal do problema

## Othello

O Othello é um jogo de tabuleiro competido em uma grade 8×8 por dois jogadores. Utilizam-se peças com duas faces, uma preta e outra branca, e o objetivo e o objetivo do jogo é terminar a partida com o maior número de peças viradas para a cor do jogador.

A partida inicia-se com quatro peças posicionadas no centro do tabuleiro: duas com a face preta apontada para cima e duas com a face branca, dispostas em diagonal. O jogador que opera as peças pretas realiza a primeira jogada.

As jogadas consistem em posicionar uma peça no tabuleiro de forma que ela flanqueie peças adversárias, ou seja, a peça colocada deve criar uma linha (horizontal, vertical ou diagonal) na qual exista pelo menos uma peça do oponente entre a nova peça e outra peça da mesma cor já presente no tabuleiro. Todas as peças adversárias flanqueadas são então viradas para a cor do jogador da vez.

Os jogadores alternam suas jogadas até que nenhum deles tenha movimentos válidos ou não haja mais espaços disponíveis no tabuleiro, momento em que a partida se encerra.

## Modelagem 

O estado do jogo é representado por uma matriz 8x8, na qual cada posição pode valer:
- "B", representando as peças pretas;
- "W", representando as peças brancas;
- None para as posições vazias.

Um estado é considerado terminal quando nenhum dos dois jogadores possui jogadas válidas.

O jogador atual é definido com base na quantidade de peças no tabuleiro e na existência de jogadas possíveis. O turno é automaticamente passado ao adversário caso o jogador atual não possua movimentos válidos.

Cada ação corresponde a uma posição válida do tabuleiro onde o jogador atual pode inserir uma peça. Uma ação é representada por um par ordenado (linha, coluna), indicando a posição da jogada na matriz.

A função de transição, ou seja, que atualiza o estado atual do jogo, recebe um estado e uma ação e retorna um novo estado. Ao aplicar uma ação, a peça do jogador atual é posicionada no tabuleiro e todas as peças adversárias flanqueadas são convertidas para a cor do jogador.

A função utility avalia o estado final do jogo com base na contagem de peças no tabuleiro. Após o jogo terminal, ela retorna 1, caso o jogador 'B' vença; -1 caso o jogador 'W' vença; e 0 caso haja empate.

### Observações sobre a implementação

Durante o desenvolvimento, foi necessário compreender na prática como as funções do modelo se relacionam.

A função de ações (`actions`) inicialmente parecia ser uma das partes mais complexas, porém sua implementação foi simplificada com a criação de uma função auxiliar responsável por validar movimentos. Isso permitiu separar a lógica de verificação das regras do jogo da lógica de geração de jogadas.

Já a função de transição (`result`) gerou dúvidas iniciais, pois foi necessário entender que ela não representa a continuidade real da partida, mas sim uma simulação de uma jogada a partir de um estado. Esse comportamento é essencial para o funcionamento de algoritmos de busca, como o minimax, que dependem da exploração de estados futuros possíveis.

# Busca adversarial

## Minimax
O Minimax é uma técnica de busca de caminhos utilizada em jogos de dois jogadores, onde um jogador tenta maximizar seu ganho enquanto o outro tenta minimizar o resultado do adversário.

O funcionamento do algoritmo é baseado na exploração de possíveis jogadas futuras por meio de recursão. A cada nível da árvore de decisão:
- Um nível representa o jogador MAX (a inteligência artificial), que busca o maior valor possível.
- O nível seguinte representa o jogador MIN (o adversário), que busca o menor valor possível.

O algoritmo percorre a árvore de possibilidades até um determinado limite (profundidade) ou até o fim do jogo. Ao final, cada estado do jogo é avaliado por uma função de avaliação, que atribui um valor numérico representando o quão favorável aquele estado é.

Com base nesses valores, o algoritmo propaga os resultados de volta pela árvore, permitindo que a inteligência artificial escolha a jogada que leva ao melhor cenário possível, considerando que o adversário também fará jogadas ótimas.

No contexto deste projeto, o algoritmo minimax foi integrado às funções já implementadas do jogo, utilizando:

- `actions` para gerar jogadas possíveis
- `result` para simular estados futuros
- `terminal` para identificar fim de jogo
- `utility` ou heurística para avaliação dos estados

Durante o desenvolvimento, houve dificuldade inicial em compreender como essas funções se conectavam dentro do algoritmo, principalmente na ideia de que o minimax não executa jogadas reais, mas sim simula possíveis cenários para tomar decisões.

### Iterative deepening
Iterative deepening é uma técnica que consiste em executar o algoritmo minimax repetidamente, aumentando gradualmente o limite de profundidade da busca.

A cada iteração, a melhor jogada encontrada até o momento é atualizada. Isso permite que o algoritmo sempre tenha uma solução disponível, mesmo que o tempo de execução seja interrompido.

Essa abordagem é especialmente útil quando há limitação de tempo, pois garante respostas progressivamente melhores.

Inicialmente, houve dificuldade em compreender a função do iterative deepening em relação ao minimax. Com o avanço do desenvolvimento, foi possível entender que essa técnica não altera o funcionamento do algoritmo em si, mas controla a profundidade da busca ao longo do tempo, permitindo obter respostas progressivamente melhores.

### Alpha-beta pruning
Alpha-beta pruning é uma otimização do algoritmo minimax que reduz o número de nós explorados na árvore de busca.

A técnica funciona mantendo dois valores durante a execução:

- alpha (α): o melhor valor já encontrado pelo jogador MAX
- beta (β): o melhor valor já garantido para o jogador MIN

Durante a exploração da árvore, quando se identifica que um determinado ramo não pode produzir um resultado melhor do que os já encontrados, esse ramo é descartado, evitando cálculos desnecessários.

Isso torna o algoritmo mais eficiente, permitindo analisar maiores profundidades em menos tempo, sem alterar o resultado final do minimax.

Também houve um período de compreensão sobre como o alpha-beta pruning se diferencia do minimax tradicional. Foi entendido que essa técnica atua como uma otimização, reduzindo o número de estados analisados ao eliminar ramos que não influenciam na decisão final, mantendo o mesmo resultado do algoritmo original.

# Experimentos computacionais (testes e discussão)

Foram realizados testes iniciais para validar a implementação das regras do jogo, especialmente as funções `actions` e `result`.

Durante esses testes, foi possível verificar:
- Se as jogadas geradas eram válidas de acordo com as regras do Othello
- Se a simulação de jogadas estava convertendo corretamente as peças adversárias

Os testes também ajudaram a identificar e corrigir erros de lógica, principalmente relacionados à verificação de direções e à aplicação das regras de captura.

Com a implementação da inteligência artificial, novos testes serão realizados para analisar o comportamento do algoritmo minimax, comparando desempenho com e sem otimizações.

# Conclusão

O desenvolvimento do projeto permitiu aplicar na prática conceitos de inteligência artificial, especialmente relacionados à busca adversarial.

Além da implementação do jogo Othello, foi possível compreender como algoritmos como o minimax utilizam simulações de estados para tomada de decisão.

Durante o processo, algumas dificuldades foram enfrentadas, principalmente na compreensão da relação entre as funções do jogo e os algoritmos de busca, bem como na diferenciação entre minimax, iterative deepening e alpha-beta pruning.

Essas dificuldades foram importantes para aprofundar o entendimento dos conceitos e melhorar a qualidade da implementação.
