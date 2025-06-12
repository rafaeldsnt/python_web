import os

def ceateFile(nameFile:str):
    with open(nameFile, "w") as fileOpen:
        fileOpen.write("0")

def inserlineFile(nameFile:str, conteudo:str):
    with open(nameFile, "a") as  fileOpen:
        fileOpen.write('\n'+conteudo)


def readFile(nameFile:str) -> str:
    i = 0
    with open(nameFile) as f:
        for x in f:
            print(f"linha {i} : "+x)
            i = i + 1

def readAndsearchword(nameFile:str, searchword:str) -> bool:
    foundword = False
    if (os.path.exists(nameFile)):
          with open(nameFile, "r") as fileOpen:
            filewords = fileOpen.readlines() 
            if(searchword == filewords):
                print("--->")
            
    return foundword 


if(__name__ == '__main__'):
    nameFile = (input("Informe o nome do Arquivo "))
    ceateFile(f'{nameFile}.txt')
    i = 0
    while i < 5:
        contentFile = (input("Informe o conteúdo do Arquivo "))
        inserlineFile(f'{nameFile}.txt' , contentFile)
        i = i + 1
    
    print(readFile(f'{nameFile+".txt" }'))

    (input("Informe a linha que deseja alterar ....  "))
    lineFile = int(input("Informe o nome do Arquivo "))
    newContent = int(input("Informe o novo conteudo do Arquivo "))









    #nameFile = (input("Informe o nome do Arquivo que será removido "))
    #removeFile(f'{nameFile}.txt')