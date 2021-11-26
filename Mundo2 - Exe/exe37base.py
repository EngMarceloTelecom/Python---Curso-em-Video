num = int(input('Escreva um Numero Decimal: '))
print('Escolha uma das bases para converção:\n[1] - Binario\n[2] - Octal\n[3] - Hexadecimal')
op = int(input('Sua Opção: '))
if op == 1:
    print('{} Convertido para Binario é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} Convertido para Octal é {}'.format(num,oct(num)[2:]))
elif op == 3:
    print('{} Convertido para Hexadecimal é {}'.format(num,hex(num)[2:]))
else:
    print('Opção Invalido, Tente Novamente')
