cont = soma = 0
while True:
    n = int(input('Digite um Numero [ou 999 para Parar]: '))
    if n == 999:
        break
    soma +=n
    cont +=1
print(f'Voce Digitou {cont} numeros, e a soma é {soma}')