palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavara {p.upper()} temos ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')
    