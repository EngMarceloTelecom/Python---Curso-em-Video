frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" Aparece {}'.format(frase.count('A')))
print('A Primeiro letra "A" aparece na posição {}'.format(frase.find('A')+1))
print('A Ultima letra "A" aparece na posição {}'.format(frase.rfind('A')+1))
