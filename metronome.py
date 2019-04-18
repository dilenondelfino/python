#Tentando fazer um metronomo legal para usar para estudar musica
#Preciso melhorar os comentários no código
import time

def andameto(self):
    while True:
        try:
            self.bpm = int(input('Valor bpm(Valores de 30 a 350): '))
            if not 30 <= self.bpm <= 350:
                raise ValueError('Bpm fora do valor permitido')
        except ValueError as e:
            print('Valor invalido:', e)
            else:
                break
