# Passo a passo do projeto

# Passo 1  - Entrar no sitema da empresa    
# # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui
import pyautogui
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
#uso do pyautogui - clicar (pyautogui.press) - escrever (pyautogui.write) - apertar uma tecla (pyautogui.press) - atalhos (pyautogui.hotkey) - 

pyautogui.PAUSE = 1

# apertar a tecla do windows
pyautogui.press("win")
# digitar o nome do programa
pyautogui.write("chrome")
# apertar enter
pyautogui.press("enter")
# digitar o link
pyautogui.write(link)
# apertar enter
pyautogui.press("enter")
# espera 5 secundos
time.sleep(3)


# Passo 2 - Fazer o login
pyautogui.click(x=446, y=409)

# digitar o email
pyautogui.write("meuEmailPessoal@gmail.com")
# passar para o campo de senha
pyautogui.press("tab")
# digitar a senha e confirmar
pyautogui.write("minhaSenha")

pyautogui.click(x=672, y=570)
time.sleep(3)

# Passo 3 - Importar a base de dados
# # pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4 - Cadastrar um produto
    pyautogui.click(x=406, y=290)
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    # enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)



# passo 5 - Repetir isso até acaba a base de dados 
