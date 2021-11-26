import random
import time
comp = random.randint(0, 5)
print('Vou Pensar em um Numero entre 0 e 5, Tente Adivinhar')
jogador = int(input('Em que Numero Estou Pensando? '))
print('PROCESSANDO....')
time.sleep(2)
if jogador == comp:
    print('Parabens o Numero Que Pensei Foi {}'.format(comp))
else:
    print('Que Pena Vc erro, O Numero Que eu Pensei Foi {}'.format(comp))