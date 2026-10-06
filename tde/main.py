# Arquivo principal que orquestrará o sistema
# Ele será responsável por:
#     mostrar o menu principal;
#     receber as escolhas do usuário;
#     chamar as funções dos outros arquivos;
#     controlar o fluxo geral do programa.

import pyfiglet
from colorama import Fore, Style, init

# Inicializa o colorama (necessário para compatibilidade com Windows)
init(autoreset=True)

# Gera a arte do texto
texto_art = pyfiglet.figlet_format("PharmaERP", font="slant")

# Imprime o título em verde brilhante
print(Fore.GREEN + Style.BRIGHT + texto_art)

# Subtítulo e descrições
print(Fore.YELLOW + "Sistema de controle farmaceutico\n")
print(
    Fore.GREEN
    + "Samuel , Samoel , Marcos & Gabriel "
    + Fore.WHITE
    + "| "
    + Fore.MAGENTA
    + " TDE Estrutura de Dados \n"
)

# IMPORTS
import time
from relatorios import listar_historico, menu_hist
from estruturas import  DEBUG
from medicamentos import menu_med
from reposicao import  menu_repo
from validar import ler_int

# =========== SISTEMA PRINCIPAL ===========

while True:
    # MENU DO SISTEMA
    print("========== SISTEMA DE CONTROLE PharmaERP ============ \n")
    print(
        "  [1] - Menu Medicamentos\n",
        " [2] - Reposição \n",
        " [3] - Histórico \n",
        " [4] - DEBUG \n"
        "  [0] - Sair \n"
    )
    print("=================================================== \n")
    opcao = ler_int("[OPÇÃO] : ")

    # MATCH CASE PARA A OPÇÃO DIGITADA
    match opcao:
        # MENU DE MEDICAMENTOS
        case 1:
            menu_med()

        # MENU DE REPOSIÇÃO
        case 2 :
            menu_repo()

        # MENU HISTÓRICO
        case 3 :
            menu_hist()

        # DEGUG
        case 4 :
            DEBUG()

        # SAIR
        case 0:
            print("Até mais!")
            break

        # OPÇÃO INVÁLIDA
        case _:
            print("Opção inválida! Tente novamente.")
