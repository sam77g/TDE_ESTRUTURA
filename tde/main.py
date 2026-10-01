# Arquivo principal que orquestrará o sistema
# Ele será responsável por:
#     mostrar o menu principal;
#     receber as escolhas do usuário;
#     chamar as funções dos outros arquivos;
#     controlar o fluxo geral do programa.


# IMPORTS
import time
from tde.utils.validar import validar_medicamento
from estruturas import (
    medicamentos,
    historico,
    fila_reposicao,
    solicitacoes_reposicao
)
from medicamentos import (
    cadastrar_medicamento,
    listar_medicamentos,
    buscar_medicamento,
    alterar_medicamento,
    remover_medicamento,
)
from estoque import (
    gerar_id,
    proximo_id
)
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
        " [1] - Adicionar medicamento \n",
        " [2] - Ver medicamentos \n",
        " [3] - Buscar medicamento \n",
        " [4] - Alterar medicamento \n",
        " [5] - Remover medicamento \n",
        " [6] - Fila de reposição \n",
        " [0] - Sair \n"
    )
    print("===================================================\n")
    opcao = int(input("Escolha uma opção: "))

    # MATCH CASE PARA A OPÇÃO DIGITADA
    match opcao:
        # ADICIONAR MEDICAMENTO
        case 1:
            medicamento = {
                "medicamento": input("Digite o nome do medicamento: "),
                "categoria": input("Digite a categoria: "),
                "estoque": int(input("Digite a quantidade: ")),
                "preco": float(input("Digite o preço: ")),
                "id": gerar_id()
            }
            # VALIDA OS DADOS DO MEDICAMENTO
            resultado = validar_medicamento(
                medicamento,
                medicamentos
            )
            if resultado is True:
                # CADASTRA O MEDICAMENTO
                cadastrar_medicamento(medicamento)
                print("\nMedicamento cadastrado com sucesso!")

                # VERIFICA SE O ESTOQUE ESTÁ ABAIXO DO MÍNIMO
                if medicamento["estoque"] < 15:
                    print("\nEstoque menor que o estoque mínimo!")
                    print(
                        f"Criando pedido de reposição para "
                        f"{medicamento['medicamento'].upper()}!\n"
                    )
                    cadastrar_repo(medicamento)
            else:
                print(f"\n{resultado}")

        # LISTAR MEDICAMENTOS
        case 2:
            listar_medicamentos()

        # BUSCAR MEDICAMENTO
        case 3:
            busca = input("Digite o medicamento: ")
            buscar_medicamento(busca)

        # ALTERAR MEDICAMENTO
        case 4:
            alt = input("Digite o medicamento: ")
            alterar_medicamento(alt)

        # REMOVER MEDICAMENTO
        case 5:
            rem = input("Digite o medicamento a ser removido: ")
            remover_medicamento(rem)

        # FILA DE REPOSIÇÃO
        case 6:
            print("nada ainda ...")
            time.sleep(1.0)

        # SAIR
        case 0:
            print("Até mais!")
            break

        # OPÇÃO INVÁLIDA
        case _:

            print("Opção inválida! Tente novamente.")