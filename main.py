from tabuleiro import tabuleiro
from checar_jogo import checar_empate, checar_vitoria
from checar_input import fim_de_jogo, jogada_valida




def main():
    '''programa principal para realização do jogo da velha'''
    
    #dados do jogo
    jogador=1
    jogo=[["-","-","-","-"] for linhas in range(4)]
    continuar_jogo=True
    print("\n  ----- Jogo da Velha -----")


    #gerador de jogadas
    while continuar_jogo==True:
        tabuleiro(jogo)
        print("Jogador {} - escolha uma posição [x,y]: ".format(jogador))
        jogada=input()


        #validador de jogadas
        while jogada_valida(jogo,jogada)==False:
            print("Posição inválida. Jogador {} - escolha uma posição [x,y]: ".format(jogador))
            jogada=input()


        #identificador de jogadas
        if jogador==1:
            jogo[int(jogada[1])][int(jogada[3])]="X"
        if jogador==2:
            jogo[int(jogada[1])][int(jogada[3])]="O"


        #verificador de vitórias
        if checar_vitoria(jogo)==True:
            tabuleiro(jogo)
            print("Jogador {} venceu o jogo. Deseja iniciar uma nova partida (S/N)?".format(jogador))
            if fim_de_jogo()==False:
                continuar_jogo=False
                jogo=[["-","-","-","-"] for linhas in range(4)]
            else:
                jogador=2
                jogo=[["-","-","-","-"] for linhas in range(4)]
                
                

        #verificador de empates
        if checar_empate(jogo)==True:
            tabuleiro(jogo)
            print("Empate. Deseja iniciar uma nova partida (S/N)?")              
            if fim_de_jogo()==False:
                continuar_jogo=False
            else:
                jogador=2
                jogo=[["-","-","-","-"] for linhas in range(4)]
                
                
        #alternador de jogadores    
        if jogador==1:
            jogador=2
        else:
            jogador=1
                
if __name__ == '__main__':
    main()
