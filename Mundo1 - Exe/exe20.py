import random
a1 = input('Primeiro Nome: ')
a2 = input('Segundo Nome: ')
a3 = input('Terceiro Nome: ')
a4 = input('Quarto Nome: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('Aluno Ordem de Apresentação é\n{}'.format(lista))
