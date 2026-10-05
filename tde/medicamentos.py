# Este arquivo será responsável pelo CRUD - LISTA
# Aqui ficará as funções de adicionar, ler, deletar e atualizar os medicamentos
# ex. de funções : 
# cadastrar_medicamento()
# listar_medicamentos()
# buscar_medicamento()
# alterar_medicamento()
# remover_medicamento()
# Também terá algumas validações
from validar import (validar_medicamento, validar_texto, validar_estoque,validar_nome, ler_int, ler_float, validar_preco)
from collections import deque 
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
    while True:
        op = ler_int("Digite a categoria [1, 2 ou 3] : ")
        if op == 1: return "Ético"
        if op == 2: return "Genérico"
        if op == 3: return "Similar"
        print("Opção inválida! Escolha 1, 2 ou 3.")

# MENU DE MEDICAMENTOS
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
            "[6] - Listar por categoria \n",
            "[7] - Listar / ordenar por preço \n"
            " [0] - Voltar \n")
        
        # VERIFICA O VALOR DIGITADO
        try :
            op_med = ler_int("Digite sua ação :  ") # verifica se realmente é int
        except ValueError: # caso der "ValueError" ele avisa
            print("Digite apenas números!")
            time.sleep(1)
            continue
        
        print("----------------------------------------")
        
        # MATCH CASE PARA O MENU
        match op_med :
            # adicionar medicamento
            case 1 :
                nome = input("Digite o nome do medicamento: ").strip()
                # valida o nome digitado
                if not validar_nome(nome, medicamentos): 
                    print("\nNome vazio ou já cadastrado.")
                    input("\nPressione ENTER para continuar...")
                    continue
                
                estoque = ler_int("Digite o estoque : ")
                # valida o estoque
                if not validar_estoque(estoque):
                    print("\nDigite um valor válido")
                    input("\nPressione ENTER para continuar...")
                    continue
                
                # dicionário do medicamento
                medicamento = {
                    "medicamento": nome,
                    "categoria": categoria(),
                    "estoque": estoque,
                    "preco": validar_preco("Digite o preço: "), # valida e adiciona o preço
                    "id": gerar_id() # gera um ID único
                }
                
                # VALIDA OS DADOS DO MEDICAMENTO
                resultado = validar_medicamento(
                    medicamento,
                    medicamentos
                )
                
                if resultado is True:
                    # CADASTRA O MEDICAMENTO
                    cadastrar_medicamento(medicamento)
                    print("\nMedicamento cadastrado com sucesso!")

                    # VERIFICA SE O ESTOQUE ESTÁ ABAIXO DO MÍNIMO [15]
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
                alt = input("Digite o medicamento: ") # salva o nome do medicamento
                alterar_medicamento(alt) # redireciona para a função de alteração
                time.sleep(1)
                input("\nPressione ENTER para continuar...")
            
            # REMOÇÃO DE MEDICAMENTO
            case 3 :
                rem = input("Digite o medicamento a ser removido: ") # salva o nome do medicamento
                remover_medicamento(rem) # redireciona para a função de remoção
                time.sleep(1)
                input("\nPressione ENTER para continuar...")
                
            # LISTA TODOS OS MEDICAMENTOS CADASTRADOS
            case 4 :
                listar_medicamentos() # chamada da função de listagem
            
            # BUSCA DE MEDICAMENTO
            case 5 :
                busca = input("Digite o medicamento: ") # salva o nome do medicamento
                buscar_medicamento(busca) # chamada da função de busca
                input("\nPressione ENTER para continuar...")
            
            # LISTAGEM/BUSCA FILTRADA
            case 6 :
                opc_busca_categoria = categoria() # recebe o valor para filtragem
                buscar_medicamento_cat(opc_busca_categoria) # lista pela categoria
                input("\nPressione ENTER para continuar...")

            # LISTAGEM ORDENADA POR PREÇO
            case 7 :
                for i in ordenar_por_preco(medicamentos): # percorre e ordena os medicamentos
                    # printa no terminal
                    print(f"{i['medicamento'].upper()} - R$ {i['preco']} (estoque: {i['estoque']})")
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
    # Repete até o usário digitar [0]
    while True : 
        for i in medicamentos :
            print(f"==================== {i["medicamento"].upper()} ======================= \n")
            print(f"quantidade : {i["estoque"]} " )  
            print(f"preço : {i["preco"]} ")
            print(f"categoria : {i["categoria"]} \n")
        op_listar =  ler_int("[ Digite 0 para SAIR ] : ")
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

    # Se não houver nenhum medicamento com a categoria correspondente
    if not encontrados:
        print(f"Nenhum medicamento cadastrado na categoria {categoria_nome}.")
        return []
    
    # Printa os medicamentos com a categoria desejada
    print(f"=========== CATEGORIA: {categoria_nome.upper()} ({len(encontrados)}) ===========\n")
    for i in encontrados: # percorre os encontrados
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
            opcao = ler_int("O que você deseja alterar ? \n")
            match opcao :
                case 1 :
                    print("-- Escolha a nova categoria --")
                    nova_categoria = categoria()
                    medicamento["categoria"] = nova_categoria # altera a categoria do medicamento
                    time.sleep(0.5)
                    return print("Categoria alterada com sucesso") # printa para o usuário 
                
                case 2 :
                    nova_quantidade = ler_int("Digite a nova quantidade : ")
                    if not validar_estoque(nova_quantidade): # valida o valor digitado
                        return print("Quantidade inválida!")
                    
                    # caso esteja abaixo da quantidade mínima
                    if nova_quantidade < 15 :
                        print("---- Quantidade abaixo do estoque mínimo ! ---")
                        print("Criando pedido de reposição ... ")
                        time.sleep(0.5) # espera 0.5 segundos
                        cadastrar_repo(medicamento) # cria um novo pedido de reposição
                    elif buscar_repo(medicamento) != None : # caso a quantidade for maior e ele estiver para repor
                        cancelar_repo(medicamento) # retira do pedidos de reposição
                        time.sleep(0.5)
                    return print("Quantidade alterada com sucesso") # printa para o usuário 
                
                case 3 :
                    novo_preco = ler_float("Digite o novo preço : ")
                    medicamento["preco"] = novo_preco # altera o preço do medicamento
                    time.sleep(1.5)
                    return print("Preço alterado com sucesso") # printa para o usuário 
                    

