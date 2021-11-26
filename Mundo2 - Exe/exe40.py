n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda NOta: '))
m1 = (n1 + n2)/2

print('Suas Notas {:.1f} e {:.1f}, sua Media é {:.1f} '.format(n1 , n2 , m1))

if m1 < 5:
    print('Tente Novamente Voce esta, REPROVADO')
elif 5 <= m1 < 6.9:
    print('Voce Esta em RECUPEÇÃO')
elif m1 >= 7:
    print('Parabens Voce foi APROVADO')