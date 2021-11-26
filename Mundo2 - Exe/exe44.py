preço = float(input('Qual Valor do Produto R$ '))
print('''Condições de Pagamento:
[1] Avista Dinheiro/Cheque: 10% de desconto
[2] Avista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros''')

opção = int(input('Qual a Opção de Pagamento: '))
if opção == 1:
    print('O Valor a Ser Pago é R$ {:.2f}'.format(preço - (preço * 0.1)))
elif opção == 2:
    print('O Valor a Ser Pago é R$ {:.2f}'.format(preço - (preço * 0.05)))
elif opção == 3:
    print('Não a Desconto nesse valor de R$ {:.2f}'.format(preço))
    print('O Valor das 2 Parcelas são R$ {:.2f} sem JUROS'.format((preço / 2)))
elif opção == 4:
    qp = int(input('Quantidade de Parcelas: '))
    print('O Valor das {} Parcelas são R$ {:.2f}'.format(qp , (preço + (preço * 0.2))/qp))
    print('O Valor Total a Ser Pago é R$ {:.2f} com JUROS'.format(preço + (preço * 0.2)))
else:
    print('Opção Invalidade Tente Novamente uma Opção Valida')