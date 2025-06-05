#imprima a tabulada escolhida pelo usuário
#utilize a função range
import time

def PrintnumberTab():
    
    int_number = int(input("Informe a tabuada que você deseja ...  "))

    for numberInttab in range(0,11):
         print(f"{numberInttab}   x {int_number} = {numberInttab*int_number}")
         time.sleep(1)

         
PrintnumberTab()