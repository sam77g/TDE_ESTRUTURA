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
from estoque import gerar_id
import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_med() :
    limpar_tela()
    print("==========================================")
    print("              MENU DE MEDICAMENTOS                   ")
    print("======================================== \n")
    print("[1] - Adicionar medicamento \n",
          "[2] - Alterar medicamento \n",
          "[3] - Remover medicamento \n",
          "[4] - Listar medicamentos \n"
          "[0] - Voltar")
    op_med = int(input("Digite sua ação : "))
    
    match op_med :
        # adicionar medicamento
        case 1 :
            medicamento = {
                "medicamento": input("Digite o nome do medicamento: "),
                "categoria": input("Digite a categoria: "),
                "estoque": int(input("Digite a quantidade: ")),
                "preco": float(input("Digite o preço: ")),
                "id": gerar_id() # gera um ID único
            }
            # VALIDA OS DADOS DO MEDICAMENTO
            resultado = validar_medicamento(
                medicamento,
                medicamentos
            )
            if resultado is True:
                # CADASTRA O MEDICAMENTOW
                cadastrar_medicamento(medicamento)
                print("\nMedicamento cadastrado com sucesso!")

                # VERIFICA SE O ESTOQUE ESTÁ ABAIXO DO MÍNIMO
                if medicamento["estoque"] < 15:
                    print("\nEstoque menor que o estoque mínimo!")
                    print(
                        f"Criando pedido de reposição para "
                        f"{medicamento['medicamento'].upper()}!\n"
                    )
                    cadastrar_repo(medicamento)
            else:
                print(f"\n{resultado}")
        
        # ALTERAÇÃO DE MEDICAMENTO
        case 2 :
            alterar_medicamento()
        
        # REMOÇÃO DE MEDICAMENTO
        case 3 :
            remover_medicamento()
            
        # LISTA TODOS OS MEDICAMENTOS CADASTRADOS
        case 4 :
            listar_medicamentos()
            
        case _ :
            print(" -- SAINDO DE MEDICAMENTOS --")
            time.sleep(0.5)
            return print(" [SUCESS EX]")
            
                

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
    return print("medicamento não encontrado !")
    