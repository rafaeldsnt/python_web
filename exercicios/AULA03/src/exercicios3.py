#Some os valores do intervalo definido pelo usuário
#utilize a função range


def Sumnumbers():
     
     total_soma = []

     int_start = int(input("Informe o início da Soma "))

     int_end = int(input("Informe o fim da Soma  "))

     print(f"Total somatório é ...{sum(range(int_start,int_end))}")

if(__name__ == '__main__'):
    Sumnumbers()