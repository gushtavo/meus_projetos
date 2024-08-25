# Modulos e Bibliotecas

import os
# import datetime
# import pyautogui

# print(os.listdir('arquivos'))

# print(datetime.date.today())

# #abrir arquivo excel -> Pandas / base de dados -> openpyxl / editar coluna e afins

# # automação -> pyautogui
# pyautogui.press('win')
# pyautogui.write('chrome')

lista_arquivos = os.listdir('arquivos')
# os.rename('arquivos/abr22.txt', 'arquivos/22/abr22.txt')

for arquivo in lista_arquivos:
    if '.txt' in arquivo:
        if '22' in arquivo:
            os.rename(f'arquivos/{arquivo}', f'arquivos/22/{arquivo}')
            print(f'Movimnetar para pasta 22: {arquivo}')
        else:
            os.rename(f'arquivos/{arquivo}', f'arquivos/23/{arquivo}')
            print(f'Movomentar para pasta 23: {arquivo}')
