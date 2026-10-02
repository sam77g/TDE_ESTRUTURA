# Arquivo principal - orquestra o sistema (menu principal e fluxo geral)
from estruturas import DEBUG, msg_erro
from validar import ler_inteiro
from relatorios import listar_historico
from medicamentos import menu_med
from estoque import menu_estoque
from balcao import menu_balcao
from vendas import menu_vendas
from reposicao import menu_repo
import time

# =========== SISTEMA PRINCIPAL ===========
while True:
    print("========== SISTEMA DE CONTROLE PharmaERP ============ \n")
    print(
        "  [1] - Medicamentos \n",
        " [2] - Estoque \n",
        " [3] - Balcão \n",
        " [4] - Vendas \n",
        " [5] - Reposição \n",
        " [6] - Histórico \n",
        " [7] - DEBUG \n",
        " [0] - Sair \n"
    )
    print("=================================================== \n")
    opcao = ler_inteiro("Escolha uma opção: ")

    match opcao:
        case 1:
            menu_med()
        case 2:
            menu_estoque()
        case 3:
            menu_balcao()
        case 4:
            menu_vendas()
        case 5:
            menu_repo()
        case 6:
            listar_historico()
        case 7:
            DEBUG()
        case 0:
            print("Até mais!")
            break
        case _:
            msg_erro("Opção inválida! Tente novamente.")
            time.sleep(1)
