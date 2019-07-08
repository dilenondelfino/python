#exe2

tamanho = input("Qual é a area a ser pintada em metros quadrados?")
cobertura = int(tamanho) * 3
custo_lata = 18
valor = 80

total_tinta = cobertura / custo_lata
total_valor = total_tinta * valor

print("A quantidade de latas de tintas é de {}, dando o valor total de {}".format(total_tinta, total_valor))
