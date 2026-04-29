from othello import Othello, Minimax, B, W

# contabiliza a diferença de peças
def heuristica(tabuleiro):
    quantos_B = sum(linha.count(B) for linha in tabuleiro)
    quantos_W = sum(linha.count(W) for linha in tabuleiro)
    return quantos_B - quantos_W

def desenha_tabuleiro(tabuleiro):


   for linha in tabuleiro:
       linha_formatada = []
      
       for casa in linha:
           if casa == 'B':
               linha_formatada.append("  B  ")
           else:
               linha_formatada.append("  W  ")


def main():
    jogo = Othello()
    tabuleiro = jogo.board

    B = Minimax(jogo, heuristica)
    W = Minimax(jogo, heuristica)

    opcao = -1
    while opcao != 0:
        print("--    OTHELLO    --")
        print("0 - Sair do jogo")
        print("1 - Modo IA vs IA")
        print("2 - Modo IA vs Humano")

        opcao = input("Opção: ")
        match opcao:
            case 1: modo_ia_vs_ia(jogo, tabuleiro, B, W)
            case 2: modo_ia_vs_humano(jogo, tabuleiro, B, W)
        

if __name__ == "__main__":
    main()
