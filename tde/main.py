#  Arquivo principal que orquestrará o sistema
# Ele será responsável por:
#     mostrar o menu principal;
#     receber as escolhas do usuário;
#     chamar as funções dos outros arquivos;
#     controlar o fluxo geral do programa.


# ================ IMPORTS ===================
# funções essencias para o sistema funcionar
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

# ================== Sistema principal ==================
while True :
    # Menu do sistema
    print("========== SISTEMA DE CONTROLE PharmaERP ============ \n")
    print(" [1] - Adicionar medicamento \n",
          "[2] - Ver medicamentos \n",
          "[3] - Buscar medicamento \n",
          "[4] - Alterar medicamento \n",
          "[5] - Remover medicamento \n",
          "[0] - Sair \n")
    print("===================================================\n")
    opcao = int(input("Escolha uma opção: ")) # salva o que foi digitado pelo usuário

    # Match case para cada opção/função
    match opcao :
        case 1 :
            # Dicionário que salva as informações do medicamento a ser adicionado
            medicamento = {
                "nome": input("Digite o nome do medicamento : "), # obrigatório
                "categoria": input("Digite a categoria : "), 
                "estoque": int(input("Digite a quantidade : ")), # obrigatório
                "preco": float(input("Digite o preço : ")),
                "id" : gerar_id() # obrigatório
            }
            cadastrar_medicamento(medicamento) # chamada da função para o cadastro do medicamento

            # verifica se o estoque disponível está menor do que o estoque mínimo
            if medicamento["estoque"] < 15 : 
                cadastrar_repo(medicamento) # se for menor, ele cadastra automaticamente o pedido de reposição
                print("Estoque menor que o estoque mínimo !")
                print(f"Criando pedido de reposição para {medicamento['nome'].upper()} !")

        case 2 : 
            listar_medicamentos() # Printa todos os medicamentos presentes na lista de medicamentos
        case 3 : 
            busca = input("Digite o medicamento : ") # salva o nome para a busca
            buscar_medicamento(busca) # chamada da função resente em medicamentos.py
        case 4 :
            alt = input("Digite o medicamento : ") # salva o nome para alterar um medicamento
            alterar_medicamento(alt)# chamada da função resente em medicamentos.py
        case 5 :
            rem = input("Digite o medicamento a ser removido : ") # salva o nome para remoção de medicamento
            remover_medicamento(rem) # chamada da função resente em medicamentos.py
        case 0 : 
            print("Até mais !") # print quando o usuário digitar para sair
            break
        case _ :
            print("Número errado - sistema encerrado") # print caso o usuário digite o número errado