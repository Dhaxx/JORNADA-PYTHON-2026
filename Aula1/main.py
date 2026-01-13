'''
1. Entrar no sistema da empresa
2. Efetuar login
3. Carregar base de dados
4. Cadastrar produtos
'''

import pyautogui as pygui
import pandas as pd
from pathlib import Path
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

def carregar_dados() -> pd.DataFrame:
    root_path = Path(__file__).resolve().parent
    dados = pd.read_csv(f'{root_path}/produtos.csv', header=0)
    return dados

def acessar_sistema(site):
    pygui.press('win')
    pygui.write('chrome')
    pygui.press('enter')
    
    sleep(2)
    
    pygui.write(site)
    pygui.press('enter')

def efetuar_login():
    pygui.press('tab')
    pygui.write(os.getenv('EMAIL'))

    pygui.press('tab')
    pygui.write(os.getenv('PASSWORD'))

    pygui.press('tab')
    pygui.press('enter')    

def cadastrar_produto():
    dados = carregar_dados()
    pygui.press('tab')

    for i, dado in dados.iterrows():
        sleep(1.2)
        pygui.write(str(dado['codigo']))
        sleep(0.1)    

        pygui.press('tab')
        pygui.write(str(dado['marca']))
        sleep(0.1)

        pygui.press('tab')
        pygui.write(str(dado['tipo']))
        sleep(0.1)

        pygui.press('tab')
        pygui.write(str(dado['categoria']))
        sleep(0.1)

        pygui.press('tab')
        pygui.write(str(dado['preco_unitario']))
        sleep(0.1)

        pygui.press('tab')
        pygui.write(str(dado['custo']))
        sleep(0.1)

        pygui.press('tab')
        pygui.write(str(dado['obs']))
        sleep(0.1)
        pygui.press('tab')
        pygui.press('enter')

        for _ in range(7):
            pygui.hotkey('shift', 'tab')


acessar_sistema(site=os.getenv('SITE'))
sleep(2)
efetuar_login()
cadastrar_produto()