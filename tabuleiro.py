def tabuleiro(jogo):
    '''função que formula/printa a estrutura do tabuleiro do jogo. list -> none'''
    for l in range(len(jogo)):
        print("\n\t {}  {}  {}  {}".format(jogo[l][0],jogo[l][1],jogo[l][2],jogo[l][3]))
    print("")
