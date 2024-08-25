import math

catetoop = float(input('comprimento do CATETO OPOSTO: '))
catetoad = float(input('comprimento do CATETO ADJACENTE: '))

hipotenusa = math.hypot(catetoop, catetoad)
print(f'O triangulo retangulo de cateto oposto {catetoop} e cateto adjacente {catetoad},'
      f' tera a Hipotenusa igual a {hipotenusa:.2f}')
