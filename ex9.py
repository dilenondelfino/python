'''
PT: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido

EN: Make a program that asks for a note, between zero and ten. Show a message if the value
invalid and continue asking until the user enters a valid value
'''

value = int(input("Enter a value: \nBetween 1 to 10 \n "))

while value <= 1 or value >= 10:
    value = int(input("Enter a value:\n Between 1 to 10\n "))
        
print(value)