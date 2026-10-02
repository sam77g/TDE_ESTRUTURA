# movimentação do estoque - PILHA
# Esse arquivo será responsável por:
# entrada de medicamentos;
# saída de medicamentos;
# verificar estoque disponível;
# atualizar quantidade;
# registrar movimentações no histórico;
# desfazer a última movimentação.
import time
from estruturas import estoque
from collections import deque 
from relatorios import entrada, retirada
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
            for i in estoque :
                print(f"medicamento : {i["medicamento"].upper()} ")
                print(f"estoque central : {i["estoque_central"]}")
                print(f"id : {i["id"]}")
                print("--------------------- \n")
        case 0 :
            print("Bye ...")
            time.sleep(1.5)
            return
        
# ADICIONA AO ESTOQUE A QUANTIDADE DESEJADA
def adicionar_estoque(med, quantidade):
    if quantidade <= 0:
        return False
    med["estoque_central"] += quantidade

    # REGISTRA NO HISTÓRICO A QUANTIDADE RECEBIDA (sem duplicar o cadastro)
    entrada(med, quantidade)

    print("Entrada registrada com sucesso!")
    
    # ADICIONAR O PROCESSAMENTO DA FILA DE REPOSIÇÃO

    return True

# FUNÇÃO AJUSTE DE ESTOQUE
def ajuste_estoque(med, nova_quantidade):

    if nova_quantidade < 0:
        print("Quantidade inválida!")
        return False

    med["estoque_central"] = nova_quantidade

    print("\nEstoque atualizado!")
    print(f"Estoque central: {med['estoque_central']}")

    return True