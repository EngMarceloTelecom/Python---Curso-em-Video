pala = ('Python', 'Programa', 'Estudar', 'Mercado','Telecom', 'Marcelo')

for i in pala:
    print(f'\nNessa Palavra {i} Temos ', end='')
    for l in i:
        if l.lower() in 'aeiou':
            print(f'{l}', end=' ')