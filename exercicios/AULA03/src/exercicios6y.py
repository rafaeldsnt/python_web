#Conte quantas vezes o usuário interagiu até digitar a opção 'sair'
#utilize a função while e crie um menu com 3 opções 
import time

def Word_palindrome(word_one):
    ispalindrome = False
    
    word_one.upper()
    
    word_second = word_one[::-1]

    if (word_second == word_one):
        ispalindrome = True
    
    return ispalindrome

def Valid_palindrome():
    word_one = (input("Informe a primeira palavra : "))

    response =  "é" if(Word_palindrome(word_one)) else "não é"

    print(f"A palavra '{word_one}' {response} palindromo")

Valid_palindrome()