# FUNÇÃO PARA REMOVER UM MEDICAMENTO PELO NOME
def remover_medicamento(nome):
    # percorre e encontra o medicamento com o nome
    for medicamento in medicamentos:
        if medicamento["medicamento"].lower() == nome.lower():
            medicamentos.remove(medicamento)
            retirada(medicamento) # adiciona ao histórico a saída do medicamento
            if buscar_repo(medicamento) is not None:
                cancelar_repo(medicamento)  # limpa o pedido de reposição pendente
            return  # achou e removeu: sai da função
    print("medicamento não encontrado !")  # só chega aqui se o for terminar sem achar

# FUNÇÃO PARA ORDENAR POR PREÇO
def ordenar_por_preco(lista):
    """
    Ordena uma lista de dicionários pelo campo "preco" (do menor para o maior)
    usando Bubble Sort. Retorna uma nova lista, sem alterar a original.
    """
    v = lista.copy()  # cópia da lista: evita modificar a lista original

    # Cada passada do loop externo "empurra" o maior elemento restante para o final
    for i in range(len(v)):
        trocou = False  # flag para detectar se houve alguma troca nesta passada

        # Bubble Sort: compara pares de elementos vizinhos
        # O "- i" ignora os últimos i elementos, que já estão na posição correta
        # O "- 1" evita estourar o índice ao acessar v[j+1]
        for j in range(len(v) - i - 1):
            # Se o preço atual for maior que o do próximo, estão fora de ordem
            if v[j]["preco"] > v[j + 1]["preco"]:
                v[j], v[j + 1] = v[j + 1], v[j]  # troca os dois de posição
                trocou = True  # registra que houve troca

        # Se nenhuma troca ocorreu, a lista já está ordenada: encerra antecipadamente
        if not trocou:
            break

    return v  # retorna a lista ordenada