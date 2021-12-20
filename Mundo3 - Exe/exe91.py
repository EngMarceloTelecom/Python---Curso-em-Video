'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

import random
import time
import operator

jogos = {'jogador1':random.randint(1,6),'jogador2':random.randint(1,6),'jogador3':random.randint(1,6),'jogador4':random.randint(1,6)}
ranking = []
for k, v in jogos.items():
    time.sleep(1)
    print(f'{k} seu dado deu {v}')

ranking = sorted(jogos.items(), key=operator.itemgetter(1), reverse=True)
print('='*30)

for i, v in enumerate(ranking):
    print(f'{i+1}ª Lugar {v[0]} com {v[1]}')
    time.sleep(1)
print('FIM')