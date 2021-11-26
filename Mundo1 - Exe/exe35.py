L1 = float(input('Primeiro Lado: '))
L2 = float(input('Segundo Lado: '))
L3 = float(input('Terceiro Lado: '))
if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Os Seguimentos Podem Formar um Triangulo OK')
else:
    print('Os Seguimentos Não Podem Formar um Triangulo Tente Novamente')
