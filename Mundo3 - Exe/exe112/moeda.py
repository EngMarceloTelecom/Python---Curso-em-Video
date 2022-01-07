def aumentar(p = 0 , t = 0):
    res = p + (p*t/100)
    return res

def diminuir(p = 0, t = 0):
    res = p - (p*t/100)
    return res

def dobro(p = 0 ):
    res = p*2
    return res

def metade(p = 0):
    res = p/2
    return res

def moeda(p = 0 ,m = 'R$'):
    return f'\t{m} {p:.2f}'.replace('.', ',')

def resumo(p = 0, t = 0):
    print()
    print(f'Seu Aumento {moeda(p)} \t= {moeda(aumentar(p, t))}')
    print(f'Seu Redução {moeda(p)} \t= {moeda(diminuir(p, t))}')
    print(f'Seu Dobro {moeda(p)} \t= {moeda(dobro(p))}')
    print(f'Sua Metade {moeda(p)} \t= {moeda(metade(p))}')
    print()

def leiadinheiro(msg):
    valido = False
    while not valido:
        ent = str(input(msg)).replace(',','.').strip()
        if ent.isalpha() or ent == '':
            print(f'\033[0:31m<<Erro>> Preço invalido\033[m')
        else:
            valido = True
            return float(ent)
