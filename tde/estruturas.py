# ESTRUTURAS LINEARES E UTILITÁRIOS DO SISTEMA
#   LISTA  -> medicamentos          (cadastro: percorrer, buscar, alterar, remover)
#   PILHA  -> historico             (list: append = push, reversed = do topo p/ base)
#   FILA   -> fila_reposicao        (deque: append = enfileira, popleft = atende; FIFO)
from collections import deque
import os

# ===== REGRAS DE NEGÓCIO =====
LIMITE_BALCAO = 15    # balcão abaixo disso gera pedido de reposição
LOTE_REPOSICAO = 30   # quantidade enviada do estoque central para o balcão

# ===== ESTRUTURAS =====
# Medicamento: {"id", "medicamento", "categoria", "preco", "estoque_central", "estoque_balcao"}
medicamentos = []
historico = []
# Pedido: {"id_repo", "id_medicamento", "medicamento", "criticidade"}
fila_reposicao = deque()

# ===== GERADORES DE ID =====
proximo_id = 1
proximo_id_repo = 1


def gerar_id():
    global proximo_id
    id_atual = proximo_id
    proximo_id += 1
    return id_atual


def gerar_id_repo():
    global proximo_id_repo
    id_atual = proximo_id_repo
    proximo_id_repo += 1
    return id_atual


# ===== BUSCAS SEM EFEITO COLATERAL (nunca imprimem) =====
def localizar_medicamento(nome):
    if not isinstance(nome, str):
        return None
    nome = nome.strip().lower()
    for med in medicamentos:
        if med["medicamento"].strip().lower() == nome:
            return med
    return None


def localizar_por_id(id_med):
    for med in medicamentos:
        if med["id"] == id_med:
            return med
    return None


# ===== INTERFACE (padrão de mensagens) =====
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input("\nPressione ENTER para continuar...")


def msg_ok(texto):
    print(f"[✓] {texto}")


def msg_aviso(texto):
    print(f"[!] {texto}")


def msg_erro(texto):
    print(f"[X] {texto}")


# ===== DEBUG =====
def DEBUG():
    print("-- PILHA DO HISTÓRICO -- \n")
    print(historico, "\n")
    print("-- FILA DE REPOSIÇÃO -- \n")
    print(fila_reposicao, "\n")
    print("-- MEDICAMENTOS -- \n")
    print(medicamentos, "\n")
    pausar()
