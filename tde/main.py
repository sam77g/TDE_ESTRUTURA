# Arquivo principal que orquestrará o sistema
# Ele será responsável por:
#     mostrar o menu principal;
#     receber as escolhas do usuário;
#     chamar as funções dos outros arquivos;
#     controlar o fluxo geral do programa.


# IMPORTS
import time
from validar import validar_medicamento
from relatorios import (
    listar_historico,
    retirada,
    entrada
)
from estruturas import (
    medicamentos,
    historico,
    fila_reposicao,
    solicitacoes_reposicao
)
from medicamentos import menu_med
from estoque import gerar_id
from reposicao import (
    cadastrar_repo,
    buscar_repo,
    remover_repo,
    listar_repo,
    remove_fila_repo,
    mostrar_fila_repo
)

# =========== SISTEMA PRINCIPAL ===========

while True:
    # MENU DO SISTEMA
    print("========== SISTEMA DE CONTROLE PharmaERP ============ \n")
    print(
        "  [1] - Menu Medicamentos\n",
        " [2] - Estoque \n",
        " [3] - Reposição \n",
        " [4] - Histórico \n",
        "  [0] - Sair \n"
    )
    print("===================================================\n")
    opcao = int(input("Escolha uma opção: "))

    # MATCH CASE PARA A OPÇÃO DIGITADA
    match opcao:
        # vai para o menu de medicamentos
        case 1:
            menu_med()
        # SAIR
        case 0:
            print("Até mais!")
            break

        # OPÇÃO INVÁLIDA
        case _:

            print("Opção inválida! Tente novamente.")