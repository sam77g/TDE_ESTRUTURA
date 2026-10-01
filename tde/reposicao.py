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
from estruturas import fila_reposicao, solicitacoes_reposicao
from estruturas import medicamentos
import time

# =========== FUNÇÕES PRINCIPAIS / CRUD ===========

# cria/cadastra um novo pedido de reposição
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
    
    #  fila inutilizada
    # ADICIONA A FILA DE REPOSIÇÃO
    # fila_reposicao.append({
    #     "id_repo" : repor["id_repo"],
    #     "medicamento" : repor["medicamento"]
    # })
    
    print(f" medicamento : {repor["medicamento"].upper()} \n",
        f"criticidade : {repor["criticidade"]} \n",
        f"ID de reposição : {repor["id_repo"]} \n",)


# função auxiliar 
def criticidade(estoque):
    if estoque < 5:
        return "CRÍTICO"
    elif estoque < 10:
        return "ALERTA"
    return "AVISO"

# consulta/busca uma reposição específica
def buscar_repo(med) :
    for repo in solicitacoes_reposicao :
        if repo["medicamento"] == med["medicamento"] :
            return repo
            
    return None

# função para remover uma solicitação de reposição
def remover_repo(med):
    for repo in solicitacoes_reposicao:
        if repo["medicamento"].lower() == med["medicamento"].lower():
            solicitacoes_reposicao.remove(repo)
            print(f"Reposição de {med['medicamento'].upper()} removida!")
            return
            
            

#função de listar as solicitações de reposição
def listar_repo() :
    print("=========================== SOLITAÇÕES DE REPOSIÇAO ================================== \n")
    for medicamento in solicitacoes_reposicao :
        print(f" nome : {medicamento["medicamento"]} \n",
              f"id de reposição : {medicamento["id_repo"]} \n",
              f"criticidae : {medicamento["criticidade"]}\n")
        print(" ---------------------------------------- \n")

# --------- FILA DE REPOSIÇÃO ---------
# Não será usada atualmente (30/09/2026). Ass.: Samuel - sam77g
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
# Inutilizado na main para o menu
    # mostrar_fila_repo()
    # print(" [s/n] - remover o primeiro item da fila de reposição ? \n")
    # opc = str(input("digite : ").strip().lower())
    # if opc == "s" :
    #     remove_fila_repo()
            