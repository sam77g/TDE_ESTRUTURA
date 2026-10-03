# =========== IMPORTS ===========
from validar import validar_estoque
from collections import deque
from estoque import gerar_id, gerar_id_repo
from estruturas import solicitacoes_reposicao, limpar_tela, medicamentos 
import time

# ===== MENU DE REPOSIÇÃO ====
def menu_repo():
    while True :
        limpar_tela()
        print("========================================= ")
        print("          MENU DE REPOSIÇÃO            ")
        print("========================================= \n")
        print(" [1] - Buscar reposição \n",
              "[2] - Listar reposições \n",
              "[3] - Atender reposição \n",
              "[4] - Cancelar reposição \n",
              "[5] - Alterar \n",
              " [0] - Voltar \n")
        
        # se digitar letra não quebra, só volta pro menu
        try:
            op_repo = int(input("Digite a ação desejada : "))
        except ValueError:
            print("Digite apenas números!")
            time.sleep(1)
            continue
        print("-----------------------------------")
        match op_repo:
            # 1 - busca pelo nome e mostra se existir
            case 1 :
                nome = input("Digite o nome do medicamento : ")
                repo = buscar_repo(nome)
                if repo is None:
                    print(f"\nNenhuma reposição pendente para '{nome}'.")
                else:
                    exibir_repo(repo)
                input("\nPressione ENTER para continuar...")

            # 2 - lista tudo que está na fila
            case 2:
                listar_repo()
                input("\nPressione ENTER para continuar...")
                
            # 3 - atende sempre a primeira da fila (FIFO)
            case 3 :
                atender_reposicao()
                input("\nPressione ENTER para continuar...")
                
            # 4 - confere se existe antes de cancelar
            case 4 :
                nome = input("Digite o nome do medicamento : ")
                repo = buscar_repo(nome)
                if repo is None:
                    print(f"\nNenhuma reposição pendente para '{nome}'.")
                else:
                    cancelar_repo(nome)
                input("\nPressione ENTER para continuar...")
            # 5 - mesma lógica: só altera se a reposição existir
            case 5 :
                nome = input("Digite o nome do medicamento : ")
                repo = buscar_repo(nome)
                if repo is None:
                    print(f"\nNenhuma reposição pendente para '{nome}'.")
                else:
                    alterar_repo(nome)
                input("\nPressione ENTER para continuar...")
            # 0 - sai do loop e volta pro menu anterior
            case 0:
                print(" -- SAINDO DE REPOSIÇÃO --")
                time.sleep(0.5)
                break

            # qualquer outro número
            case _:
                print("Opção inválida!")
                time.sleep(1)


# FUNÇÃO DE BUSCA 
# aceita o dicionário do medicamento OU só o nome (str); nunca imprime, nunca quebra
def buscar_repo(med):
    if med is None:
        return None

    # se veio dict pega o nome dele, se veio str usa direto
    nome = med["medicamento"] if isinstance(med, dict) else med
    nome = str(nome).strip().lower()   # tira espaço e ignora maiúscula/minúscula

    if not nome:    # string vazia
        return None

    # busca linear na fila comparando pelo nome
    for repo in solicitacoes_reposicao:
        if repo["medicamento"].strip().lower() == nome:
            return repo

    return None

# FUNÇÃO DE CADASTRAR REPOSIÇÃO 
def cadastrar_repo(med) :
    # pega o ID e nome do remédio 

    # se já tem reposição pra esse remédio não duplica
    repo_existente = buscar_repo(med)
    
    if repo_existente is not None :
        return
    # DICIONÁRIO PARA CADA MEDICAMENTO
    repor = {
        "medicamento" : med["medicamento"],
        "id_repo" : gerar_id_repo(),
        "id_medicamento" : med["id"],                    # liga a reposição ao cadastro do remédio
        "criticidade" : criticidade(med["estoque"]),
        "quantidade_solicitada" : 15 - med["estoque"]    # 15 = estoque mínimo, pede só o que falta
    }

    # LISTA DE SOLICITAÇÕES
    solicitacoes_reposicao.append(repor)   # entra no fim da fila
    
    print(f" medicamento : {repor["medicamento"].upper()} \n",
        f"criticidade : {repor["criticidade"]} \n",
        f"ID de reposição : {repor["id_repo"]} \n",)


