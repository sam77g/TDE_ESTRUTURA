# CRUD de medicamentos - LISTA
# cadastrar / listar / buscar / alterar / remover (+ listar por categoria)

import time
from estruturas import (medicamentos, limpar_tela, pausar, gerar_id,
                        localizar_medicamento, msg_ok, msg_aviso, msg_erro)
from validar import (validar_medicamento, validar_nome, ler_inteiro, ler_decimal)
from relatorios import entrada, retirada
from reposicao import sincronizar_reposicao, remover_repo, buscar_repo, processar_fila
from balcao import distribuir_inicial
from estoque import ajustar_estoque

CATEGORIAS = {1: "Ético", 2: "Genérico", 3: "Similar"}


# ===== CATEGORIA =====
def categoria():
    print("[1] - Ético ")
    print("[2] - Genérico")
    print("[3] - Similar \n")
    while True:
        op = ler_inteiro("Qual a categoria ? [1, 2 ou 3] : ")
        if op in CATEGORIAS:
            return CATEGORIAS[op]
        msg_erro("Escolha 1, 2 ou 3.")


# ===== EXIBIÇÃO =====
def exibir_medicamento(med):
    print(f"==================== {med['medicamento'].upper()} ======================= \n")
    print(f"ID : {med['id']}")
    print(f"Categoria : {med['categoria']}")
    print(f"Preço : R$ {med['preco']:.2f}")
    print(f"Estoque central : {med['estoque_central']}")
    print(f"Balcão : {med['estoque_balcao']} \n")


# ===== MENU =====
def menu_med():
    while True:
        limpar_tela()
        print("========================================= ")
        print("          MENU DE MEDICAMENTOS            ")
        print("========================================= \n")
        print(" [1] - Adicionar medicamento \n",
              "[2] - Alterar medicamento \n",
              "[3] - Remover medicamento \n",
              "[4] - Listar medicamentos \n",
              "[5] - Buscar medicamento \n",
              "[6] - Listar por categoria \n",
              "[0] - Voltar \n")
        op_med = ler_inteiro("Digite sua ação : ")
        print("----------------------------------------")
        match op_med:
            case 1:
                nome = input("Digite o nome do medicamento: ").strip()
                med = {
                    "medicamento": nome,
                    "categoria": categoria(),
                    "estoque_central": ler_inteiro("Digite a quantidade: ", 0),
                    "estoque_balcao": 0,
                    "preco": ler_decimal("Digite o preço: ", 0),
                }
                resultado = validar_medicamento(med, medicamentos)
                if resultado is True:
                    med["id"] = gerar_id()  # ID só é consumido se o cadastro for válido
                    for linha in cadastrar_medicamento(med):
                        print(linha)
                else:
                    msg_erro(resultado)
                pausar()

            case 2:
                alterar_medicamento(input("Digite o medicamento: "))
                pausar()

            case 3:
                nome = input("Digite o medicamento a ser removido: ")
                if localizar_medicamento(nome) is None:
                    msg_erro("Medicamento não encontrado!")
                elif input(f"Remover {nome.strip().upper()} e todos os dados relacionados? [s/n] : ").strip().lower() == "s":
                    ok, msg = remover_medicamento(nome)
                    (msg_ok if ok else msg_erro)(msg)
                else:
                    print("Remoção cancelada.")
                pausar()

            case 4:
                listar_medicamentos()
                pausar()

            case 5:
                buscar_medicamento(input("Digite o medicamento: "))
                pausar()

            case 6:
                buscar_medicamento_cat(categoria())
                pausar()

            case 0:
                print(" -- SAINDO DE MEDICAMENTOS --")
                time.sleep(0.5)
                break

            case _:
                msg_erro("Opção inválida!")
                time.sleep(1)


# ===== CREATE =====
def cadastrar_medicamento(med):
    """Cadastra, registra a entrada, distribui ao balcão e abre reposição se preciso.
    Retorna a lista de mensagens para o menu exibir."""
    medicamentos.append(med)
    entrada(med, med["estoque_central"])  # entrada com a quantidade total, antes da distribuição

    msgs = [f"[✓] {med['medicamento'].upper()} cadastrado com sucesso!"]
    ok, msg = distribuir_inicial(med)
    msgs.append(("[✓] " if ok else "[!] ") + msg)

    aviso = sincronizar_reposicao(med)
    if aviso:
        msgs.append(aviso)
    return msgs


# ===== READ =====
def listar_medicamentos():
    if not medicamentos:
        msg_aviso("Nenhum medicamento cadastrado.")
        return
    for med in medicamentos:
        exibir_medicamento(med)


def buscar_medicamento(nome):
    med = localizar_medicamento(nome)
    if med is None:
        msg_erro("Nenhum medicamento encontrado!")
        return None
    exibir_medicamento(med)
    return med


def buscar_medicamento_cat(categoria_nome):
    encontrados = [
        m for m in medicamentos
        if m["categoria"].strip().lower() == categoria_nome.strip().lower()
    ]
    if not encontrados:
        msg_aviso(f"Nenhum medicamento cadastrado na categoria {categoria_nome}.")
        return []

    print(f"=========== CATEGORIA: {categoria_nome.upper()} ({len(encontrados)}) ===========\n")
    for med in encontrados:
        exibir_medicamento(med)
    return encontrados


# ===== UPDATE =====
def alterar_medicamento(nome):
    med = localizar_medicamento(nome)
    if med is None:
        msg_erro("Nenhum medicamento encontrado!")
        return

    print(f" ----- ALTERAR {med['medicamento'].upper()} ----- ")
    print(" [1] - Categoria \n",
          "[2] - Estoque central (ajuste) \n",
          "[3] - Preço \n",
          "[4] - Nome ")
    opcao = ler_inteiro("O que você deseja alterar ? ")

    match opcao:
        case 1:
            print("-- Escolha a nova categoria --")
            med["categoria"] = categoria()
            msg_ok("Categoria alterada com sucesso!")

        case 2:
            nova = ler_inteiro("Digite a nova quantidade do estoque central: ", 0)
            ok, msg = ajustar_estoque(med, nova)
            if not ok:
                msg_erro(msg)
                return
            msg_ok(msg)
            for linha in processar_fila():  # estoque novo pode atender reposições pendentes
                print(linha)

        case 3:
            med["preco"] = ler_decimal("Digite o novo preço : ", 0)
            msg_ok("Preço alterado com sucesso!")

        case 4:
            novo = input("Digite o novo nome : ").strip()
            if not validar_nome(novo, medicamentos, med["id"]):
                msg_erro("Nome inválido ou já utilizado por outro medicamento.")
                return
            repo = buscar_repo(med)
            med["medicamento"] = novo
            if repo is not None:
                repo["medicamento"] = novo  # mantém a fila consistente
            msg_ok("Nome alterado com sucesso!")

        case _:
            msg_erro("Opção inválida!")


# ===== DELETE =====
def remover_medicamento(nome):
    """Remove o medicamento e tudo ligado a ele (estoque e balcão fazem parte do
    registro; a reposição é removida da fila). Retorna (ok, mensagem)."""
    med = localizar_medicamento(nome)
    if med is None:
        return False, "Medicamento não encontrado!"
    medicamentos.remove(med)
    remover_repo(med)
    retirada(med)
    return True, f"{med['medicamento'].upper()} removido (cadastro, estoque, balcão e reposição)."
