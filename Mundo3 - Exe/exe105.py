'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:'''

def notas(*n, sit=False):
    alunos = {}
    alunos['total'] = len(n)
    alunos['maior'] = max(n)
    alunos['menor'] = min(n)
    alunos['media'] = sum(n)/len(n)
    
    if sit:
        if alunos['media'] >= 7:
            alunos['situação'] = 'BOA'
        elif alunos['media'] >= 5:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'RUIM'
    return alunos

cont = 0
while True:
    cont = cont + 1
    n = float(input(f'Qual a Nota {cont}ª: '))
    rep = str(input('Quer Add Mais Notas [S/N]: '))
    if rep in 'Nn':
        break

situ = str(input('Ver a Situação do Aluno [S/N]: '))
if situ in 'sS':
    notas = notas(n,sit=True)
else:
    notas = notas(n,sit=False)

print(notas)
