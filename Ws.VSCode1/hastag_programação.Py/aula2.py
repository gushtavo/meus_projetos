# strings e Funções de texto
faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento
print(f'Faturameto da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}')

email_cliente = 'gustavo_Relikia7@gmail.com'

#maiuscula
email_cliente = email_cliente.upper()
print(email_cliente)

#minuscula
email_cliente = email_cliente.lower()
print(email_cliente)

# posição do elemento dentro do texto -> "@"
print(email_cliente.find('@')) # -1 quando não encontrar

# tamanho do texto
print(len(email_cliente))

#pegar um caracter
print(email_cliente[16])
print(email_cliente[-4])

#pegar um pedaço do texto
print(email_cliente[7:])

#trocar um pedaço do texto
novo_email = email_cliente.replace('gmail', 'hotmail')
print(novo_email)

#trabalho com nomes
nome = 'gustavo roberto'

print(nome.capitalize()) #somente a primeira palavra com a primeira letra Maiuscula
print(nome.title()) #Primeira letra maiuscula de todas as Palavras

#pegar o servidor do email
posição_arroba = email_cliente.find('@')
servidor = email_cliente[posição_arroba:]
print(servidor)
#pegar o 1 nome
posição_espaço = nome.find(' ')
primeiroNome = nome[:posição_espaço]
print(primeiroNome)
#pegar o 2 nome
posição_espaço = nome.find(' ')
sobrenome = nome[posição_espaço + 1:]
print(sobrenome)

#casos especias -> formatações numericas em texto
margem_lucro = round(margem_lucro, 2)
print(f'Faturameto da empresa: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro: R${lucro:.2f}, Margem: {margem_lucro:.0%}')
