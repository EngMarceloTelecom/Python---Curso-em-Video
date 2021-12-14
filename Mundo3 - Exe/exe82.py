'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
lis = []
lisimpar = []
lispar = []
while True:
    num = int(input('Digite um Numero: '))
    res = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
    lis.append(num)
    while res not in 'SN':
        res = str(input('Opção Invalidade. Quer Continuar [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
for i, v in enumerate(lis):
    if v % 2 == 0:
        lispar.append(v)
    else:
        lisimpar.append(v)

print(f'Sua lista é {lis}')
print(f'Sua lista dos Pares {lispar}')
print(f'Sua lista dos Impares {lisimpar}')


