resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    nu = int(input('Digite um Numero: '))
    quant +=1
    soma += nu
    resp = str(input('Quer Continuar [Sim ou Não]? ')).upper().split()[0]
    
    if resp == int:
        print('Opção Invalida')
        
    if quant == 1:
        maior = menor = nu
    else:
        if nu > maior:
            maior = nu
        if nu < menor:
            menor = nu
media = soma/quant
print('Voce Digitou {}, sua Media {:.2f}'.format(quant, media))
print('O Maior Numero é {}, e o Menor Numero é {}'.format(maior,menor))