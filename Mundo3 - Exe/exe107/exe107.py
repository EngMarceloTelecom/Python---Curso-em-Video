import moeda

p = float(input('Digite o Valor [R$]: '))
t = float(input('Qual a Taxa [%]: '))

print(f'Seu Aumento R$ {p} foi de {moeda.aumentar(p, t)}')
print(f'Seu Desconto R$ {p} foi de {moeda.diminuir(p, t)}')
print(f'Seu Dobro R$ {p} foi de {moeda.dobro(p)}')
print(f'Sua Metade R$ {p} foi de {moeda.metade(p)}')