'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 0 <= idade <=17:
        return f'Sua idade é {idade} Voto NÃO Obrigatório'
    elif 65 >= idade >= 18:
        return f'Sua idade é {idade} Voto Obrigatório'
    elif idade > 65:
        return f'Sua idade é {idade} Voto Opcional'

ano = int(input('Em Que Ano Voce Nasceu: '))
print(voto(ano))
