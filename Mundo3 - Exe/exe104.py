'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = float(n)
            ok = True
        else:
            print(f'Erro Digite um Numero')
        if ok:
            break
    return valor

n = leiaInt('Digite um Numero: ')
print(f'Você Acabou de Digitar o Numero {n}')
print('FIM')