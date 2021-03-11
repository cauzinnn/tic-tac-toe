def checar_vitoria(jogo):
    '''função que analisa o tabuleiro do jogo em busca de uma sequência que
        garanta a vitória. list -> bool'''

    #diagonais
    if jogo[0][0]==jogo[1][1]==jogo[2][2]==jogo[3][3]!="-":
        return True
    if jogo[0][3]==jogo[1][2]==jogo[2][1]==jogo[3][0]!="-":
        return True


    #colunas
    acumulador = ""
    for i in range(4):
        for j in range(4):
            acumulador += jogo[i][j]
        if acumulador[0]==acumulador[1]==acumulador[2]==acumulador[3]!="-":
            return True
        acumulador = ""

        
    #linhas
    for i in range(4):
        for j in range(4):
            acumulador += jogo[j][i]
        if acumulador[0]==acumulador[1]==acumulador[2]==acumulador[3]!="-":
            return True
        acumulador = ""
  

    #quadrado
    for i in range(3):
        for j in range(3):
            if jogo[i][j]==jogo[i][j+1]==jogo[i+1][j]==jogo[i+1][j+1]!="-":
                return True
    else:
        return False


def teste_checar_vitoria():
    print(checar_vitoria([['X','X','X','X'], ['O','X','O','O'], ['-','-','O','X'], ['-','-','-','O']]) == True)
    print(checar_vitoria([['O','O','O','O'], ['X','O','X','X'], ['-','X','X','O'], ['-','-','-','X']]) == True)
    print(checar_vitoria([['X','O','O','X'], ['X','X','O','O'], ['X','O','O','X'], ['O','X','X','O']]) == False)
    print(checar_vitoria([['X','O','O','X'], ['O','X','O','O'], ['X','O','X','X'], ['O','X','O','X']]) == True)


def checar_empate(jogo):
    '''função que analisa o tabuleiro do jogo para descobrir se não houve um
        vencedor e deu empate. list -> bool'''
    acumulador=""
    for x in range(4):
        for y in range(4):
            if jogo[x][y]=="-":
                acumulador+=jogo[x][y]
    return not bool(acumulador)

def teste_checar_empate():
    print(checar_empate([['X','O','X','O'], ['O','X','O','X'], ['X','O','X','O'], ['X','O','X','O']]) == True)
    print(checar_empate([['O','X','O','X'], ['X','O','X','O'], ['O','X','O','X'], ['O','X','O','X']]) == True)
    print(checar_empate([['X','O','X','O'], ['O','O','O','X'], ['X','O','X','X'], ['O','X','O','X']]) == True)
