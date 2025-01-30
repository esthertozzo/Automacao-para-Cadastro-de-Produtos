# no terminal: pip install pyautogui --- nao sendo necessario instalar novamente
 
"""
passo 1: abrir o sistema da empresa
    abrir o google chrome --> apertar a tecla win; digitar o texto chrome; apertar enter
    entrar no link do sistema --> https://dlp.hashtagtreinamentos.com/python/intensivao/login

passo 2: fazer login
passo 3: pegar a base de dados dos produtos
passo 4: cadastrar um produto
passo 5: repetir o passo 4 até acabar todos os produtos
"""

import pyautogui
import time

pyautogui.PAUSE = 2 # esperar 1 seg para o computador pensar entre um comando e outro

# pyautogui.click -> clicar
# pyautogui.press -> presssionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho de teclado ("ctrl", "c")

# passo 1
pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

# pedir pro computados esperar 3 segundos, pq o site pode demorar para abrir
time.sleep(3)

# passo 2
pyautogui.click(x=205, y=487)
pyautogui.write("tozzo.est@gmail.com")

pyautogui.press('tab') # passa para o campo da senha
pyautogui.write("senha1234567")

pyautogui.press('tab') # passa para o botão logar
pyautogui.press("enter")

# passo 3 importar a base de dados
# pip install pandas openpyxl 
import pandas

# passo 4
# armazenar as informacoes da base de dados numa variavel chamada tabela
tabela = pandas.read_csv("produtos.csv")

print(tabela)

time.sleep(2)

# passo 5
# tabela.index é uma lista com todas as minhas linhas/indices da tabela
for linha in tabela.index:
    pyautogui.click(x=183, y=355)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    # n positivo scroll p cima
    # n negativo scroll pra baixo
    pyautogui.scroll(10000)