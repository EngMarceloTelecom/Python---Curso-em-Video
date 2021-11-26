import random

n = (random.randint(0,10), random.randint(0,10), random.randint(0,10),
random.randint(0,10),random.randint(0,10))

print(f'Os Valores Sotiados São {n}')

for i in n:
    print(f'{i} ', end='')

print(f'\nO Maior Valor {max(n)}')
print(f'O Menor Valor {min(n)}')