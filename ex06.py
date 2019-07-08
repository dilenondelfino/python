n1 = float(input("Nota um: "))
n2 = float(input("Nota dois: "))

media = float((n1 + n2) / 2)

if media >= 6 and media <=9 :
    print("Aprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("reprovado")
    