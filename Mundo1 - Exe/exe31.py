dis = float(input('Qual a Distancia (Km): '))
print('Boa Viagem de {:.0f} km'.format(dis))
if dis <= 200:
    preço = dis * 0.5
else:
    preço = dis * 0.45
print('O preço da Sua Viagem é R$ {:.2f}'.format(preço))