'''
Faça um programa que: Dada uma lista [1,2,3,4,5,6,7,8,9,10] e um numero inteiro, imprima a tabuada desse numero
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input('Qual o numero da tabudada de deseja: '))

#com compreensão de lista - peguei esse exemplo do Eduardo
print([n * i for i in lista])

#for i in lista:
#   print(n * i)