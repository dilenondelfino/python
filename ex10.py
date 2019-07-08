cont = 0
maior = 0

while cont < 5:
    numero = int(input("Digite um numero: "))
    if numero > maior:
        maior = numero
    cont += 1

print('O maior numero é : {}'.format(maior))