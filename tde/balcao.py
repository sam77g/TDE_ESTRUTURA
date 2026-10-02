# ARQUIVO COM FUÇÕES PARA O FUNCIONAMENTO DO BALCÃO
#  Imports 
from medicamentos import buscar_medicamento
from estruturas import balcao

def menu_balcao() :
    print(" =========== MENU BALCÃO =========== \n")
    print("[1] - Listar Balcão ")
    print("[2] - Transferir para o balcão ")
    print("[3] - Buscar no balcão ")
    print("[0] - SAIR \n")
    
    op_balc = int(input("Opção : "))
    match op_balc :
        case 1 :
            listar_balcao()
        case 2 :
            nome = input("O nome do medicamento : ")
            med = buscar_medicamento(nome)
            transferir_balcao(med)
        case 3 :
            busca_balc = input("Digite o medicamento : ")
            buscar_balcao(buscar_balcao)

def adicionar_balcao() :
    return print("adicionado ao balcão !")

def listar_balcao(med) :
    for i in balcao :
        if i["medicamento"].strip().lower() == med.strip().lower() :
            print(f" ----------- {med.upper()} ----------- ")
            print(f"Quantidade no balcão : {i["estoque_balcao"]}")
        
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
