salario = float(input('Qual Seu Salario? R$ '))
if salario <= 1250:
    print('Seu Salario com Almeto de 15% é {:.2f}'.format((salario*0.15 + salario)))
else:
    print('Seu Salario com Almeto de 10% é {:.2f}'.format((salario*0.1 + salario)))