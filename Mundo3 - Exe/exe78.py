'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o 
maior e o menor valor digitado e as 
suas respectivas posições na lista.'''

num = []
for i in range(0,5):
    num.append(int(input(f'Digite o {i}ª Numero: ')))

print("="*30)
print(f'A Minha Lista é {num}')
print("="*30)
print(f'O Maior Numero Digitado foi {max(num)} nas posições ',end='')

for c, v in enumerate(num):
    if v == max(num):
        print(f'{c}...',end='')

print(f'\nO Menor Numero Digitado foi {min(num)} nas posições ',end='')
for c, v in enumerate(num):    
    if v == min(num):
        print(f'{c}...',end='')

