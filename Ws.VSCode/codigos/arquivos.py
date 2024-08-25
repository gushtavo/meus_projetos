
# arquivo = open("vendas.txt", "r")

# # fazer o que quiser com o arquivo

# arquivo.close()

with open("vendas.txt", "r") as arquivo:
    # fazer o que quiser com o arquivo
    infos = arquivo.readlines()
vendas_totais = 0
for item in infos:
    item = item.replace("\n", "")
    item = item.replace(" ", "")
    resultado = item.split(",")
    valor = resultado[1]
    valor = float(valor)
    vendas_totais = vendas_totais + valor

print(vendas_totais)