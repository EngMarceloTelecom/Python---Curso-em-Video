from interface import *
from arquivo import *
import time

cabeçalho('SISTEM << MARCELO >>')

arq = 'curso.txt'
if arqExiste(arq):
    cabeçalho('Arquivo Encontrado Com Sucesso')
else:
    cabeçalho('Aquivo Não encontrado')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastrada', 'Cadastrar Nova Pessoa', 'Deletar Cadastro' ,'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('DELETANDO CADASTRO')
    elif resposta == 4:
        cabeçalho('<<Saindo do Sistema>>> Até Logo')
        break
    else:
        cabeçalho('\033[31m<<Erro>>..Digite uma Opção Valida\033[m')
    time.sleep(1)
