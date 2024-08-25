lar = float(input('Largura da parede: '))
alt = float(input('altura da parede: '))

area = lar * alt
print(f'Sua para tem a dimensao de {lar}x{alt} e sua area é de {area}m².')

tinta = area / 2.0
print(f'Para pintar essa parede, voce precisara de {tinta}L de tinta.')
