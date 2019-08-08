from random import choice # pip install random
from time import sleep

possibilidades = ["0,0","0,1","0,2","1,0","1,1","1,2","2,0","2,1","2,2"]
tabuleiro = [["_","_","_"],["_","_","_"],["_","_","_"]]


def remove_possibilidades(numero):    
    try:
        index = possibilidades.index(numero)
        possibilidades.pop(index)
    except:
        pass

def fim_de_jogo():
    exit()


def verifica_possibilidades(n):
    if possibilidades == []:
        fim_de_jogo()
    else:
        if n in possibilidades:
            remove_possibilidades(n)
            return True
        else:
            return False


def verifica_ganhador():
    ganhar = [
    [tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]],
    [tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]],
    [tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]],
    [tabuleiro[0][0],tabuleiro[1][1],tabuleiro[2][2]],
    [tabuleiro[0][2],tabuleiro[1][1],tabuleiro[2][0]],
    [tabuleiro[0][0],tabuleiro[1][0],tabuleiro[2][0]],
    [tabuleiro[0][1],tabuleiro[1][1],tabuleiro[2][1]],
    [tabuleiro[0][2],tabuleiro[1][2],tabuleiro[2][2]],
    ]

    if ["X","X","X"] in ganhar:
        print("\033[042m Player 1 WIN!!!!\033[0m")
        exibe()
        fim_de_jogo()
    if ["O","O","O"] in ganhar:
        print("\033[041m YOU LOSE!!!!\033[0m")
        exibe()
        fim_de_jogo()


def jogar():
    n = str(input("Digite um valor: "))
    if verifica_possibilidades(n) == True:
        jogador = 1
        jogo(n,jogador)
    else:
        jogar()




def jogar2():
    try:
        n = choice(possibilidades)
    except:
        print("\033[046m DEU VELHA!!!\033[0m")
        fim_de_jogo()
    if verifica_possibilidades(n) == True:
        jogador = 2
        jogo(n,jogador)
    else:
        jogar2()

def jogo(n,jogador):
    n = n.split(",")
    n[0] = int(n[0])
    n[1] = int(n[1])
    if jogador == 1:
        tabuleiro[n[0]][n[1]] = "X"
    elif jogador == 2:
        tabuleiro[n[0]][n[1]] = "O"
    verifica_ganhador()
    exibe()



def exibe():
    print(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2])
    print(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2])
    print(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2])
    print(10*"-")


print("Para jogar digite uma das possibilidades apresentadas")
while len(possibilidades) > 0:
    print("As possiblidades são: {}\n".format(possibilidades))    
    jogar()
    jogar2()
    #print("\nA quantidade de possibilidades possiveis: [{}]".format(len(possibilidades)))
