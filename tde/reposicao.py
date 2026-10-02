# fila de reposição
# CRUD para as solitações de reposição 
# Adicionar as funções de :
# Cadastrar
# Consultar
# Alterar
# Remover
# Listar
# Sam77g : vou adicionar as validações após criar o CRUD inicial

# =========== IMPORTS ===========
from collections import deque
from estoque import gerar_id, gerar_id_repo
from estruturas import fila_reposicao, solicitacoes_reposicao, limpar_tela
import time

# ===== MENU DE REPOSIÇÃO ====
def menu_repo():
    while True:
        limpar_tela()
        print("========================================= ")
        print("          MENU DE REPOSIÇÃO            ")
        print("========================================= \n")
        print(" [1] - Buscar reposição \n",
              "[2] - Listar reposições \n",
              "[0] - Voltar \n")

        try:
            op_repo = int(input("Digite a ação desejada : "))
        except ValueError:
            print("Digite apenas números!")
            time.sleep(1)
            continue

        print("-----------------------------------")
        match op_repo:
            case 1:
                nome = input("Digite o nome do medicamento : ")
                repo = buscar_repo(nome)
                if repo is None:
                    print(f"\nNenhuma reposição pendente para '{nome}'.")
                else:
                    exibir_repo(repo)
                input("\nPressione ENTER para continuar...")

            case 2:
                listar_repo()
                input("\nPressione ENTER para continuar...")

            case 0:
                print(" -- SAINDO DE REPOSIÇÃO --")
                time.sleep(0.5)
                break

            case _:
                print("Opção inválida!")
                time.sleep(1)


# =========== BUSCA ===========
# aceita o dicionário do medicamento OU só o nome (str); nunca imprime, nunca quebra
def buscar_repo(med):
    if med is None:
        return None

    nome = med["medicamento"] if isinstance(med, dict) else med
    nome = str(nome).strip().lower()

    if not nome:
        return None

    for repo in solicitacoes_reposicao:
        if repo["medicamento"].strip().lower() == nome:
            return repo

    return None

# ===== CADASTRAR REPOSIÇÃO ======
def cadastrar_repo(med) :
    # pega o ID e nome do remédio 

    repo_existente = buscar_repo(med)
    
    if repo_existente is not None :
        return
    # DICIONÁRIO PARA CADA MEDICAMENTO
    repor = {
        "medicamento" : med["medicamento"],
        "id_repo" : gerar_id_repo(),
        "id_medicamento" : med["id"],
        "criticidade" : criticidade(med["estoque"])
    }

    # LISTA DE SOLICITAÇÕES
    solicitacoes_reposicao.append({
        "id_repo" : repor["id_repo"],
        "medicamento" : repor["medicamento"],
        "criticidade" : repor["criticidade"]
    })
    
    print(f" medicamento : {repor["medicamento"].upper()} \n",
        f"criticidade : {repor["criticidade"]} \n",
        f"ID de reposição : {repor["id_repo"]} \n",)


# exibe uma reposição já encontrada
def exibir_repo(repo):
    print(f" nome : {repo['medicamento']} \n",
          f"id de reposição : {repo['id_repo']} \n",
          f"criticidade : {repo['criticidade']} \n")


# =========== LISTAR ===========
def listar_repo():
    print("=========================== SOLICITAÇÕES DE REPOSIÇÃO ================================== \n")
    if not solicitacoes_reposicao:
        print("Nenhuma solicitação de reposição pendente.")
        return
    for repo in solicitacoes_reposicao:
        exibir_repo(repo)
        print(" ---------------------------------------- \n")
        
# função auxiliar 
def criticidade(estoque):
    if estoque < 5:
        return "CRÍTICO"
    elif estoque < 10:
        return "ALERTA"
    return "AVISO"
        
# função para remover uma solicitação de reposição
def remover_repo(med):
    for repo in solicitacoes_reposicao:
        if repo["medicamento"].lower() == med["medicamento"].lower():
            solicitacoes_reposicao.remove(repo)
            print(f"Reposição de {med['medicamento'].upper()} removida!")
            

# --------- FILA DE REPOSIÇÃO ---------

# FUNÇÃO PARA RETIRAR UM ELEMENTO NA FILA DE REPOSIÇAO
def remove_fila_repo() :
    print(f"remover o medicamento : {fila_reposicao[0]["medicamento"]}")
    yes_or_no = str(input("Vocẽ realmente deseja retirar esse medicamento da fila de reposição ? [s/n] : ").strip().lower())
    if yes_or_no == "s" :
        fila_reposicao.popleft() # retira o primeiro
        print("REMOVENDO ...")
        time.sleep(0.5)
        print(" ---- Item removido com sucesso !! ----")
    else : 
        print("O medicamento continua na FILA ! \n")

# FUNÇÃO PARA MOSTRAR A FILA DE REPOSIÇÃO
def mostrar_fila_repo() :
    print("=========================== FILA DE REPOSIÇAO ================================== \n")
    for medicamento in fila_reposicao :
        print(f" nome : {medicamento["medicamento"]} \n",
              f"id de reposição : {medicamento["id_repo"]} \n",)
        print(" ---------------------------------------- \n")

            