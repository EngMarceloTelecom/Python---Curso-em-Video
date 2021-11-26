altura = float(input('Sua Altura (m) '))
peso = float(input('Seu Peso (Kg) '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Voce esta Abaixo do Peso')
elif imc <= 25:
    print('Voce esta no Peso Ideal')
elif imc <= 30:
    print('Voce esta com Sobrepeso')
elif imc <= 40:
    print('Voce esta Obeso')
else:
    print('Voce esta com Obesidade Mórbida')
