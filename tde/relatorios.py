# consultas e relatórios
# Histórico de movimentações = PILHA (o último registro fica no topo).
from datetime import datetime
from estruturas import historico, limpar_tela, pausar


def _registrar(med, tipo, quantidade=None):
    historico.append({
        "medicamento": med["medicamento"],
        "id_medicamento": med["id"],
        "categoria": med["categoria"],
        "tipo": tipo,
        "quantidade": quantidade,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
    })


# Cada função só REGISTRA no histórico (sem print): quem chama decide a mensagem.
def entrada(med, quantidade=None):
    _registrar(med, "ENTRADA", quantidade)


def retirada(med):
    _registrar(med, "SAÍDA")


def transferencia(med, quantidade=None):
    _registrar(med, "TRANSFERÊNCIA", quantidade)


def venda(med, quantidade=None):
    _registrar(med, "VENDA", quantidade)


def ajuste(med, quantidade=None):
    _registrar(med, "AJUSTE", quantidade)


def listar_historico():
    limpar_tela()
    print("========================================= ")
    print("        HISTÓRICO (mais recente primeiro)  ")
    print("========================================= \n")
    if not historico:
        print("Nenhuma movimentação registrada.")
    for i in reversed(historico):  # leitura do topo da pilha para a base
        print(f"==================== {i['medicamento'].upper()} ({i['tipo']}) =======================\n")
        print(f"ID : {i['id_medicamento']}")
        if i.get("quantidade") is not None:
            print(f"Quantidade : {i['quantidade']}")
        print(f"Data : {i['data']} ")
        print(f"Categoria : {i['categoria']} \n")
    pausar()
