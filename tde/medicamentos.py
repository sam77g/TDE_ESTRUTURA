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
from estruturas import medicamentos, estoque
from relatorios import entrada, retirada
from reposicao import cadastrar_repo, buscar_repo, remover_repo, remove_fila_repo
from estoque import gerar_id, adicionar_estoque, ajuste_estoque
from balcao import transferir_balcao, adicionar_balcao, remover_balcao
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
            "[6] - Listar por categoria \n",
            "[7] - Adicionar ao estoque \n",
            "[8] - Transferir para o balcão \n",
            " [0] - Voltar \n")
        op_med = int(input("Digite sua ação : "))
        print("----------------------------------------")
        match op_med :
            # adicionar medicamento
            case 1 :
                medicamento = {
                    "medicamento": input("Digite o nome do medicamento: "),
                    "categoria": categoria(),
                    "estoque_central": int(input("Digite a quantidade: ")),
                    "estoque_balcão"  : 0,
                    "preco": float(input("Digite o preço: ")),
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

                    # VERIFICA SE O ESTOQUE DO BALCÃO ESTÁ ABAIXO DO MÍNIMO
                    # (o pedido apenas é CRIADO aqui; o atendimento virá depois)
                    if medicamento["estoque_balcão"] < 15:
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
            
            # ENTRADA NO ESTOQUE CENTRAL
            case 7:
                nome = input("Digite o medicamento: ")
                med = buscar_medicamento(nome)
                if med is not None:
                    quantidade = int(input("Quantidade de entrada: "))
                    if not adicionar_estoque(med, quantidade):
                        print("Quantidade inválida!")
                else:
                    print("Medicamento não encontrado!")
                input("\nPressione ENTER para continuar...") 

            # TRANSFERÊNCIA MANUAL: CENTRAL -> BALCÃO
            case 8:
                nome = input("Digite o medicamento: ")
                med = buscar_medicamento(nome)
                if med is not None:
                    quantidade = int(input("Quantidade a transferir para o balcão: "))
                    transferir_balcao(med, quantidade)
                else:
                    print("Medicamento não encontrado!")
                input("\nPressione ENTER para continuar...")
                
            # SAÍDA
            case 0 :
                print(" -- SAINDO DE MEDICAMENTOS --")
                time.sleep(0.5)
                break
            case _ :
                print(" -- OPÇÃO INVÁLIDA -- ")
                
                    

# FUNÇAO DE CADASTRO DE MEDICAMENTOS
def cadastrar_medicamento(med) :
    medicamentos.append(med) # adiciona o medicamento a lista
    estoque.append({
        "medicamento" : med["medicamento"],
        "id" : med["id"],
        "estoque_central" : med["estoque_central"]
    })
    entrada(med, med["estoque_central"]) # REGISTRA A ENTRADA (antes da distribuição, com a quantidade total)
    distribuir_inicial(med)
    
    

# FUNÇAO DE LISTAR TODOS OS MEDICAMENTOS
def listar_medicamentos() :
    while True :
        for i in medicamentos :
            print(f"==================== {i["medicamento"].upper()} ======================= \n")
            print(f"Estoque : {i["estoque_central"]} " )  
            print(f"Balcão : {i["estoque_balcão"]}")
            print(f"Preço : {i["preco"]} ")
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
        print(f"Estoque : {i["estoque_central"]} " )  
        print(f"Balcão : {i["estoque_balcão"]}")
        print(f"Preço : {i['preco']} ")
        print(f"ID : {i['id']} \n")

    return encontrados

# FUNÇÃO DE BUSCAR MEDICAMENTOS PELO NOME
def buscar_medicamento(nome):
    
    for i in medicamentos :
        if i["medicamento"].strip().lower() == nome.strip().lower(): # compara os nomes 
            print(f"==================== {i["medicamento"].upper()} ======================= \n")
            print(f"Estoque central : {i["estoque_central"]} " )  
            print(f"Balcão : {i["estoque_balcão"]}")
            print(f"preço : {i["preco"]} ")
            print(f"ID : {i["id"]} \n")
            return i
        else :
            return print("Nenhum medicamento encontrado ! \n")

    
# função de alterar características do medicamento atrvés do nome digitado
def alterar_medicamento(nome) :
    for medicamento in medicamentos: # percorre a lista de medicamentos
        if medicamento["medicamento"].strip().lower() == nome.strip().lower(): # verifica se o nome digitado está presente na lista
            print(f" ----- ALTERAR {nome.upper()} ----- ")
            print(" [1] - Categoria \n",
                  "[2] - Estoque central\n",
                  "[3] - Preço ")
            opcao = int(input("O que você deseja alterar ? \n"))
        else :
            return print("Nenhum medicamento encontradado !")
            
        match opcao :
                case 1 :
                    print("-- Escolha a nova categoria --")
                    nova_categoria = categoria()
                    medicamento["categoria"] = nova_categoria # altera a categoria do medicamento
                    time.sleep(0.5)
                    return print("Categoria alterada com sucesso") # printa para o usuário 
                
                # nova quantidade total do estoque central.
                case 2:
                    nova_quantidade = int(input("Digite a nova quantidade do estoque central: "))

                    # A alteração (e a validação) fica centralizada em ajuste_estoque()
                    if not ajuste_estoque(medicamento, nova_quantidade):
                        return

                    print(f"Estoque balcão: {medicamento['estoque_balcão']}")

                    # Verifica se o balcão precisa de reposição
                    if medicamento["estoque_balcão"] < 15:
                        if buscar_repo(medicamento) is None:
                            cadastrar_repo(medicamento)
                            print("\nPedido de reposição criado!")

                    return print("Quantidade alterada com sucesso!")
                
                case 3 :
                    novo_preco = float(input("Digite o novo preço : "))
                    medicamento["preco"] = novo_preco # altera o preço do medicamento
                    time.sleep(1.5)
                    return print("Preço alterado com sucesso") # printa para o usuário 
                    

# função para remover o medicamento
def remover_medicamento(nome):
    for medicamento in medicamentos:
        if medicamento["medicamento"].strip().lower() == nome.strip().lower():
            medicamentos.remove(medicamento)
            retirada(medicamento)
            if buscar_repo(medicamento) is not None:
                remover_repo(medicamento)  # limpa o pedido de reposição pendente
            return  # achou e removeu: sai da função
    print("medicamento não encontrado !")  # só chega aqui se o for terminar sem achar

# DISTRIBUIÇÃO DOS MEDICAMENTOS 
def distribuir_inicial(med) :
    quantidade = min(30, med["estoque_central"])
    if quantidade <= 0 :
        return print("[SYSTEM] : Impossibilitado de distribuir o medicamento para o balcão !")
    else :
        med["estoque_central"] -= quantidade
        med["estoque_balcão"] += quantidade
        print(f" ESTOQUE CENTRAL : {med["estoque_central"]}")
        print(f" BALCÃO : {med["estoque_balcão"]}")
        return print("Transferência Realizada")

