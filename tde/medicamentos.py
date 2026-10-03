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
from reposicao import cadastrar_repo, buscar_repo, cancelar_repo
from estoque import gerar_id
import time
import os

# FUNÇÃO PARA LIMPAR TELA
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# FUNÇÃO PARA CATEGORIAS
def categoria() :
    print("[1] - Ético ")
    print("[2] - Genérico")
    print("[3] - Similar \n")
    categoria_op = int(input("Qual a categoria ? [1,2 ou 3] : "))
    if categoria_op == 1 :
        return "Ético"
    elif categoria_op == 2 :
        return "Genérico"
    else :
        return "Similar"

def menu_med() :
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
            "[6] - Listar por categoria \n"
            " [0] - Voltar \n")
        op_med = int(input("Digite sua ação : "))
        print("----------------------------------------")
        match op_med :
            # adicionar medicamento
            case 1 :
                medicamento = {
                    "medicamento": input("Digite o nome do medicamento: "),
                    "categoria": categoria(),
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
                    input("\nPressione ENTER para continuar...")
                else:
                    print(f"\n{resultado}")
            
            # ALTERAÇÃO DE MEDICAMENTO
            case 2 :
                alt = input("Digite o medicamento: ")
                alterar_medicamento(alt)
                time.sleep(1)
                input("\nPressione ENTER para continuar...")
            
            # REMOÇÃO DE MEDICAMENTO
            case 3 :
                rem = input("Digite o medicamento a ser removido: ")
                remover_medicamento(rem)
                time.sleep(1)
                input("\nPressione ENTER para continuar...")
                
            # LISTA TODOS OS MEDICAMENTOS CADASTRADOS
            case 4 :
                listar_medicamentos()
            
            # BUSCA DE MEDICAMENTO
            case 5 :
                busca = input("Digite o medicamento: ")
                buscar_medicamento(busca)
                input("\nPressione ENTER para continuar...")
            case 6 :
                opc_busca_categoria = categoria()
                buscar_medicamento_cat(opc_busca_categoria)
                input("\nPressione ENTER para continuar...")
                
            # SAÍDA
            case _ :
                print(" -- SAINDO DE MEDICAMENTOS --")
                time.sleep(0.5)
                break
                
                    

# FUNÇAO DE CADASTRO DE MEDICAMENTOS
def cadastrar_medicamento(med) :
    medicamentos.append(med) # adiciona o medicamento a lista
    entrada(med) # REGISTRA A ENTRADA
    
    

# FUNÇAO DE LISTAR TODOS OS MEDICAMENTOS
def listar_medicamentos() :
    while True :
        for i in medicamentos :
            print(f"==================== {i["medicamento"].upper()} ======================= \n")
            print(f"quantidade : {i["estoque"]} " )  
            print(f"preço : {i["preco"]} ")
            print(f"categoria : {i["categoria"]} \n")
        op_listar = int(input("[ Digite 0 para SAIR ] : "))
        if op_listar == 0 :
            return False
        else : 
            break

# FUNÇÃO DE BUSCAR MEDICAMENTOS POR CATEGORIA
def buscar_medicamento_cat(categoria_nome):
    # filtra todos os medicamentos da mesma categoria
    # Equivale a :
    # encontrados = []
    # for m in medicamentos:
    #     if m["categoria"].strip().lower() == categoria_nome.strip().lower():
    #         encontrados.append(m)
    encontrados = [
        # percorre a lista de medicamentos 
        m for m in medicamentos 
        # e guarda os correspondedes em uma lista nova
        if m["categoria"].strip().lower() == categoria_nome.strip().lower()
    ]

    if not encontrados:
        print(f"Nenhum medicamento cadastrado na categoria {categoria_nome}.")
        return []

    print(f"=========== CATEGORIA: {categoria_nome.upper()} ({len(encontrados)}) ===========\n")
    for i in encontrados:
        print(f"==================== {i['medicamento'].upper()} ======================= \n")
        print(f"quantidade : {i['estoque']} ")
        print(f"preço : {i['preco']} ")
        print(f"ID : {i['id']} \n")

    return encontrados

# FUNÇÃO DE BUSCAR MEDICAMENTOS PELO NOME
def buscar_medicamento(nome):
    
    for i in medicamentos :
        if i["medicamento"].lower() == nome.lower(): # compara os nomes 
            print(f"==================== {i["medicamento"].upper()} ======================= \n")
            print(f"quantidade : {i["estoque"]} " )  
            print(f"preço : {i["preco"]} ")
            print(f"ID : {i["id"]} \n")
            return i

    
# função de alterar características do medicamento atrvés do nome digitado
def alterar_medicamento(nome) :
    for medicamento in medicamentos: # percorre a lista de medicamentos
        if medicamento["medicamento"].lower() == nome.lower(): # verifica se o nome digitado está presente na lista
            print(f" ----- ALTERAR {nome.upper()} ----- ")
            print(" [1] - Categoria \n",
                  "[2] - Estoque / Quantidade \n",
                  "[3] - Preço ")
            opcao = int(input("O que você deseja alterar ? \n"))
            match opcao :
                case 1 :
                    print("-- Escolha a nova categoria --")
                    nova_categoria = categoria()
                    medicamento["categoria"] = nova_categoria # altera a categoria do medicamento
                    time.sleep(0.5)
                    return print("Categoria alterada com sucesso") # printa para o usuário 
                
                case 2 :
                    nova_quantidade = int(input("Digite a nova quantidade : "))
                    medicamento["estoque"] = nova_quantidade # altera a quantidade em estoque do sistema
                    
                    if nova_quantidade < 15 :
                        print("---- Quantidade abaixo do estoque mínimo ! ---")
                        print("Criando pedido de reposição ... ")
                        time.sleep(0.5) # espera 0.5 segundos
                        cadastrar_repo(medicamento) # cria um novo pedido de reposição
                    elif buscar_repo(medicamento) != None :
                        cancelar_repo(medicamento)
                        time.sleep(0.5)
                    return print("Quantidade alterada com sucesso") # printa para o usuário 
                
                case 3 :
                    novo_preco = float(input("Digite o novo preço : "))
                    medicamento["preco"] = novo_preco # altera o preço do medicamento
                    time.sleep(1.5)
                    return print("Preço alterado com sucesso") # printa para o usuário 
                    

# função para remover o medicamento
def remover_medicamento(nome):
    for medicamento in medicamentos:
        if medicamento["medicamento"].lower() == nome.lower():
            medicamentos.remove(medicamento)
            retirada(medicamento)
            if buscar_repo(medicamento) is not None:
                cancelar_repo(medicamento)  # limpa o pedido de reposição pendente
            return  # achou e removeu: sai da função
    print("medicamento não encontrado !")  # só chega aqui se o for terminar sem achar
    
def ordenar_por_preco(lista):
    v = lista.copy()
    for i in range(len(v)):
        for j in range(len(v) - i - 1):
            if v[j]["preco"] > v[j+1]["preco"]:
                v[j], v[j+1] = v[j+1], v[j]
    return v    # O(n²) pior caso; O(n) melhor caso se parar quando não houver trocas