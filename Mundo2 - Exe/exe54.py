import datetime
atual = datetime.date.today().year
totmaior = 0
totnemor = 0
for i in range(1, 8):
    qa = int(input('Nascimento {}º: '.format(i)))
    mi = atual - qa
    if mi >= 18:
        totmaior += 1
    else:
        totnemor += 1
print('A {} Pessoa MAIOR de IDADE'.format(totmaior))
print('A {} Pessoa MENOR de IDADE'.format(totnemor))