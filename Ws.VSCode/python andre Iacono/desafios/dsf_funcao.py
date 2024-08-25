def calc_tinta(rend, altura, largura):
    metro_quadrado = altura * largura
    total_tinta = metro_quadrado / rend
    return total_tinta


rendimento = int(input('Qual o rendimento da lata em (m²): '))
altura = int(input('Qual altura da parede em (Metros): '))
largura = int(input('Qual a largura da parede em (Metros): '))

total_latas = calc_tinta(rendimento, altura, largura)
print(f'Você precisa de {total_latas} Latas de tinta')
