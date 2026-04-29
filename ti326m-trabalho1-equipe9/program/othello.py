import math
import copy # para copiar o board na função result
import time

W = 'W'
B = 'B'
EMPTY = None


class Othello:

    def __init__(self):
        
        self.board = [
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, W,     B,     EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, B,     W,     EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
        ]

    def player(self, board):
        #Jackeline - returns player who has the next turn on a board
    
        # conta quantas peças B e W existem no tabuleiro todo
        quantos_B = sum(linha.count(B) for linha in board)
        quantos_W = sum(linha.count(W) for linha in board)

        jogador_atual = B if quantos_B <= quantos_W else W
        outro_jogador = W if jogador_atual == B else B

        # verifica jogadas
        if self.acoes_por_jogador(board, jogador_atual):
            return jogador_atual
        elif self.acoes_por_jogador(board, outro_jogador):
            return outro_jogador
        else:
            return None # fim do jogo

    def acoes_por_jogador(self, board, jogador):
        #Jackeline
        # função que retorna as ações possíveis do jogador passado por parâmetro
        jogadas = set()

        for linha in range(8):
            for coluna in range(8):
                if board[linha][coluna] == EMPTY: # se o espaço atual for vazio
                    if self.OMovimentoEValido(board, linha, coluna, jogador):
                        jogadas.add((linha, coluna))

        return jogadas

    def actions(self, board):
        #Matheus - (returns set of all possible actions avaiable on the board)
        #encontra todas as jogadas possiveis no Othello
        jogadasPossiveis = set()
        jogadorAtual = self.player(board)

        # se não há jogador (fim do jogo), não há ações possíveis
        if jogadorAtual is None:
            return set()

        #preciso percorrer todo o tabuleiro
        for i in range(8):
            for j in range(8):
                if board[i][j] == EMPTY: #só vai jogar nas casas vazias
                    if self.OMovimentoEValido(board, i, j, jogadorAtual):
                        jogadasPossiveis.add((i, j))

        return jogadasPossiveis

        
        
    
    def result(self, board, action):
        #Jackeline - returns the board that results from making a move on the board
        
        if action not in self.actions(board): # verifica se a ação é válida antes de avançar
            raise ValueError("Ação inválida")

        novo_board = copy.deepcopy(board) # faz uma cópia completa do tabuleiro

        linha, coluna = action
        jogador = self.player(board)
        oponente = B if jogador == W else W

        novo_board[linha][coluna] = jogador

        direcoes = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),         (0,1),
            (1,-1),  (1,0), (1,1)
        ]

        for dl, dc in direcoes:             # percorre a lista direções
            i, j = linha + dl, coluna + dc  # caminha uma casa na direção atual
            pecas_para_virar = []           # peças do adversário que podem ser viradas

            while 0 <= i < 8 and 0 <= j < 8:        # para cada nova casa acessada
                if novo_board[i][j] == oponente:    # se tiver a peça do oponente
                    pecas_para_virar.append((i, j)) # adiciona em peças para virar
                    i += dl     # avança para a próxima casa na mesma direção
                    j += dc
                elif novo_board[i][j] == jogador:   # se tiver a peça do jogador atual
                    for x, y in pecas_para_virar:   # para cada casa em peças para virar
                        novo_board[x][y] = jogador  # as peças do oponente se tornam as dos jogador atual
                    break
                else:
                    break

        return novo_board
    
    def terminal(self, board):
        #Jackeline - returns True if game is over, False otherwise

        if not self.acoes_por_jogador(board, B) and not self.acoes_por_jogador(board, W):
            return True
        return False
    
    def utility(self, board):
        #Jackeline - returns 1 if B has won the game, -1 if W has won, 0 otherwise

        # conta a quantidade de cada peça
        quantos_B = sum(linha.count(B) for linha in board)
        quantos_W = sum(linha.count(W) for linha in board)

        # verifica qual peça está em maior quantidade
        if quantos_B > quantos_W:
            return 1
        if quantos_B < quantos_W:
            return -1
        else:
            return 0

    #função que verifica se o movimento de uma peça é válido
    def OMovimentoEValido(self, board, linha, coluna, player):
        '''
        Matheus
            condiçoes para a jogada ser válida:

            é em espaço vazio 

            cerca peças adversárias

            funciona em várias direções 

            tem pelo menos uma peça inimiga no meio
        '''
        #espaço vazio
        if board[linha][coluna] is not EMPTY:
            return False

        #adversario
        oponente = B if player == W else W

        #---------- direita ---------
        j = coluna + 1

        encontrou_oponente = False #verifica se encontrou inimigo no caminho

        # percorre enquanto estiver dentro do tabuleiro
        while j < 8:

            # se encontrar peça adversária, continua procurando
            if board[linha][j] == oponente:
                encontrou_oponente = True

            # se encontrar peça do jogador
            elif board[linha][j] == player:
                # só é válido se tiver pelo menos um inimigo antes
                if encontrou_oponente:
                    return True
                break  # se não tiver inimigo antes, para

            # se encontrar espaço vazio, não é válido
            else:
                break

            j += 1  # avança para a próxima posição

    
        #------------ esquerda ---------=

        #mesma lógica da direita mas pra esquerda
        j = coluna-1
        encontrou_oponente = False  # reseta

        while j >= 0:

            if board[linha][j] == oponente:
                encontrou_oponente = True

            elif board[linha][j] == player:
                if encontrou_oponente:
                    return True
                break

            else:
                break

            j -= 1  # anda para a esquerda


        #------------ para baixo ---------

        #faz começar na posição de baixo da peça que vai jogar
        i = linha + 1
        encontrou_oponente = False

        #percorre o tabuleiro
        while i < 8:
            if board[i][coluna] == oponente: #se encontrar inimigo contiua
                encontrou_oponente = True
            elif board[i][coluna] == player: 
                #se encontrar a própria peça, verifica se tem pelo menos um inimigo, se tiver então está cercado, então é true
                if encontrou_oponente:
                    return True
                break
            #espaço vazio
            else:
                break
            i += 1 #vai pro proximo

        #------------ para cima ---------

        #mesma lógica de baixo mas pra cima
        i = linha - 1
        encontrou_oponente = False

        while i >= 0:
            if board[i][coluna] == oponente:
                encontrou_oponente = True

            elif board[i][coluna] == player:
                if encontrou_oponente:
                    return True
                break
            else:
                break
            i -= 1

        #------------ diagonais ---------
        #diagonal esquerda pra baixo
        i, j = linha + 1, coluna - 1
        encontrou_oponente = False
        #mesmo esquema, só que agora tem que considerar tanto a linha quanto a coluna,
        # e as condições de parada são diferentes porque tem que considerar os limites do tabuleiro
    
        while i < 8 and j >= 0: 
            if board[i][j] == oponente:# se encontrar inimigo contiua
                encontrou_oponente = True
                # se encontrar a própria peça, verifica se tem pelo menos um inimigo, se tiver então está cercado, então é true
            elif board[i][j] == player:
                if encontrou_oponente:
                    return True
                break
            else:
                break
            #desce (i+1) e anda pra esquerda (j-1) ou seja - Diagonal, e vai pro proximo
            i += 1
            j -= 1


        #diagonal direita pra baixo
        i, j = linha + 1, coluna + 1
        #mesma lógica da diagonal esquerda pra baixo, só que agora anda pra direita.
        encontrou_oponente = False

        while i < 8 and j < 8:
            if board[i][j] == oponente:
                encontrou_oponente = True
            elif board[i][j] == player:
                if encontrou_oponente:
                    return True
                break
            else:
                break
            #pra direita agora
            i += 1
            j += 1

        
       
    
        #------------ diagonal esquerda pra cima ---------

        i, j = linha - 1, coluna - 1
        encontrou_oponente = False
        #Lógica ainda semelhante, só que agora tem que considerar os 
        # limites de cima e esquerda do tabuleiro
        while i >= 0 and j >= 0:
            if board[i][j] == oponente:
                encontrou_oponente = True
            elif board[i][j] == player:
                if encontrou_oponente:
                    return True
                break
            else:
                break
            i -= 1
            j -= 1

        #------------ diagonal direita pra cima ---------
        i, j = linha - 1, coluna + 1
        # mesma lógica da diagonal esquerda pra cima, 
        # só que agora tem que considerar os limites de cima e direita do tabuleiro
        encontrou_oponente = False

        while i >= 0 and j < 8:
            if board[i][j] == oponente:
                encontrou_oponente = True
            elif board[i][j] == player:
                if encontrou_oponente:
                    return True
                break
            else:
                break
            i -= 1
            j += 1
        
        # se nenhuma direção for válida
        return False


