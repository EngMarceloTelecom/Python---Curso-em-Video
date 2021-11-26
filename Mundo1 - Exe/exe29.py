vel = float(input('Qual Velocidade do Carro (Km/h)? '))
if vel > 80:
    print('Você Foi Multado R$ {:.2f}'.format(7*(vel-80)))
print(vel,'km/h Velocidade Permitida')