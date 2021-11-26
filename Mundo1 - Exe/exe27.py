n = str(input('Qual Seu Nome Completo? ')).strip().upper()
nome = n.split()
print('Seu Primeiro Nome é: {}'.format(nome[0]))
print('Seu Ultimo Nome é: {}'.format(nome[len(nome)-1]))
