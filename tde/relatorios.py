# consultas e relatórios
# Esse arquivo será responsável pelas funcionalidades que analisam os dados.
from collections import deque 
from datetime import datetime
from reposicao import cancelar_repo, cadastrar_repo
from estruturas import historico,limpar_tela, medicamentos
import time
# MENU
def menu_hist() :
    while True:
        limpar_tela()
        print("========================================= ")
        print("             MENU DE HISTÓRICO            ")
        print("========================================= ")
        print(
                " [1] - Listar Histórico \n",
                " [2] - Desfazer / Voltar histórico \n"
                " [0] - Voltar \n"
            )
        try :
            opcao = int(input("Digite a opçao desejada : "))
        except ValueError :
            print("Digite apenas números!")
            time.sleep(1)
            continue
        
        match opcao :
            case 1 :
                listar_historico()
                time.sleep(1)
                input("\nPressione ENTER para continuar...")
                
            case 2 :
                desfazer_ultima()
                time.sleep(1)
                input("\nPressione ENTER para continuar...")
                
            case 0 :
                print("Voltando para o menu principal ...")
                time.sleep(0.5)
                return

# FUNÇÃO DE REGISTRO DE ENTRADA NO ESTOQUE
def entrada(med) :
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y %H:%M") # SALVA O DIA E HORA DE ENTRADA
    
    entry_med = {
        "medicamento" : med["medicamento"],
        "id_medicamento" : med["id"],
        "categoria" : med["categoria"],
        "dados": med.copy(),
        "data" : data_formatada, # saída: dd/mm/2026 hr:min
        "tipo" : "ENTRADA"
    }
    
    historico.append(entry_med) # ENTRADA NO TOPO DA PILHA
    return print(f"O {med["medicamento"]} foi adicionado ao sistema !")

# FUNÇAO DE REGISTRO DE SAÍDA NO ESTOQUE
def retirada(med):
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y %H:%M") # SALVA O DIA E HORA DE RETIRADA
    out_med = {
        "medicamento": med["medicamento"],
        "id_medicamento": med["id"],
        "categoria": med["categoria"],
        "dados": med.copy(),
        "tipo": "SAÍDA",
        "data": data_formatada
    }
    historico.append(out_med)  # registra a saída (antes era historico.pop())
    return print(f"O {med['medicamento'].upper()} foi retirado ")

# FUNÇÃO PARA LISTAR O HISTÓRICO
def listar_historico() :
    limpar_tela()
    for i in reversed(historico) :
        print(f"==================== {i['medicamento'].upper()} ({i['tipo']}) =======================\n")
        print(f"ID : {i['id_medicamento']} \n")
        print(f"Data : {i['data']} \n") 
        print(f"Categoria : {i['categoria']}") 

def desfazer_ultima():
    if not historico:
        print("Nada para desfazer.")
        return
    mov = historico.pop()                       # só mexe no topo
    if mov["tipo"] == "ENTRADA":                # desfaz entrada = remove o medicamento
        medicamentos[:] = [m for m in medicamentos if m["id"] != mov["id_medicamento"]]
        cancelar_repo(mov["dados"])
    else:                                       # desfaz saída = devolve o medicamento
        med = mov["dados"]
        medicamentos.append(med)
        if med["estoque"] < 15:
            cadastrar_repo(med)
    print(f"Desfeito: {mov['tipo']} de {mov['medicamento']}")