import moeda

p = float(input('Digite o Valor [R$]: '))
t = float(input('Qual a Taxa [%]: '))

print(f'Seu Aumento {moeda.moeda(p)} foi de {moeda.moeda(moeda.aumentar(p, t))}')
print(f'Seu Desconto {moeda.moeda(p)} foi de {moeda.moeda(moeda.diminuir(p, t))}')
print(f'Seu Dobro {moeda.moeda(p)} foi de {moeda.moeda(moeda.dobro(p))}')
print(f'Sua Metade {moeda.moeda(p)} foi de {moeda.moeda(moeda.metade(p))}')