
from moeda import moeda, aumentar, diminuir, dobro, metade, resumo, leiadinheiro

p = leiadinheiro('Digite o Valor [R$]: ')
t = float(input('Qual a Taxa [%]: '))

print(resumo(p, t))
