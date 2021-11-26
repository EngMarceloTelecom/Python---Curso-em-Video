cont = soma = n = 0
n = int(input('Digite um Numero [ou 999 para Parar]: '))
while n != 999:
    soma +=n
    cont +=1
    n = int(input('Digite um Numero [ou 999 para Parar]: '))
print(f'Voce Digitou {cont} numeros, e a soma é {soma}')