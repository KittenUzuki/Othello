# Trabalho 1 de TI326 - Inteligência Artificial

## Integrantes

* Matheus Ferreira Fagundes
* Jackeline Cristina da Silva Ribeiro
* Yasmin Victoria Lopes da Silva

## Descrição

Este projeto tem como objetivo a implementação do jogo Othello (Reversi) juntamente com uma inteligência artificial baseada em algoritmos de busca adversarial.

O jogo foi desenvolvido considerando suas regras oficiais, incluindo a validação de jogadas, alternância de turnos, captura de peças em múltiplas direções e verificação de fim de jogo.

Além da parte lógica do jogo, também está sendo desenvolvido um agente inteligente capaz de tomar decisões de forma automática. Para isso, será utilizado o algoritmo Minimax, com melhorias através das técnicas de Alpha-Beta Pruning e Iterative Deepening, visando aumentar a eficiência da busca e permitir análises mais profundas dentro de um tempo limitado.

O problema foi modelado formalmente como (S, A, T, U), permitindo a aplicação estruturada dos algoritmos de tomada de decisão.

## Como executar

Para executar o projeto, é necessário ter o Python instalado (versão 3.10 ou superior).

No terminal, siga os passos abaixo:

1. Acesse a pasta do projeto:

cd ti326m-trabalho1-equipe9


2. Execute o arquivo principal:

python program/othello.py


Ao executar o programa, serão exibidas no terminal informações como:
- Jogador atual
- Jogadas possíveis
- Resultado das jogadas aplicadas no tabuleiro

Esses testes permitem validar se a lógica do jogo está funcionando corretamente.

## Estrutura do projeto

- `program/othello.py`: implementação do jogo, incluindo regras, validação de jogadas e base do algoritmo Minimax  
- `relatorio.md`: relatório detalhado contendo modelagem formal, explicação dos algoritmos e análises  
- `README.md`: documentação geral do projeto  

## Observações

O desenvolvimento foi realizado de forma incremental, com divisão equilibrada entre os integrantes do grupo. Cada parte do código foi construída com foco no entendimento da lógica, garantindo que todos os membros compreendessem o funcionamento do sistema.

O projeto será finalizado até dia 07/04, terça-feira.
