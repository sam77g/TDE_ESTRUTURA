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
from validar import validar_medicamento, validar_texto, validar_estoque, validar_nome
from estruturas import medicamentos
from relatorios import entrada, retirada
from reposicao import cadastrar_repo, buscar_repo, remover_repo, remove_fila_repo
import time

# FUNÇAO DE CADASTRO DE MEDICAMENTOS
def cadastrar_medicamento(med) :
    medicamentos.append(med) # adiciona o medicamento a lista
    entrada(med) # REGISTRA A ENTRADA
    
    

# FUNÇAO DE LISTAR TODOS OS MEDICAMENTOS
def listar_medicamentos() :
    for i in medicamentos :
        print(f"==================== {i["medicamento"].upper()} ======================= \n")
        print(f"quantidade : {i["estoque"]} " )  
        print(f"preço : {i["preco"]} ")
        print(f"ID : {i["id"]} \n")

# FUNÇÃO DE BUSCAR MEDICAMENTOS
def buscar_medicamento(nome):
    for i in medicamentos :
        if i["medicamento"].lower() == nome.lower(): # compara os nomes 
            print(f"==================== {i["medicamento"].upper()} ======================= \n")
            print(f"quantidade : {i["estoque"]} " )  
            print(f"preço : {i["preco"]} ")
            print(f"ID : {i["id"]} \n")

    

# função de alterar características do medicamento atrvés do nome digitado
def alterar_medicamento(nome) :
    for medicamento in medicamentos: # percorre a lista de medicamentos
        if medicamento["medicamento"].lower() == nome.lower(): # verifica se o nome digitado está presente na lista
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
                    elif buscar_repo(medicamento) != None :
                        remover_repo(medicamento)
                    return print("Quantidade alterada com sucesso") # printa para o usuário 
                
                case 3 :
                    novo_preco = float(input("Digite o novo preço : "))
                    medicamento["preco"] = novo_preco # altera o preço do medicamento
                    return print("Preço alterado com sucesso") # printa para o usuário 
                    

# função para remover o medicamento
def remover_medicamento(nome):
    for medicamento in medicamentos:
        if medicamento["medicamento"].lower() == nome.lower():
            medicamentos.remove(medicamento)
            retirada(medicamento)
            if buscar_repo(medicamento) is not None:
                remover_repo(medicamento)  # limpa o pedido de reposição pendente
    print("medicamento não encontrado !")
    