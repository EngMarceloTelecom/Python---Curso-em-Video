def leiaInt(msg):
    while True:
        try:
            n = int(input('Qual Sua opção: '))
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

def linha():
    return '='*40

def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def menu(lista):
    cabeçalho('Menu Principal')
    cont = 1
    for i in lista:
        print(f'{cont} - {i}') 
        cont += 1
    opç = leiaInt('Qual Sua opção: ')
    return opç



