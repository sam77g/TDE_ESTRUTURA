# Arquivo principal que orquestrará o sistema
# Ele será responsável por:
#     mostrar o menu principal;
#     receber as escolhas do usuário;
#     chamar as funções dos outros arquivos;
#     controlar o fluxo geral do programa.


# IMPORTS
import time
from validar import validar_medicamento
from relatorios import listar_historico
from estruturas import limpar_tela, DEBUG
from medicamentos import menu_med
from estoque import gerar_id, menu_estoque
from reposicao import  menu_repo

# =========== SISTEMA PRINCIPAL ===========

while True:
    # MENU DO SISTEMA
    print("========== SISTEMA DE CONTROLE PharmaERP ============ \n")
    print(
        "  [1] - Menu Medicamentos\n",
        " [2] - Estoque \n",
        " [3] - Reposição \n",
        " [4] - Histórico \n",
        " [5] - DEBUG"
        " [0] - Sair \n"
    )
    print("=================================================== \n")
    opcao = int(input("Escolha uma opção: "))

    # MATCH CASE PARA A OPÇÃO DIGITADA
    match opcao:
        # MENU DE MEDICAMENTOS
        case 1:
            menu_med()

        # MENU DE ESTOQUE
        case 2 :
            menu_estoque()

        # MENU DE REPOSIÇÃO
        case 3 :
            menu_repo()

        # LISTAR O HISTÓRICO
        case 4 :
            listar_historico()

        # DEGUG
        case 5 :
            DEBUG()
            
        # SAIR
        case 0:
            print("Até mais!")
            break

        # OPÇÃO INVÁLIDA
        case _:

            print("Opção inválida! Tente novamente.")