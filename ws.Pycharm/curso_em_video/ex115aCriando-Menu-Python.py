from uteis.interface import *
from uteis.arquivo import *
from time import sleep

arg = 'arquivo.txt'
if not arquivoExiste(arg):
    criarArquivo(arg)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('PESSOAS CADASTRADAS')
        lerArquivo(arg)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ').title()
        idade = leiaint('Idade: ')
        cadastrar(arg, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até Logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção Válida.\033[m')
    sleep(2)
