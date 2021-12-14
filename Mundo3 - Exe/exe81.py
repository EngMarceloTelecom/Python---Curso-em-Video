'''Crie um programa que vai ler vários números e colocar em uma lista.A) Quantos números foram digitados.                                                  B) A lista de valores, ordenada de forma decrescente.                                                C) Se o valor 5 foi digitado e está ou não na lista.'''
lis = []

while True:
    num = int(input('Digite um Numero: '))
    res = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
    lis.append(num)
    
    while res not in 'SN':
        res = str(input('Opção Invalide, Quer Continuar [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break

if 5 in lis:
    print('Existe o Numero 5 na Sua Lista')
else:
    print('Não Existe o Numero 5 na Sua Lista')

lis.sort(reverse=True)
print(lis)
print(f'A sua Lista tem {len(lis)} elementos')