# Reposição - FILA (FIFO) de pedidos para reabastecer o balcão
# Pedido: {"id_repo", "id_medicamento", "medicamento", "criticidade"}
# A reposição NÃO cria medicamento: só move unidades do estoque central para o balcão.
import time
from collections import deque
from estruturas import (fila_reposicao, localizar_por_id, gerar_id_repo, limpar_tela, pausar,
                        LIMITE_BALCAO, LOTE_REPOSICAO, msg_erro)
from validar import ler_inteiro
from balcao import transferir_estoque_balcao


# ===== CRITICIDADE (sempre retorna um valor) =====
def criticidade(quantidade):
    if quantidade >= LIMITE_BALCAO:
        return "NORMAL"
    if quantidade >= 10:
        return "AVISO"
    if quantidade >= 5:
        return "ALERTA"
    return "CRÍTICO"


# ===== BUSCA (aceita o dict do medicamento OU o nome; nunca imprime) =====
def buscar_repo(med):
    if med is None:
        return None
    if isinstance(med, dict):
        for repo in fila_reposicao:
            if repo["id_medicamento"] == med["id"]:
                return repo
        return None
    nome = str(med).strip().lower()
    if not nome:
        return None
    for repo in fila_reposicao:
        if repo["medicamento"].strip().lower() == nome:
            return repo
    return None


# ===== ENFILEIRAR =====
def cadastrar_repo(med):
    """Enfileira um pedido. Retorna o pedido, ou None se já existir (sem duplicar)."""
    if buscar_repo(med) is not None:
        return None
    repo = {
        "id_repo": gerar_id_repo(),
        "id_medicamento": med["id"],
        "medicamento": med["medicamento"],
        "criticidade": criticidade(med["estoque_balcao"]),
    }
    fila_reposicao.append(repo)
    return repo


def sincronizar_reposicao(med):
    """Mantém o pedido coerente com o balcão: cria, atualiza a criticidade ou cancela.
    Retorna uma mensagem (ou None se nada mudou de relevante)."""
    repo = buscar_repo(med)
    nome = med["medicamento"].upper()

    if med["estoque_balcao"] >= LIMITE_BALCAO:
        if repo is not None:
            fila_reposicao.remove(repo)
            return f"[✓] Reposição de {nome} cancelada: balcão normalizado."
        return None

    if repo is not None:
        repo["criticidade"] = criticidade(med["estoque_balcao"])
        return None

    repo = cadastrar_repo(med)
    return (f"[!] Balcão de {nome} abaixo de {LIMITE_BALCAO}! Pedido de reposição "
            f"#{repo['id_repo']} criado (criticidade: {repo['criticidade']}).")


# ===== REMOVER =====
def remover_repo(med):
    """Remove da fila todos os pedidos do medicamento. Retorna True se removeu algo."""
    restantes = deque(r for r in fila_reposicao if r["id_medicamento"] != med["id"])
    removeu = len(restantes) != len(fila_reposicao)
    fila_reposicao.clear()
    fila_reposicao.extend(restantes)
    return removeu


# ===== PROCESSAR A FILA (FIFO) =====
def processar_fila():
    """Atende os pedidos na ordem de chegada. Sem estoque central, o pedido continua
    pendente na fila. Retorna a lista de mensagens."""
    msgs = []
    pendentes = deque()

    while fila_reposicao:
        repo = fila_reposicao.popleft()  # primeiro a entrar, primeiro a sair
        med = localizar_por_id(repo["id_medicamento"])
        if med is None:
            continue  # medicamento removido: descarta
        nome = med["medicamento"].upper()

        if med["estoque_balcao"] >= LIMITE_BALCAO:
            continue  # já normalizado: pedido obsoleto

        quantidade = min(LOTE_REPOSICAO, med["estoque_central"])
        if quantidade <= 0:
            msgs.append(f"[!] Não foi possível repor {nome}. Estoque insuficiente (pedido pendente).")
            pendentes.append(repo)
            continue

        ok, msg = transferir_estoque_balcao(med, quantidade)
        msgs.append(("[✓] Reposição: " if ok else "[X] ") + msg)

        if med["estoque_balcao"] < LIMITE_BALCAO:  # repôs só parte: continua pendente
            repo["criticidade"] = criticidade(med["estoque_balcao"])
            pendentes.append(repo)

    fila_reposicao.extend(pendentes)  # mantém a ordem original
    if not msgs:
        msgs.append("Nenhuma reposição pendente.")
    return msgs


# ===== EXIBIÇÃO =====
def exibir_repo(repo):
    print(f" nome : {repo['medicamento']} \n",
          f"id de reposição : {repo['id_repo']} \n",
          f"criticidade : {repo['criticidade']} \n")


def listar_repo():
    print("=========================== FILA DE REPOSIÇÃO ================================== \n")
    if not fila_reposicao:
        print("Nenhuma solicitação de reposição pendente.")
        return
    for posicao, repo in enumerate(fila_reposicao, start=1):
        print(f" posição na fila : {posicao}")
        exibir_repo(repo)
        print(" ---------------------------------------- \n")


# ===== MENU =====
def menu_repo():
    while True:
        limpar_tela()
        print("========================================= ")
        print("          MENU DE REPOSIÇÃO            ")
        print("========================================= \n")
        print(" [1] - Buscar reposição \n",
              "[2] - Listar fila de reposição \n",
              "[3] - Processar fila \n",
              "[0] - Voltar \n")
        op_repo = ler_inteiro("Digite a ação desejada : ")
        print("-----------------------------------")
        match op_repo:
            case 1:
                nome = input("Digite o nome do medicamento : ")
                repo = buscar_repo(nome)
                if repo is None:
                    print(f"\nNenhuma reposição pendente para '{nome}'.")
                else:
                    exibir_repo(repo)
                pausar()

            case 2:
                listar_repo()
                pausar()

            case 3:
                for linha in processar_fila():
                    print(linha)
                pausar()

            case 0:
                print(" -- SAINDO DE REPOSIÇÃO --")
                time.sleep(0.5)
                break

            case _:
                msg_erro("Opção inválida!")
                time.sleep(1)
