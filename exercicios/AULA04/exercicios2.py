#Definir um set com 3 elementos 
#acessar  por indice 
#adicionar 
#adicionar duplicado
#remover por valor


MySET = {"Petrópolis", "Vila Velha", "Blumenau"}


def AcessMYSET():
    for x in MySET:
        print(f"Acessando um set  ...{x}")
    
def AddItemMYSET():
    MySET.add("Bento Gonçalves")
    print(f"Item add  ... Bento Gonçalves")

def AddItemListIndex():
    MySET.add("Bento Gonçalves")
    print(f"__________")

def RemoveValue():
    MySET.remove("Bento Gonçalves")



if(__name__ == '__main__'):
    AcessMYSET()
    AddItemMYSET()
    AddItemListIndex()
    print(f"Print SET ...")
    AcessMYSET()
    AddItemListIndex()
    print(f"Print SET ...")
    AcessMYSET()
    RemoveValue()
    print(f"Print Final  ..")
    AcessMYSET()