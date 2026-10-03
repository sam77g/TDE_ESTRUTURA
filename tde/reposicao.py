
# =========== IMPORTS ===========
from validar import validar_estoque
from collections import deque
from estoque import gerar_id, gerar_id_repo
from estruturas import fila_reposicao, solicitacoes_reposicao, limpar_tela, medicamentos 
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
        
        try:
            op_repo = int(input("Digite a ação desejada : "))
        except ValueError:
            print("Digite apenas números!")
            time.sleep(1)
            continue
        print("-----------------------------------")
        match op_repo:
            case 1 :
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
                
            case 3 :
                atender_reposicao()
                input("\nPressione ENTER para continuar...")
                
            case 4 :
                nome = input("Digite o nome do medicamento : ")
                repo = buscar_repo(nome)
                if repo is None:
                    print(f"\nNenhuma reposição pendente para '{nome}'.")
                else:
                    cancelar_repo(nome)
                input("\nPressione ENTER para continuar...")
            case 5 :
                nome = input("Digite o nome do medicamento : ")
                repo = buscar_repo(nome)
                if repo is None:
                    print(f"\nNenhuma reposição pendente para '{nome}'.")
                else:
                    alterar_repo(nome)
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
        "criticidade" : criticidade(med["estoque"]),
        "quantidade_solicitada" : 15 - med["estoque"]
    }

    # LISTA DE SOLICITAÇÕES
    solicitacoes_reposicao.append({
        "id_repo" : repor["id_repo"],
        "id_medicamento" : repor["id_medicamento"],
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
          f"criticidade : {repo['criticidade']} \n",
          f"quantidade solicitada : {repo['quantidade_solicitada']}")


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
def cancelar_repo(med):
    nome = med["medicamento"] if isinstance(med, dict) else med
    nome = str(nome).strip().lower()
    for repo in solicitacoes_reposicao:
        if repo["medicamento"].strip().lower() == nome:
            solicitacoes_reposicao.remove(repo)
            print(f"Reposição de {repo['medicamento'].upper()} removida!")
            return
    print("Reposição não encontrada")
            
            
def atender_reposicao():
    if not solicitacoes_reposicao:
        print("Fila vazia.")
        return

    repo = solicitacoes_reposicao[0]            # só espia, não remove
    print(f"Próxima da fila: {repo['medicamento'].upper()} ({repo['criticidade']})")

    try:
        qtd = int(input("Digite a quantidade recebida : "))
    except ValueError:
        print("Digite apenas números!")
        return
    if not validar_estoque(qtd) or qtd == 0:
        print("Quantidade inválida.")
        return

    med = None
    for m in medicamentos:                      # busca linear na lista de cadastro
        if m["id"] == repo["id_medicamento"]:
            med = m
            break

    solicitacoes_reposicao.popleft()            # só agora sai da fila: O(1)

    if med is None:
        print("Medicamento não existe mais; solicitação descartada.")
        return

    med["estoque"] += qtd
    print(f"{med['medicamento'].upper()}: estoque agora é {med['estoque']}")

    if med["estoque"] < 15:                     # continua baixo: volta pro fim da fila
        print("Ainda abaixo do mínimo; nova solicitação criada.")
        cadastrar_repo(med)
            
def alterar_repo(nome):
    repo = buscar_repo(nome)
    if repo is None:
        print("Reposição não encontrada"); return
    try:
        qtd = int(input("Nova quantidade solicitada : "))
    except ValueError:
        print("Digite apenas números!"); return
    if qtd <= 0:
        print("A quantidade deve ser maior que 0."); return
    repo["quantidade_solicitada"] = qtd
    print("Quantidade solicitada alterada!")
                