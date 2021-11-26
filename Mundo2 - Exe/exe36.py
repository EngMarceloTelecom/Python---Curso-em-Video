casa = float(input('Qual Valor da Casa R$ '))
sala = float(input('Qual Salario R$ '))
ano = int(input('Quantos Anos? '))
pres = casa / (ano * 12)

if pres <= 0.3 * sala:
    print('Emprestimo Cosedido, Sua Prestação Mensal é R$ {:.2f}'.format(pres))
else:
    print('Emprestimo Negado, Sua Prestação é R$ {:.2f}, 30% acima do seu Salario'.format(pres))
