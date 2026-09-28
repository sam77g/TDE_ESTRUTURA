# Este arquivo será responsável pelo CRUD - LISTA
# Aqui ficará as funções de adicionar, ler, deletar e atualizar os medicamentos
# ex. de funções : 
# cadastrar_medicamento()
# listar_medicamentos()
# buscar_medicamento()
# alterar_medicamento()
# remover_medicamento()
# Também terá algumas validações
from collections import deque 
from estruturas import medicamentos


def cadastrar_medicamento(nome) :
    medicamentos.append(nome)
    
def listar_medicamentos() :
    print(medicamentos)

def buscar_medicamento(nome):
    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome.lower():
            return print(f"{medicamento}")
    
    return None

def alterar_medicamento(nome) :
    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome.lower():
            print(f" ----- ALTERAR {nome.upper()} ----- \n")
            print("[1] - Categoria \n",
                  "[2] - Estoque / Quantidade \n",
                  "[3] - Preço ")
            opcao = int(input("O que você deseja alterar ? \n"))
            match opcao :
                case 1 :
                    nova_categoria = input("Digite a nova categoria : ")
                    medicamento["categoria"] = nova_categoria
                    return "Categoria alterada com sucesso"
                case 2 :
                    nova_quantidade = input("Digite a nova quantidade : ")
                    medicamento["estoque"] = nova_quantidade
                    return "Quantidade alterada com sucesso"
                case 3 :
                    novo_preco = float(input("Digite o novo preço : "))
                    medicamento["preco"] = novo_preco
                    return "Preço alterado com sucesso"
                    

        
def remover_medicamento(nome) :  
    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome.lower():
            medicamentos.pop(medicamento)
            return print(f"{nome} removido ! ")
    
    return None   