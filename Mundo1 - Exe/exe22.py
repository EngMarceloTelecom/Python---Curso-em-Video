nc = input('Nome Completo: ')
print('Seu nome em Maiuscula: ',nc.upper())
print('Seu nome em Minuscula: ',nc.lower())
print('Total de Letras do Seu nome é: ',len(nc) - nc.count(' '))
print('Quantidade de Letras do seu Primeiro Nome é: ',len(nc.split()[0]))
