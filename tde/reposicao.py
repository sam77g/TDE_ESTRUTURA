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
from estruturas import fila_reposicao, solicitacoes_reposicao

# cria/cadastra um novo pedido de reposição
def cadastrar_repo(med) :
    # pega o ID e nome do remédio 
    repor = {
        "medicamento" : med["nome"],
        "ID_repo" : med["id"],
        "criticidade" : criticidade(med["estoque"])
            
    }
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
def consultar_repo() :
    return

# função de alterar um pedido de reposição
def alterar_repo() :
    return

# função para remover uma solicitação de reposição
def remover_repo() :
    return

#função de listar as solicitações de reposição
def listar_repo() :
    return