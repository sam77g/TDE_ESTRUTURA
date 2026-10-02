# ARQUIVO COM FUÇÕES PARA O FUNCIONAMENTO DO BALCÃO
def adicionar_balcao() :
    return print("adicionado ao balcão !")

def listar_balcao() :
    return print("lista balcão")

def buscar_balcao() :
    return print("buscar no balcão")

# TRANSFERÊNCIA MANUAL: ESTOQUE CENTRAL -> BALCÃO
def transferir_balcao(med, quantidade):
    # regra 1: quantidade precisa ser maior que zero
    if quantidade <= 0:
        print("Quantidade inválida!")
        return False

    # regra 2: não pode ultrapassar o estoque central
    if quantidade > med["estoque_central"]:
        print(f"Estoque central insuficiente! Disponível: {med['estoque_central']}")
        return False

    # regra 3: diminui o central e aumenta o balcão
    med["estoque_central"] -= quantidade
    med["estoque_balcão"] += quantidade

    print("\nTransferência realizada com sucesso!")
    print(f"Estoque central: {med['estoque_central']}")
    print(f"Estoque balcão: {med['estoque_balcão']}")
    return True


def remover_balcao() :
    return print("Removido do balcão")
