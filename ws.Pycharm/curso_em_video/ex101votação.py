def voto(n):
    from datetime import date
    idade = date.today().year - n
    if idade < 16:
        return f'Com {idade} anos: Não VOTA.'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('-' * 30)
nasc = int(input('Em que ano você nasceu: '))
print(voto(nasc))
