#  Arquivo principal que orquestrará o sistema
# Ele será responsável por:
#     mostrar o menu principal;
#     receber as escolhas do usuário;
#     chamar as funções dos outros arquivos;
#     controlar o fluxo geral do programa.


# IMPORTS
from collections import deque 
from medicamentos import cadastrar_medicamento, listar_medicamentos, medicamentos

while True :
    print("========== SISTEMA DE CONTROLE PharmaERP ============ \n")
    print("[1] - Adicionar medicamento \n",
          "[2] - Ver medicamentos \n",
          "[3] - Sair \n")
    opcao = int(input("Escolha uma opção: \n"))
    
    match opcao :
        case 1 :
            medicamento = {
                "nome": input("Digite o nome do medicamento : "),
                "categoria": input("Digite a categoria : "),
                "estoque": int(input("Digite a quantidade : ")),
                "estoque_minimo": 10,
                "preco": float(input("Digite o preço : ")),
                "id" : len(medicamentos)
            }
            cadastrar_medicamento(medicamento)
        case 2 : 
            listar_medicamentos()
        case 3 : 
            print("Até mais !")
            break
        case _ :
            print("Número errado - sistema encerrado")