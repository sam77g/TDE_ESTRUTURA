# Vendas - saída de medicamentos do BALCÃO
import time
from estruturas import limpar_tela, pausar, localizar_medicamento, msg_ok, msg_erro
from validar import validar_quantidade, ler_inteiro
from relatorios import venda
from reposicao import sincronizar_reposicao


# ===== LÓGICA =====
def realizar_venda(med, quantidade):
    """Baixa 'quantidade' do balcão. Se o balcão ficar abaixo do limite, gera reposição.
    Retorna (ok, lista_de_mensagens)."""
    if med is None:
        return False, ["Medicamento não encontrado!"]
    if not validar_quantidade(quantidade):
        return False, ["Quantidade inválida!"]
    if quantidade > med["estoque_balcao"]:
        return False, [f"Balcão insuficiente! Disponível: {med['estoque_balcao']}"]

    med["estoque_balcao"] -= quantidade
    venda(med, quantidade)

    total = quantidade * med["preco"]
    msgs = [f"Venda: {quantidade}x {med['medicamento'].upper()} = R$ {total:.2f} "
            f"(balcão restante: {med['estoque_balcao']})"]
    aviso = sincronizar_reposicao(med)
    if aviso:
        msgs.append(aviso)
    return True, msgs


# ===== MENU =====
def menu_vendas():
    while True:
        limpar_tela()
        print("========================================= ")
        print("              MENU DE VENDAS              ")
        print("========================================= \n")
        print(" [1] - Realizar venda \n",
              "[0] - Voltar \n")
        op = ler_inteiro("Digite sua ação : ")
        print("----------------------------------------")
        match op:
            case 1:
                med = localizar_medicamento(input("Digite o medicamento: "))
                if med is None:
                    msg_erro("Medicamento não encontrado!")
                else:
                    print(f"Balcão disponível: {med['estoque_balcao']}")
                    ok, msgs = realizar_venda(med, ler_inteiro("Quantidade vendida: ", 1))
                    for i, m in enumerate(msgs):
                        if i == 0:
                            (msg_ok if ok else msg_erro)(m)
                        else:
                            print(m)
                pausar()

            case 0:
                print(" -- SAINDO DE VENDAS --")
                time.sleep(0.5)
                break

            case _:
                msg_erro("Opção inválida!")
                time.sleep(1)