class Minimax:

    def __init__(self, game, heuristic, time_limit = 3.0, use_pruning = True):
        
        self.game = game
        self.heuristic = heuristic
        self.time_limit = time_limit
        self.use_pruning = use_pruning
        self.nodes_expanded = 0
        self.start_time = 0.0

    def run(self, state, depth = 4, alpha = -math.inf, beta = math.inf):
        #Jackeline - returns the optimal action for the current player on the state
        
        self.start_time = time.time()
        self.nodes_expanded = 0
        melhor_jogada = None
        melhor_valor = None

        # Iterative Deepening
        # a profundidade aumenta enquanto houver tempo
        profundidade = 1

        while True:
            if time.time() - self.start_time > self.time_limit:
                break

            jogador_inicial = self.game.player(state)
            maximizing = (jogador_inicial == B)
            valor, jogada = self._minimax(state, profundidade, maximizing, alpha, beta)

            if jogada is not None:
                melhor_jogada = jogada
                melhor_valor = valor

            profundidade += 1

        print("Melhor valor:", melhor_valor)
        print("Nós expandidos:", self.nodes_expanded)
        print("Tempo gasto:", time.time() - self.start_time)

        return melhor_jogada

        
    def _minimax(self, state, depth, maximizing, alpha, beta):

        self.nodes_expanded += 1

        if time.time() - self.start_time > self.time_limit:
            return self.heuristic(state), None

        if self.game.terminal(state):
            return self.game.utility(state), None

        if depth == 0:
            return self.heuristic(state), None

        # jogador MAX
        if maximizing:
            melhor_valor = -math.inf
            melhor_jogada = None

            for action in self.game.actions(state):
                novo_estado = self.game.result(state, action)

                valor, _ = self._minimax(novo_estado, depth - 1, False, alpha, beta)

                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = action

                #alpha-beta 
                if self.use_pruning:
                    alpha = max(alpha, melhor_valor)
                    if beta <= alpha:
                        break
                        

            return melhor_valor, melhor_jogada
            
    # jogador MIN
        else:
            pior_valor = math.inf
            pior_jogada = None

            for action in self.game.actions(state):
                novo_estado = self.game.result(state, action)

                valor, _ = self._minimax(novo_estado, depth - 1, True, alpha, beta)

                if valor < pior_valor:
                    pior_valor = valor
                    pior_jogada = action

                # alpha-beta pruning
                if self.use_pruning:
                    beta = min(beta, pior_valor)
                    if beta <= alpha:
                        break  # poda

            return pior_valor, pior_jogada



