
def leiaInt(msg):
    while True:
        try:
            n = int(input('Digite um Numero: '))
        except (ValueError, TypeError):
            print('\033[31mErro>>> Por Favor Digite um Numero Inteiro Valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('Usuário Preferio não Digitar')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input('Digite um Numero: '))
        except (ValueError, TypeError):
            print('\033[31mErro>>> Por Favor Digite um Numero Real Valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('Usuário Preferio não Digitar')
            return 0
        else:
            return n



ni = leiaInt('Digite um Numero Inteiro: ')
nf = leiaFloat('Digite um Numero Real: ')
print(f'Você Acabou de Digitar o Numero inteiro {ni} e o rela foi {nf}')
print('FIM')