'''
# Python Object-Oriented Programming (POO) => Programação Orientada a Objeto

# Classes
    # Utilizados para criar obhetos (Instances)
    # Objetos sao partes dentro de uma  Class (Instancias)
    # Classes sçao utilizadas para agrupar Dados e Funções,
    podendo reutilizar.
    ======
    # Class: Frutas
    # Objects: Maça, Abacaxi...

# Anotações
    Primeira letra da classe sempre Maiuscula
    *Pass igual classe vazia
    *self representa o objeto antes do parametro
'''

# Criar a Classe
from datetime import date


class Funcionario:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade(self):
        ano_atual = date.today().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


# Criar o objeto
usuario1 = Funcionario('Gustavo', 'Roberto', 2004)
usuario2 = Funcionario('Laura', 'Silva', 2001)

# Criar os parametros
# usuario1.nome = 'Gustavo'
# usuario1.sobrenome = 'Roberto'
# usuario1.data_nascimento = '20/06/2004'

# usuario2.nome = 'Laura'
# usuario2.sobrenome = 'Silva'
# usuario2.data_nascimento = '17/02/2001'


# Print
print(usuario1.nome_completo())
print(usuario2.nome_completo())
print(usuario1.idade())
print(usuario2.idade())
# construtores
