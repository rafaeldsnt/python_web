#Definir uma tupla com 3 elementos 
#Adicionar uma chave com elemente
#alterar um valor numa chave especifica
#remover por valor (chave / valor)


MYDIC = {
  "Marca": "Ford",
  "Modelo": "Fiesta",
  "Ano": 2021
}


def ADDITEMNYDIC():
    MYDIC["color"] = "vermelho"
    
    
def UpdateValueforIndex():
    MYDIC.update({"Item" : "7856210-96","Ano": 2000, "Modelo" : "Fiesta 2k"})

def RemoveItemMYDIC():
    MYDIC.pop("color")



if(__name__ == '__main__'):
    print(f"Imprimindo... -> {MYDIC}")
    ADDITEMNYDIC()
    print(f"Imprimindo... -> {MYDIC}")
    UpdateValueforIndex()
    print(f"Imprimindo... -> {MYDIC}")
    RemoveItemMYDIC()
    print(f"Imprimindo... -> {MYDIC}")
    