#Imprimir os numeros a partir de um input do usuário
#até um limite definido, também pelo próprio usuário
#utilize funcao definido parametros


def WriteNumbers(int_start, int_end):
    for numbertowrite in range(int_start, int_end):
        print(f"Número ...{numbertowrite}")
        numbertowrite = numbertowrite + 1; 



def RangeofNumbers():
       int_start = int(input("Informe o início da Contagem "))

       int_end = int(input("Informe o fim da Contagem "))

       WriteNumbers(int_start,(int_end + 1))





if(__name__ == '__main__'):
    RangeofNumbers()