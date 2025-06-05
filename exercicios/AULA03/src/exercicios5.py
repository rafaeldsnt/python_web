#Conte quantas vezes o usuário interagiu até digitar a opção 'sair'
#utilize a função while e crie um menu com 3 opções 
import time

def Userinteraction():

    not_end = True
    total_option1 = 0
    total_option2 = 0

    while not_end:
        print(f"=====================================================================================")
        print(f"Opção 1 ----> Carro ")
        print(f"Opção 2 ----> Moto ")
        print(f"Opção 3 ----> Sair ")
        print(f"=====================================================================================")
        int_option = int(input("Informe a sua opção "))

        match int_option:
                case 1:
                    total_option1 += 1
                case 2:
                     total_option2 += 1
                case 3:
                    not_end = False
                case _:
                     print(f"Não identificamos a sua opção!!! ")

        print(f"A opção 1 - Carro foi chamada {total_option1}")
        print(f"A opção 1 - Moto  foi chamada {total_option2}")
        
         

Userinteraction()