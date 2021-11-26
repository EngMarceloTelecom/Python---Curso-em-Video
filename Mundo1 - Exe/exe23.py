num = int(input('Informe um Numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o Numero', num)
print('Unidade: ',u)
print('Dezena: ',d)
print('Centena: ',c)
print('Milhar: ',m)
