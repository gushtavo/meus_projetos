metro = float(input('Uma distancia em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print(f'A medida de {metro}M, correspomde a. \n{km:}KM '
      f'\n{hm:}HM \n{dam}DAM \n{dm:.0f}DM \n{cm:.0f}CM \n{mm:.0f}MM.')
