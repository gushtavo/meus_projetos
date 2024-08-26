expr = (str(input('Digite uma Expressão: ')))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua Expressão está Válida!')
else:
    print('Sua Expressão está Errada!')
