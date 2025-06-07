#Armazene 5 frutas nas estruturas (lista/Set/Tuple/DIC)
#definir uma lista vazia
#criar um estrutura de repetição para inseris os 5 elementos 
#criar uma variável para cada esturtura e fazer a devida conversão
#imprirmir os 5 resultados
#2 - após o teste acima, aplique o random para nserir o valor na lista

my_fruitsList = []
my_fruitsSet = {}
my_fruitTuple = ()
my_fruitsDIC = {}


def AddItemList(my_fruitsList):
    for x in range(0,5):
        name_fruit = input(f"Informe o nome da {x+1} fruta ...")
        my_fruitsList.append(name_fruit)


def PrintItensList(my_fruitsList):
    for x in my_fruitsList:
         print(f"Fruta Cadastrada: Indice ->  {my_fruitsList.index(x)} ... {x}")


def ConvertListinSetTUPLE(my_fruitsList,my_fruitsSet, my_fruitTuple,my_fruitsDIC):
    my_fruitsSet = set(my_fruitsList)
    my_fruitTuple = tuple(my_fruitsList)
    
    for t in my_fruitsList:
        my_fruitsDIC["frutas"] = t

def PrintItensSet(my_fruitsSet):
    for x in my_fruitsList:
         print(f"Fruta Cadastrada: SET   ... {x}")




def PrintTUPLE(my_fruitTuple):
    print(f"Fruta Cadastrada: TUPLE   ... {len(my_fruitTuple)}")

    for t in my_fruitTuple:
         print(f"Fruta Cadastrada: SET   ... {t}")


def PrintDIC(my_fruitsDIC):
    for d in my_fruitsDIC:
         print(f"Fruta Cadastrada: SET   ... {d}")




if(__name__ == '__main__'):
    print(f"=====================================================================================")
    print(f"=====================================================================================")
    print(f"------------> Operação com Lista")
    print(f"--> Cadastro Lista")
    AddItemList(my_fruitsList)
    print(f"--> Impressão de  Lista")
    PrintItensList(my_fruitsList)
    print(f"=====================================================================================") 
    print(f"=====================================================================================")

    print(f"=====================================================================================")
    print(f"=====================================================================================")
    print(f"------------> Conversão")
    ConvertListinSetTUPLE(my_fruitsList,my_fruitsSet, my_fruitTuple,my_fruitsDIC)
    print(f"=====================================================================================") 
    print(f"=====================================================================================")

    print(f"=====================================================================================")
    print(f"=====================================================================================")
    print(f"------------> Operação com SET")
    print(f"--> Impressão de SET")
    PrintItensSet(my_fruitsSet)
    print(f"=====================================================================================") 
    print(f"=====================================================================================")

    print(f"=====================================================================================")
    print(f"=====================================================================================")
    print(f"------------> Operação com TUPLE")
    print(f"--> Impressão de TUPLE")
    PrintTUPLE(my_fruitTuple)
    print(f"=====================================================================================") 
    print(f"=====================================================================================")


    print(f"=====================================================================================")
    print(f"=====================================================================================")
    print(f"------------> Operação com DIC")
    print(f"--> Impressão de DIC")
    PrintDIC(PrintDIC)
    print(f"=====================================================================================") 
    print(f"=====================================================================================")