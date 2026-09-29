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
from reposicao import cadastrar_repo
import time

def cadastrar_medicamento(nome) :
    medicamentos.append(nome)
    
def listar_medicamentos() :
    print(medicamentos)

def buscar_medicamento(nome):
    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome.lower():
            return print(f"{medicamento}")
    
    return print("Medicamento não encontrado.")

# função de alterar características do medicamento atrvés do nome digitado
def alterar_medicamento(nome) :
    for medicamento in medicamentos: # percorre a lista de medicamentos
        if medicamento["nome"].lower() == nome.lower(): # verifica se o nome digitado está presente na lista
            print(f" ----- ALTERAR {nome.upper()} ----- \n")
            print("[1] - Categoria \n",
                  "[2] - Estoque / Quantidade \n",
                  "[3] - Preço ")
            opcao = int(input("O que você deseja alterar ? \n"))
            match opcao :
                case 1 :
                    nova_categoria = input("Digite a nova categoria : ")
                    medicamento["categoria"] = nova_categoria # altera a categoria do medicamento
                    return print("Categoria alterada com sucesso") # printa para o usuário 
                
                case 2 :
                    nova_quantidade = int(input("Digite a nova quantidade : "))
                    medicamento["estoque"] = nova_quantidade # altera a quantidade em estoque do sistema
                    
                    if nova_quantidade < 15 :
                        print("---- Quantidade abaixo do estoque mínimo ! ---")
                        print("Criando pedido de reposição ... ")
                        time.sleep(0.75) # espera 1.5 segundos
                        cadastrar_repo(medicamento) # cria um novo pedido de reposição
                        
                    return print("Quantidade alterada com sucesso") # printa para o usuário 
                
                case 3 :
                    novo_preco = float(input("Digite o novo preço : "))
                    medicamento["preco"] = novo_preco # altera o preço do medicamento
                    return print("Preço alterado com sucesso") # printa para o usuário 
                    

# função para remover o medicamento
def remover_medicamento(nome) :  
    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome.lower(): # compara os nomes 
            medicamentos.remove(medicamento)
            return print(f"{nome} removido ! ")
    
    return print("Medicamento não encontrado.")  