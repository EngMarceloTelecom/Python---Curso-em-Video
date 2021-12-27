'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:'''

import time

def escreva(texto):
    tam = len(texto)+4
    print('='*tam)
    print(f'  {texto}')
    print('='*tam)
texto = 'CONTANDO'
escreva(texto)

def contador1(i, f, p):
    print('='*20)
    for c in range(i, f, p):
        print(f'{c}',end=' ', flush=True)
        time.sleep(0.3)
    
def contador2(i, f, p):
    print('='*10)
    for c in range(i, f, p):
        print(f'{c}',end=' ', flush=True)
        time.sleep(0.3)

def contador(i, f, p):
    print('='*p)
    for c in range(i, f+1, p):
        print(f'{c}',end=' ', flush=True)
        time.sleep(0.3)

contador1(1, 11, 1)
print()
contador2(10, 0, -2)
print(f'\n==========')
i = int(input('Inicio: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))

if f < i and p > 0:
    print(f'Não é possivel fazer a Contagem entre {i} e {f} Nescessario que o Passo seja Negativo')
if f > i and p < 0:
    print(f'Não é possivel fazer a Contagem entre {i} e {f} Nescessario que o Passo seja Positivo')
if p == 0:
    p = 1
contador(i, f, p)
print('\nFIM')