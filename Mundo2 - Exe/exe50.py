soma = 0
cont = 0
for i in range(1,7):
    n = int(input('Digite o {}º Numeros: '.format(i)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('Voce Informou {} PARES e a Soma é {}'.format(cont, soma))