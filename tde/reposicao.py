# fila de reposição
# CRUD para as solitações de reposição 
# Adicionar as funções de :
# Cadastrar
# Consultar
# Alterar
# Remover
# Listar
# Sam77g : vou adicionar as validações após criar o CRUD inicial
from collections import deque 
from estoque import gerar_id
from estruturas import fila_reposicao, solicitacoes_reposicao
from medicamentos import medicamentos

# cria/cadastra um novo pedido de reposição
def cadastrar_repo(med) :
    # pega o ID e nome do remédio 

    buscar_repo(med)

    repor = {
        "medicamento" : med["nome"],
        "id_repo" : gerar_id,
        "id_medicamento" : med["id"],
        "criticidade" : criticidade(med["estoque"])         
    }

    solicitacoes_reposicao.append(repor["medicamento"])
    return print(repor)

# função auxiliar 
def criticidade(estoque) :

    if estoque < 5:
        return "CRÍTICO"

    elif estoque < 10:
        return "ALERTA"

    elif estoque < 15:
        return "AVISO"

# consulta/busca uma reposição específica
def buscar_repo(med) :
    for repo in solicitacoes_reposicao :
        repo["id_medicamento"] == med["id"]
        return repo
    return None
        

# função de alterar um pedido de reposição
def alterar_repo() :
    return

# função para remover uma solicitação de reposição
def remover_repo() :
    return

#função de listar as solicitações de reposição
def listar_repo() :
    print("=========================== SOLITAÇÕES DE REPOSIÇAO ================================== \n")
    # for med in fila_reposicao :

    return