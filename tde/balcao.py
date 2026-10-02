# Balcão - medicamentos disponíveis para venda
# Única porta de movimentação ESTOQUE CENTRAL -> BALCÃO: transferir_estoque_balcao()
import time
from estruturas import (medicamentos, limpar_tela, pausar, localizar_medicamento,
                        LOTE_REPOSICAO, msg_ok, msg_aviso, msg_erro)
from validar import validar_quantidade, ler_inteiro
from relatorios import transferencia


# ===== LÓGICA (sem print: retorna (ok, mensagem)) =====
def transferir_estoque_balcao(med, quantidade):
    """Move 'quantidade' do estoque central para o balcão, com todas as checagens."""
    if med is None:
        return False, "Medicamento não encontrado!"
    if not validar_quantidade(quantidade):
        return False, "Quantidade inválida!"
    if quantidade > med["estoque_central"]:
        return False, f"Estoque central insuficiente! Disponível: {med['estoque_central']}"

    med["estoque_central"] -= quantidade
    med["estoque_balcao"] += quantidade
    transferencia(med, quantidade)
    return True, (f"{quantidade} unidade(s) de {med['medicamento'].upper()} transferida(s) para o balcão. "
                  f"Central: {med['estoque_central']} | Balcão: {med['estoque_balcao']}")


def distribuir_inicial(med):
    """No cadastro: envia até LOTE_REPOSICAO unidades ao balcão (ou tudo, se houver menos)."""
    quantidade = min(LOTE_REPOSICAO, med["estoque_central"])
    if quantidade <= 0:
        return False, "Sem estoque central para enviar ao balcão."
    return transferir_estoque_balcao(med, quantidade)


# ===== EXIBIÇÃO =====
def listar_balcao():
    print(" ------- BALCÃO PharmaERP ------- \n")
    if not medicamentos:
        msg_aviso("Nenhum medicamento cadastrado.")
        return
    for med in medicamentos:
        print(f" ID {med['id']:<3} | {med['medicamento']:<25} | balcão: {med['estoque_balcao']}")


# ===== MENU =====
def menu_balcao():
    from reposicao import sincronizar_reposicao  # import local: reposicao importa balcao

    while True:
        limpar_tela()
        print("========================================= ")
        print("              MENU DO BALCÃO              ")
        print("========================================= \n")
        print(" [1] - Listar balcão \n",
              "[2] - Consultar quantidade \n",
              "[3] - Transferir estoque -> balcão \n",
              "[0] - Voltar \n")
        op = ler_inteiro("Digite sua ação : ")
        print("----------------------------------------")
        match op:
            case 1:
                listar_balcao()
                pausar()

            case 2:
                med = localizar_medicamento(input("Digite o medicamento: "))
                if med is None:
                    msg_erro("Medicamento não encontrado!")
                else:
                    print(f"{med['medicamento'].upper()} - balcão: {med['estoque_balcao']}")
                pausar()

            case 3:
                med = localizar_medicamento(input("Digite o medicamento: "))
                if med is None:
                    msg_erro("Medicamento não encontrado!")
                else:
                    ok, msg = transferir_estoque_balcao(
                        med, ler_inteiro("Quantidade a transferir para o balcão: ", 1))
                    (msg_ok if ok else msg_erro)(msg)
                    if ok:
                        aviso = sincronizar_reposicao(med)  # balcão pode ter normalizado
                        if aviso:
                            print(aviso)
                pausar()

            case 0:
                print(" -- SAINDO DO BALCÃO --")
                time.sleep(0.5)
                break

            case _:
                msg_erro("Opção inválida!")
                time.sleep(1)
