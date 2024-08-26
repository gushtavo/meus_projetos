vendas = [100, 50, 130, 80, 120, 200]

print(vendas[0])

total_vendas = sum(vendas)
print(total_vendas)
quantidade = len(vendas)
print(quantidade)
valor_max = max(vendas)
valor_min = min(vendas)
print(valor_max, valor_min)

posicao = vendas.index(130)
print("Posicao", posicao)
print(vendas[2:])

produtos = ["iphone", "ipad", "airpod"]
precos = [4000, 8000, 2000]

#edita um item
print("iphone" in produtos)
novo_preco = precos[0] * 1.1
precos[0] = novo_preco
print(precos)

# adiciona um item
produtos.append("macbook")
precos.append(10000)
print(produtos)
print(precos)

# remover um item
produtos.remove("macbook")
precos.pop(-1)
print(produtos)
print(precos)

# inserir um valor
produtos.insert(1, "airpod")
print(produtos)

# contar valores
print(produtos.count("airpod"))

# ordenar
precos.sort(reverse=True)
print(precos)