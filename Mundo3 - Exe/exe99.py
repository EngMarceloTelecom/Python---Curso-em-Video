'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep
def maior(*num):
    lista = []
    for valor in num:
        print(f'{valor}',end=' ',flush=True)
        sleep(0.3)
    if not num:
        print('Sem Valor Informado')
    else:
        lista.append(valor)
        print(f'\nO Maior Valor Informado é {max(lista)}')

maior(3,5,9,6,9)
print('='*30)
maior(10,2,8,6,20)
print('='*30)
maior()
print('='*30)
print('FIM')
