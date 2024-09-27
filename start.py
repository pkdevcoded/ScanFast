import os
import shutil
import time
import sys
from datetime import datetime

pasta_fotos = 'fotos'
pasta_verificadas = 'fotoverificada'
arquivo_lista = 'lista.txt'
arquivo_log = 'no_search.log'

class Cores:
    VERDE = "\033[92m"
    VERMELHO = "\033[91m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    RESET = "\033[0m"

def cabecalho():
    print(f"{Cores.AZUL}{'=' * 50}")
    print(f"{Cores.AZUL}{' '*15}Início da Verificação de Arquivos{' '*15}{Cores.AZUL}")
    print(f"{Cores.AZUL}{'=' * 50}{Cores.RESET}\n")

def mover_arquivos():
    with open(arquivo_lista, 'r') as f:
        arquivos = [linha.strip() for linha in f.readlines()]
    arquivos_png = [arquivo + '.png' if not arquivo.endswith('.png') else arquivo for arquivo in arquivos]
    total_arquivos = len(arquivos_png)

    for idx, arquivo in enumerate(arquivos_png):
        caminho_arquivo = os.path.join(pasta_fotos, arquivo)
        print(f"{Cores.AMARELO}Verificando o arquivo: {caminho_arquivo}{Cores.RESET}")
        progresso = 0

        if os.path.exists(caminho_arquivo):
            shutil.move(caminho_arquivo, os.path.join(pasta_verificadas, arquivo))
            print(f"{Cores.VERDE}{arquivo} movido para {pasta_verificadas}.{Cores.RESET}")
        else:
            with open(arquivo_log, 'a') as log:
                log.write(f'{arquivo}\n')
            print(f"{Cores.VERMELHO}{arquivo} não encontrado, registrado no log.{Cores.RESET}")

        progresso = (idx + 1) / total_arquivos
        bar_length = 50
        block = int(bar_length * progresso)
        progress_bar = f"{Cores.AZUL}[{'#' * block}{'-' * (bar_length - block)}] {progresso * 100:.2f}%"
        
        print(f"\r{progress_bar}", end="")
        time.sleep(0.1)

    print()

    for arquivo in os.listdir(pasta_fotos):
        if arquivo.endswith('.png'):
            caminho_arquivo = os.path.join(pasta_fotos, arquivo)
            shutil.move(caminho_arquivo, 'lixeiro')

def verificar_periodo_dia():
    hora_atual = datetime.now().hour
    if 6 <= hora_atual < 12:
        return "Bom dia!"
    elif 12 <= hora_atual < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

def exibir_mensagem_grande(mensagem):
    tamanho = len(mensagem) + 4
    print(f"{Cores.AZUL}{'=' * tamanho}")
    print(f"{Cores.AZUL}| {mensagem} |")
    print(f"{Cores.AZUL}{'=' * tamanho}{Cores.RESET}")

def contagem_regressiva(segundos):
    for i in range(segundos, 0, -1):
        print(f"\r{Cores.AMARELO}{i} segundos{Cores.RESET}", end="")
        time.sleep(1)
    print(f"\r{Cores.VERDE}Start!{Cores.RESET}")

def menu():
    print(f"{Cores.AZUL}{'=' * 20} MENU {'=' * 20}{Cores.RESET}")
    print("1. Iniciar verificação")
    print("2. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Preparando para iniciar a verificação")
        contagem_regressiva(5)
        cabecalho()
        mover_arquivos()
        print(f"{Cores.AZUL}{'=' * 50}{Cores.RESET}")

        # Exibe a mensagem de despedida
        mensagem = verificar_periodo_dia() + " Tchau!"
        exibir_mensagem_grande(mensagem)
        input("Pressione Enter para sair...")
    elif opcao == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        mensagem = verificar_periodo_dia() + " Tchau!"
        exibir_mensagem_grande(mensagem)
        input("Pressione Enter para sair...")
    else:
        print(f"{Cores.VERMELHO}Opção inválida! Tente novamente.{Cores.RESET}")

menu()
