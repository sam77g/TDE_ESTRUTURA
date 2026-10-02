# movimentação do estoque - PILHA
# Esse arquivo será responsável por:
# entrada de medicamentos;
# saída de medicamentos;
# verificar estoque disponível;
# atualizar quantidade;
# registrar movimentações no histórico;
# desfazer a última movimentação.
import time
from collections import deque 
# GERA OS IDs PARA OS MEDICAMENTOS
proximo_id = 1
def gerar_id():
    global proximo_id

    id_atual = proximo_id
    proximo_id += 1

    return id_atual

# GERA OS IDs PARA AS REPOSIÇÕES
proximo_id_repo = 1
def gerar_id_repo():
    global proximo_id_repo

    id_atual = proximo_id_repo
    proximo_id_repo += 1

    return id_atual

def menu_estoque() :
    print("========================================= ")
    print("             MENU DE ESTOQUE              ")
    print("========================================= \n")
    print("[1] - Listar estoque \n",
          "[2] - Buscar em estoque \n",
          "[0] - Sair")
    op_estq = int(input("Digite sua ação : "))
    match op_estq :
        case 1 :
            print(" ------- ESTOQUE PharmaERP ------- \n")
        case 0 :
            print("Bye ...")
            time.sleep(1.5)
            return