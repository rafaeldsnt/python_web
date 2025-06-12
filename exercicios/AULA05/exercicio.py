import os

def ceateFile(nameFile:str, conteudo:str):
    with open(nameFile, "w") as fileOpen:
        fileOpen.write(conteudo)


def inserlineFile(nameFile:str, conteudo:str):
    with open(nameFile, "a") as  fileOpen:
        fileOpen.write('\n' + conteudo)



def readFile(nameFile:str) -> str:
    with open(nameFile, "r") as fileOpen:
        return fileOpen.read()


def readAndCountlines(nameFile:str) -> str:
    if (os.path.exists(nameFile)):
          with open(nameFile, "r") as fileOpen:
            return len(fileOpen.readlines())


def readAndsearchword(nameFile:str, searchword:str) -> bool:
    foundword = False
    if (os.path.exists(nameFile)):
          with open(nameFile, "r") as fileOpen:
            filewords = fileOpen.readlines() 
            if(searchword in filewords):
                foundword = True
            else:
                print("Não encontrei...")
            
    return foundword 
    

def removeFile(nameFile:str):
    if (os.path.exists(nameFile)):
        os.remove(nameFile)
        print(f"Arquivo encontrado e apagado!!!")
    else:
        print(f"Arquivo não encontrado!!!")


if(__name__ == '__main__'):
    #nameFile = (input("Informe o nome do Arquivo "))
    #contentFile = (input("Informe o conteúdo do Arquivo "))
    #ceateFile(f'{nameFile}.txt' , contentFile)

    #namereadFile = (input("Informe o nome do Arquivo "))
    #print(readFile(f'{namereadFile+".txt" }'))


    #nameFile = (input("Informe o nome do Arquivo "))
    #contentFile = (input("Informe o conteúdo do Arquivo "))
    #inserlineFile(f'{nameFile}.txt' , contentFile)
    #print(readFile(f'{nameFile+".txt" }'))

    #nameFile = (input("Informe o nome do Arquivo "))
    #print(readAndCountlines(f'{nameFile+".txt" }'))

    nameFile = (input("Informe o nome do Arquivo "))
    wordseach = (input("Informe a palavra do Arquivo "))

    print(readAndsearchword(f'{nameFile}.txt' , wordseach))



    #nameFile = (input("Informe o nome do Arquivo que será removido "))
    #removeFile(f'{nameFile}.txt')