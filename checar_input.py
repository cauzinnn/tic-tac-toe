def jogada_valida(jogo,jogada):
    '''função que analisa se a jogada que o jogador deseja fazer está de acordo
        com os padrões estabelecidos no jogo e/ou se ela não é igual a jogadas
        anteriores. list,str -> bool'''
    if (jogada[0]!="[" or jogada[2]!="," or jogada[4]!="]" or jogada[1] not in "0123" or
        jogada[3] not in "0123" or jogo[int(jogada[1])][int(jogada[3])]!="-"):
        return False
    else:
        return True

    
def teste_jogada_valida():
    print(jogada_valida([['X','X','O','X'], ['O','X','O','O'], ['X','-','-','X'], ['-','-','-','O']],'[3,0]')==True)
    print(jogada_valida([['X','X','O','X'], ['O','X','O','O'], ['X','-','-','X'], ['-','-','-','O']],'(3,0)')==False)
    print(jogada_valida([['X','X','O','X'], ['O','X','O','O'], ['X','-','-','X'], ['-','-','-','O']],'[3 0]')==False)
    print(jogada_valida([['X','X','O','X'], ['O','X','O','O'], ['X','-','-','X'], ['-','-','-','O']],'[4,6]')==False)
    print(jogada_valida([['X','X','O','X'], ['O','X','O','O'], ['X','-','-','X'], ['-','-','-','O']],'[2,0]')==False)


def fim_de_jogo():
    '''função que identifica se o jogador deseja ou não finalizar o jogo. none -> bool'''
    S_N=input()
    while S_N not in "SN" or len(S_N)!=1:
        print("Comando inválido. Deseja iniciar uma nova partida (S/N)?")
        S_N=input()
    if S_N=="N":
        return False
    if S_N=="S":
        return True
