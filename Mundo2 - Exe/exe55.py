maior = 0
menor = 0
for i in range(1,6):
    peso = float(input('Peso da {}º Pessoa (Kg): '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso é {} Kg'.format(maior))
print('O MENOR peso é {} Kg'.format(menor))