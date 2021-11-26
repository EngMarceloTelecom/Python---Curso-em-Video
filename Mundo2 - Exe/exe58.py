'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''
import random
import time

comp = random.randint(0, 10)
print('Vou Pensar em um Numero entre 0 e 10, Tente Adivinhar')
acertou = False
palpit  = 0
while not acertou:
    jogador = int(input('Em que Numero Estou Pensando? '))
    palpit +=1
    print('PENSANDO....')
    time.sleep(2)
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp: 
            print('Mais...')
        else:
            print('Menos...')

print('Parabens o Numero Que Pensei Foi {}\ne Voce tentou {}x'.format(comp,palpit))

