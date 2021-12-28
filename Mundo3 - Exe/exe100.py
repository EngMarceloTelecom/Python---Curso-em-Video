'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

import random
from time import sleep

numero = []
def sorteio(lista):
    for i in range(0,5):
        sn = random.randint(1,10)
        lista.append(sn)
        print(f'{sn}',end=' ', flush=True)
        sleep(0.3)

def sorteiopar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nA soma dos Valores Pares da lista {lista} = {soma}')

sorteio(numero)
sorteiopar(numero)
