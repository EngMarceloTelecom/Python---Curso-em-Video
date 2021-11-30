''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

import time

num = []
while True:
    valor = int(input('Digite um Numero: '))
    if valor not in num:
        num.append(valor)
        print('Valor Adicionado com Sucesso..')
    else:
        print('Valor Duplicado..')
    res = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Valor Invalido Quer Continuar [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('='*30)
num.sort()
print (f'Sua Lista é {num}')
print('FIM')