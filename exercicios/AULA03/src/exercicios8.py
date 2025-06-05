#Crie uma função para imprimir um quadrado de asteristicos

import numpy as np
    

def Square():
    int_start = int(input("Qual é o tamanho do Quadrado (ex.: 4x4)  "))

    for _ in range(int_start):
        print('*' * int_start)


def Squareholemiddle():
    int_start = int(input("Qual é o tamanho do Quadrado (ex.: 4x4)  "))
    meio = int_start // 2
    for i in range(int_start):
        linha = '' 
        for j in range(int_start):
            if i == meio and j == meio: 
                linha += '   '
            else:
                linha += ' * ' 
        print(linha)

def pyramid():
    int_start = int(input("Qual é o tamanho da base da piramede  "))
    altura = int_start // 2 
    for i in range(altura + 1):
        espaco = ' ' * (altura -i)
        asteristicos = '*' * (2*i+1)
        print(espaco + asteristicos + espaco) 


if(__name__ == '__main__'):
    #Square()
    #Squareholemiddle()
    pyramid()