nome = input('Digite seu nome completo: ').strip()
print('Muito prazer em te conhecer!')
divisao = nome.split()
print(f'Seu primeiro nome é {divisao[0]}')
print(f'Seu ultimo nome é {divisao[len(divisao) - 1]}')