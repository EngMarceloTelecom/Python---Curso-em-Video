
from moeda import moeda, aumentar, diminuir, dobro, metade, resumo

p = float(input('Digite o Valor [R$]: '))
t = float(input('Qual a Taxa [%]: '))

print(resumo(p, t))