# FUNLÇAO PARA EXIBIR UMA REPOSIÇÃO JÁ ENCONTRADA
def exibir_repo(repo):
    print(f" nome : {repo['medicamento']} \n",
          f"id de reposição : {repo['id_repo']} \n",
          f"criticidade : {repo['criticidade']} \n",
          f"quantidade solicitada : {repo['quantidade_solicitada']}")


# FUNÇÃO PARA LISTAR AS SOLITAÇÕES
def listar_repo():
    print("=========================== SOLICITAÇÕES DE REPOSIÇÃO ================================== \n")
    if not solicitacoes_reposicao:   # fila vazia
        print("Nenhuma solicitação de reposição pendente.")
        return
    for repo in solicitacoes_reposicao:
        exibir_repo(repo)
        print(" ---------------------------------------- \n")
        
# função auxiliar 
# define o nível de acordo com o estoque atual
def criticidade(estoque):
    if estoque < 5:
        return "CRÍTICO"
    elif estoque < 10:
        return "ALERTA"
    return "AVISO"      # de 10 a 14
        
# FUNÇÃO PARA A REMOÇÃO DE SOLITAÇÃO
# também aceita dict ou nome, igual a buscar_repo
def cancelar_repo(med):
    nome = med["medicamento"] if isinstance(med, dict) else med
    nome = str(nome).strip().lower()
    for repo in solicitacoes_reposicao:
        if repo["medicamento"].strip().lower() == nome:
            solicitacoes_reposicao.remove(repo)   # remove pelo objeto, pode estar em qualquer posição
            print(f"Reposição de {repo['medicamento'].upper()} removida!")
            return
    print("Reposição não encontrada")
            
            
# ATENDE A PRIMEIRA REPOSIÇÃO DA FILA
def atender_reposicao():
    if not solicitacoes_reposicao:
        print("Fila vazia.")
        return

    repo = solicitacoes_reposicao[0]            # só espia, não remove
    print(f"Próxima da fila: {repo['medicamento'].upper()} ({repo['criticidade']})")

    # valida a quantidade ANTES de tirar da fila, assim se errar não perde a solicitação
    try:
        qtd = int(input("Digite a quantidade recebida : "))
    except ValueError:
        print("Digite apenas números!")
        return
    if not validar_estoque(qtd) or qtd == 0:
        print("Quantidade inválida.")
        return

    # procura o medicamento no cadastro pelo id
    med = None
    for m in medicamentos:                      # busca linear na lista de cadastro
        if m["id"] == repo["id_medicamento"]:
            med = m
            break

    solicitacoes_reposicao.popleft()            # só agora sai da fila: O(1)

    # caso o remédio tenha sido excluído enquanto estava na fila
    if med is None:
        print("Medicamento não existe mais; solicitação descartada.")
        return

    med["estoque"] += qtd   # soma o que chegou no estoque
    print(f"{med['medicamento'].upper()}: estoque agora é {med['estoque']}")

    if med["estoque"] < 15:                     # continua baixo: volta pro fim da fila
        print("Ainda abaixo do mínimo; nova solicitação criada.")
        cadastrar_repo(med)
            
# ALTERA A QUANTIDADE SOLICITADA DE UMA REPOSIÇÃO
def alterar_repo(nome):
    repo = buscar_repo(nome)
    if repo is None:
        print("Reposição não encontrada"); return
    try:
        qtd = int(input("Nova quantidade solicitada : "))
    except ValueError:
        print("Digite apenas números!"); return
    if qtd <= 0:    # não aceita 0 nem negativo
        print("A quantidade deve ser maior que 0."); return
    repo["quantidade_solicitada"] = qtd   # repo é a referência da fila, então já atualiza lá
    print("Quantidade solicitada alterada!")