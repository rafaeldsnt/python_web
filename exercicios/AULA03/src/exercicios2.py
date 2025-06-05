#Imprima uma contagem regressiva com um input feito pelo usuário
#utilize a função while
import time


def Countdown():
    int_start = int(input("Informe o início da Contagem regressiva... "))
    while  (int_start >= 0):
        print(f"Número ...{int_start}")
        time.sleep(1)
        int_start -= 1; 



if(__name__ == '__main__'):
    Countdown()