#  Arquivo principal que orquestrará o sistema
# Ele será responsável por:
#     mostrar o menu principal;
#     receber as escolhas do usuário;
#     chamar as funções dos outros arquivos;
#     controlar o fluxo geral do programa.


# IMPORTS
import time
from collections import deque 
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
while True :
    # MENU DO SISTEMA
    print("========== SISTEMA DE CONTROLE PharmaERP ============ \n")
    print(" [1] - Adicionar medicamento \n",
          "[2] - Ver medicamentos \n",
          "[3] - Buscar medicamento \n",
          "[4] - Alterar medicamento \n",
          "[5] - Remover medicamento \n",
          "[6] - Fila de reposição \n"
          " [0] - Sair \n")
    print("===================================================\n")
    opcao = int(input("Escolha uma opção: ")) # OPÇÃO ESCOLHIDA

    # MATCH CASE PARA A OPÇÃO DIGITADA
    match opcao :
        # ADICIONAR MEDICAMENTO A LISTA DE MEDICAMENTOS
        case 1 :
            medicamento = {
                "medicamento": str(input("Digite o nome do medicamento : ")), # obrigatório
                "categoria": str(input("Digite a categoria : ")), 
                "estoque": int(input("Digite a quantidade : ")), # obrigatório
                "preco": float(input("Digite o preço : ")),
                "id" : gerar_id() # obrigatório
            }
            cadastrar_medicamento(medicamento) # CADASTRA 
            # verifica se o estoque disponível está menor do que o estoque mínimo
            if medicamento["estoque"] < 15 : 
                # se for menor, ele cadastra automaticamente o pedido de reposição
                print("Estoque menor que o estoque mínimo !")
                print(f"Criando pedido de reposição para {medicamento['medicamento'].upper()} ! \n")
                cadastrar_repo(medicamento)

        case 2 : 
            listar_medicamentos()
        case 3 : 
            busca = input("Digite o medicamento : ")
            buscar_medicamento(busca) # CHAMADA DA FUNÇÃO DE BUSCA
        case 4 :
            alt = input("Digite o medicamento : ")
            alterar_medicamento(alt) # CHAMADA DA FUNÇÃO DE ALTERAÇÃO
        case 5 :
            rem = input("Digite o medicamento a ser removido : ")
            remover_medicamento(rem) # CHAMADA DA FUNÇÃO DE REMOÇÃO 
        case 6 :
            print("nada ainda ...")
            time.sleep(1.0)
        case 0 : 
            print("Até mais !")
            break
        case _ :
            print("Número errado - sistema encerrado")