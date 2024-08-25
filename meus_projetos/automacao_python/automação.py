# passo a passo do projeto

# 1. abrir o sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar: pip install pyautogui
import pyautogui
from time import sleep
import pandas as pd

pyautogui.PAUSE = 0.5

# abrir o navegador  (chrome)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no site do sistema
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# aqui pode ser que ele demora alguns segundos para carregar o site
sleep(3)

# 2. fazer o login
pyautogui.click(x=749, y=515)
pyautogui.write('gr5563714@gmail.com')

pyautogui.press('tab')  # passou para o campo de senha
pyautogui.write('Arlicleude1@')

pyautogui.click(x=967, y=734)  # botao de login
sleep(3)

# 3. abrir/importar a base de dados dos produtos para cadastrar
# pip install pandas numpy openpyxl
# tabula -> transfomar 'pdf' em pandas
tabela_produto = pd.read_csv('produtos.csv')

# 4. cadastrar um produto
for linha in tabela_produto.index:

    codigo = tabela_produto.loc[linha, 'codigo']
    marca = tabela_produto.loc[linha, 'marca']
    tipo = tabela_produto.loc[linha, 'tipo']
    categoria = tabela_produto.loc[linha, 'categoria']
    preco_unitario = tabela_produto.loc[linha, 'preco_unitario']
    custo = tabela_produto.loc[linha, 'custo']

    # botao de  codigo do produto
    pyautogui.click(x=640, y=363)
    # prencher o codigo do produto
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press('tab')

    # marca
    pyautogui.write(str(marca))
    # passar para o proximo campo
    pyautogui.press('tab')

    # tipo
    pyautogui.write(str(tipo))
    # passar para o proximo campo
    pyautogui.press('tab')

    # categoria
    pyautogui.write(str(categoria))
    # passar para o proximo campo
    pyautogui.press('tab')

    # preço
    pyautogui.write(str(preco_unitario))
    # passar para o proximo campo
    pyautogui.press('tab')

    # custo
    pyautogui.write(str(custo))
    # passar para o proximo campo
    pyautogui.press('tab')

    # obs
    obs = tabela_produto.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    # passar para o proximo campo
    pyautogui.press('tab')

    # aperta o botão
    pyautogui.press('enter')  # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

# pyperclip -> ajuda a escrever caracteres especiais

# 5. repetir esse processo ate acabar a lista de produtos
