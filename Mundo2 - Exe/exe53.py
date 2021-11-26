frase = str(input('Digite uma Frase: ')).strip().upper()
sepa = frase.split()
junto = ''.join(sepa)
inver = ''
for i in range(len(junto)-1, -1, -1):
    inver += junto[i]
print('{} , {}'.format(junto, inver), end=' ')
if inver == junto:
    print('\nEsta Frase é um PALINDROMO')
else:
    print('\nEsta Frase NÃO é um PALINDROMO')
