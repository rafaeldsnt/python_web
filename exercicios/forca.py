import random

def hangmangame():

    listAleatorywords = ["uva", "tangerina", "abobrinha", "kiwi", "peixe", "espinafres", "batatas", "damasco", "cevada", "óleo"]
    wordsalreadytried = []
    wordselect = random.choice(listAleatorywords)
    
    endgame = False
    point = 0
    playattempt = 5
    
    print(f"A palavra secreta é  .... {wordselect}  ")

    while endgame==False:
        
        print(f"=====================================================================================")
        print(f"Sua pontuação --> {point}")
        print(f"Tentativas de Jogadas --> {playattempt}")
        print(f"=====================================================================================")
        letter = (input("Informe uma letra qualquer ? "))
        
        if (letter not in wordsalreadytried):
            if (letter in wordselect):
                print(f"=====================================================================================")
                print(f"Você acertou uma letra")
                print(f"=====================================================================================")
                point = point + 1
                wordsalreadytried.append(letter)
                playattempt = playattempt -1
            else:
                playattempt = playattempt -1
                wordsalreadytried.append(letter)
                print(f"=====================================================================================")
                print(f"Você Errou!!! ")
                print(f"=====================================================================================")
        else:
            print(f"=====================================================================================")
            print(f"Você já tentou essa letra, tente outra")
            print(f"=====================================================================================")


        if (playattempt == 0):
            endgame = True
            print(f"=====================================================================================")
            print(f"Fim de Jogo!!!  ")
            print(f"A palavra secreta é  .... {wordselect}  ")
            print(f"Suas tentativas foram .... {wordsalreadytried}  ")
            print(f"Sua pontuação foi.. {point}  ")
            print(f"=====================================================================================")
        

hangmangame()