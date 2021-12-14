'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
lista = [[], []]
for i in range(1,8):
    num = int(input(f'Digite o {i}ª Numero: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'A lista Completa {lista}')
print(f'A lista de Pares {lista[0]}')
print(f'A lista de Impares {lista[1]}')

