#Definir uma tupla com 3 elementos 
#acessar  por indice 
#alterar um valor pelo indice
#adicionar pelo valor 
#remover por valor


MyTUPLE = ("apple", "banana", "cherry")


def AcessMyTUPLEINDEX():
    print(f"Acess tuple index :: {MyTUPLE[0]}")
    
def UpdateValueforIndex():
    newList = list(MyTUPLE)
    newList[1] = "Kiwi"
    MyTUPLE2 = tuple(newList)

    for x in MyTUPLE2:
        print(f" Nova Tupla {x}")

def AddItemValue():
    newList2 = list(MyTUPLE)
    newList2.append("goiaba")
    MyTUPLE3 = tuple(newList2)

    for y in MyTUPLE3:
        print(f" Nova Tupla {y}")





if(__name__ == '__main__'):
    AcessMyTUPLEINDEX()
    UpdateValueforIndex()
    AddItemValue()
    #print(f"Print SET ...")
    #AcessMYSET()
    #AddItemListIndex()
    #print(f"Print SET ...")
    #AcessMYSET()
    #RemoveValue()
    #print(f"Print Final  ..")
    #AcessMYSET()