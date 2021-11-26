L1 = float(input('Primeiro Lado: '))
L2 = float(input('Segundo Lado: '))
L3 = float(input('Terceiro Lado: '))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Os Seguimentos Podem Formar um Triangulo OK')
    if L1 == L2 == L3:
        print('O Triangulo é EQUILÁTERO')
    elif L1 == L2 or L1 == L3 or L3 == L2:
        print('O Triangulo é ISÓSCELES')
    elif L1 != L2 !=L3 != L1:
        print('O Triangulo é  ESCALENO')
else:
    print('Os Seguimentos Não Podem Formar um Triangulo Tente Novamente')
