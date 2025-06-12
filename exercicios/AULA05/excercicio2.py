import os

def ceateFile(nameFile:str):
    with open(nameFile, "w") as fileOpen:
        fileOpen.write("0")

def inserlineFile(nameFile:str, conteudo:str):
    with open(nameFile, "a") as  fileOpen:
        fileOpen.write('\n'+conteudo)

def readAndCountlines(nameFile:str) -> int:
    sumInt = 0
    if (os.path.exists(nameFile)):
          with open(nameFile, "r") as fileOpen:
            lines = fileOpen.readlines()
            print(lines)
            for number in lines:
                if (number != None):
                    print(number)
                    sumInt = sumInt + int(number)   

    return sumInt


if(__name__ == '__main__'):
    nameFile = (input("Informe o nome do Arquivo "))
    ceateFile(f'{nameFile}.txt')
    i = 0
    while i < 3:
        contentFile = (input("Informe o conteúdo do Arquivo "))
        inserlineFile(f'{nameFile}.txt' , contentFile)
        i = i + 1
    
    print(readAndCountlines(f'{nameFile}.txt'))



    #nameFile = (input("Informe o nome do Arquivo que será removido "))
    #removeFile(f'{nameFile}.txt')