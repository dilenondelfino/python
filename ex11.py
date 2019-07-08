'''
Faça um programa que itere em uma string e toda vez que uma vogal aparecer na sua string print o seu nome entre as letras

string = bananas

b
delfino
n
delfino
n
...
'''

my_string = str(input('Digite uma palavra: \n'))
nome = str(input('Digite o seu nome: \n'))

#obs: sempre criar uma variavel de verificação para o for
for letra in my_string:
    if letra in 'aeiou':
        print(nome)
    else:
        print(letra)