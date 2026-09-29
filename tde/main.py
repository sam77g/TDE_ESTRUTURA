#  Arquivo principal que orquestrará o sistema
# Ele será responsável por:
#     mostrar o menu principal;
#     receber as escolhas do usuário;
#     chamar as funções dos outros arquivos;
#     controlar o fluxo geral do programa.


# IMPORTS
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
    alterar_repo,
    listar_repo
)

while True :
    print("========== SISTEMA DE CONTROLE PharmaERP ============ \n")
    print(" [1] - Adicionar medicamento \n",
          "[2] - Ver medicamentos \n",
          "[3] - Buscar medicamento \n",
          "[4] - Alterar medicamento \n",
          "[5] - Remover medicamento \n",
          " [0] - Sair \n")
    print("===================================================\n")
    opcao = int(input("Escolha uma opção: "))
    
    match opcao :
        case 1 :
            medicamento = {
                "nome": input("Digite o nome do medicamento : "), # obrigatório
                "categoria": input("Digite a categoria : "), 
                "estoque": int(input("Digite a quantidade : ")), # obrigatório
                "preco": float(input("Digite o preço : ")),
                "id" : gerar_id() # obrigatório
            }
            cadastrar_medicamento(medicamento)
            # verifica se o estoque disponível está menor do que o estoque mínimo
            if medicamento["estoque"] < 15 : 
                # se for menor, ele cadastra automaticamente o pedido de reposição
                cadastrar_repo(medicamento)
                print("Estoque menor que o estoque mínimo !")
                print(f"Criando pedido de reposição para {medicamento['nome'].upper()} !")

        case 2 : 
            listar_medicamentos()
        case 3 : 
            busca = input("Digite o medicamento : ")
            buscar_medicamento(busca)
        case 4 :
            alt = input("Digite o medicamento : ")
            alterar_medicamento(alt)
        case 5 :
            rem = input("Digite o medicamento a ser removido : ")
            remover_medicamento(rem)
        case 0 : 
            print("Até mais !")
            break
        case _ :
            print("Número errado - sistema encerrado")