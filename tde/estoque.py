# Estoque central (depósito)
# entrada de medicamentos; ajuste de quantidade; listagem e consulta.
# A movimentação estoque -> balcão fica em balcao.py (transferir_estoque_balcao).
import time
from estruturas import (medicamentos, limpar_tela, pausar, localizar_medicamento,
                        msg_ok, msg_aviso, msg_erro)
from validar import validar_quantidade, validar_estoque, ler_inteiro
from relatorios import entrada, ajuste
from reposicao import processar_fila


# ===== LÓGICA (sem print: retorna (ok, mensagem)) =====
def adicionar_estoque(med, quantidade):
    """Entrada de unidades no estoque central."""
    if med is None:
        return False, "Medicamento não encontrado!"
    if not validar_quantidade(quantidade):
        return False, "Quantidade inválida!"
    med["estoque_central"] += quantidade
    entrada(med, quantidade)
    return True, f"Entrada de {quantidade} unidade(s) registrada. Estoque central: {med['estoque_central']}"


def ajustar_estoque(med, nova_quantidade):
    """Define a nova quantidade total do estoque central (correção de inventário)."""
    if med is None:
        return False, "Medicamento não encontrado!"
    if not validar_estoque(nova_quantidade):
        return False, "Quantidade inválida!"
    med["estoque_central"] = nova_quantidade
    ajuste(med, nova_quantidade)
    return True, f"Estoque central atualizado: {med['estoque_central']}"


# ===== EXIBIÇÃO =====
def listar_estoque():
    print(" ------- ESTOQUE PharmaERP ------- \n")
    if not medicamentos:
        msg_aviso("Nenhum medicamento cadastrado.")
        return
    for med in medicamentos:
        print(f" ID {med['id']:<3} | {med['medicamento']:<25} | central: {med['estoque_central']}")


# ===== MENU =====
def menu_estoque():
    while True:
        limpar_tela()
        print("========================================= ")
        print("             MENU DE ESTOQUE              ")
        print("========================================= \n")
        print(" [1] - Listar estoque \n",
              "[2] - Buscar em estoque \n",
              "[3] - Entrada de estoque \n",
              "[0] - Voltar \n")
        op = ler_inteiro("Digite sua ação : ")
        print("----------------------------------------")
        match op:
            case 1:
                listar_estoque()
                pausar()

            case 2:
                med = localizar_medicamento(input("Digite o medicamento: "))
                if med is None:
                    msg_erro("Medicamento não encontrado!")
                else:
                    print(f"{med['medicamento'].upper()} (ID {med['id']}) - estoque central: {med['estoque_central']}")
                pausar()

            case 3:
                med = localizar_medicamento(input("Digite o medicamento: "))
                if med is None:
                    msg_erro("Medicamento não encontrado!")
                else:
                    ok, msg = adicionar_estoque(med, ler_inteiro("Quantidade de entrada: ", 1))
                    (msg_ok if ok else msg_erro)(msg)
                    if ok:
                        for linha in processar_fila():  # novo estoque pode atender pendências
                            print(linha)
                pausar()

            case 0:
                print(" -- SAINDO DE ESTOQUE --")
                time.sleep(0.5)
                break

            case _:
                msg_erro("Opção inválida!")
                time.sleep(1)
