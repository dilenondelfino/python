'''
Faça um programa que receba uma data de nascimento (01/01/1900) e imprima
'Voce naseu em 01 de 01 de 1900'
'''
nascimento = input("Qual é a sua data de nascimento:\n Modelo '01/01/1990'\n")

# o split faz com o string vire uma lista
dia, mes, ano = nascimento.split('/')

print("Voce nasceu em {} de {} de {}".format(dia, mes, ano))
