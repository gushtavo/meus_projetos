# print
print('Ola, Mundo!')

nome = input('Seu nome: ')
idade = int(input('Sua idade: '))
print(nome, idade)

# tipos de variaveis
faturamento = 1200  # tipo: int
custo = 750.0  # tipo: float -> numero com casa decimal

novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto = faturamento * 0.1
lucro = faturamento - custo - imposto

margem_lucro = lucro / faturamento

print('Faturamento foi de ', faturamento)
print('O custo foi de ', custo)
print('O lucro da empresa foi de ', lucro)
print('A margem de lucro foi de ', round(margem_lucro, 1))


email = 'qualquerfulano@gmail.com'  # tipo: string -> Texto

teve_lucro = True or False  # tipo: Boolean

# Mod -> % resto da divisão
tempo_contrato = 170
tempo_anos = tempo_contrato / 12
print('Tempos em anos', int(tempo_anos))
tempo_meses = tempo_contrato % 12
print('Tempo em Meses ', tempo_meses)
