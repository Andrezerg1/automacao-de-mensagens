'''
Este projeto automatiza o envio de mensagens para clientes.
Autor: André Zerger Bigaran
Data: 26/12/2025
'''

import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

# Carregamento das informações de contato

planilha = openpyxl.load_workbook('numeros.xlsx')
planilha_clientes = planilha['Plan1']

#Bloco prinipal

for linha in planilha_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    mensagem = f'Olá, {nome}. Passando para avisar que o seu boleto vence em {vencimento}'

    link_mensagem = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'

    webbrowser.open(link_mensagem)
    sleep(20)

    # Executa esse bloco de código (envia a mensagem), caso contrário, registra os erros em um arquivo .csv

    try:     
        pyautogui.press('enter')
        sleep(5)
    except:
        print(f'Não foi possivel enviar mensagem para {nome}')
        with open('erros.csv','a',newline='',encoding='utf-8') as arquivo:
            arquivo.write(f'{telefone},{nome}')

    



