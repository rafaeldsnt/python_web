#Definir uma lista com 3 elementos 
#acessar  por indice 
#alterar por indice 
#adicionar 
#adicionar por indice
#remover por valor
#remover por indice


listAny=["RJ","SC","MG"]


def AcessIndex():
    print(f"Acessando por indice ...{listAny[0]}")
    
def UpdateIndex():
    listAny[0] = "AM"
    print(f"UpdateIndex AM ...{listAny[0]}")

def AddItemList():
    listAny.append("MT")
    print(f"AddItemList MT ...{listAny[0]}")

def AddItemListIndex():
    listAny.insert(0,"ES")
    print(f"AddItemListIndex ES ...{listAny[0]}")

def RemoveValue():
    listAny.remove("AM")
    print(f"RemoveValue AM ...{listAny[0]}")

def RemoveItemIndex():
    listAny.pop()
    print(f"RemoveItemIndex 3 ...{listAny[0]}")

if(__name__ == '__main__'):
    print(f"Print  ...{listAny}")
    AcessIndex()
    UpdateIndex()
    AddItemList()
    AddItemListIndex()
    RemoveValue()
    RemoveItemIndex()
    print(f"Print Final  ...{listAny}")
