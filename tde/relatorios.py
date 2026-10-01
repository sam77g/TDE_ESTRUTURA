# consultas e relatórios
# Esse arquivo será responsável pelas funcionalidades que analisam os dados.
from collections import deque 
from datetime import datetime
from estruturas import historico

# FUNÇÃO DE REGISTRO DE ENTRADA NO ESTOQUE
def entrada(med) :
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y %H:%M") # SALVA O DIA E HORA DE ENTRADA
    
    entry_med = {
        "medicamento" : med["medicamento"],
        "id_medicamento" : med["id"],
        "categoria" : med["categoria"],
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
        "tipo": "SAÍDA",
        "data": data_formatada
    }
    historico.append(out_med)  # registra a saída (antes era historico.pop())
    return print(f"O {med['medicamento'].upper()} foi retirado ")

# FUNÇÃO PARA LISTAR O HISTÓRICO
def listar_historico() :
    for i in historico :
        print(f"==================== {i['medicamento'].upper()} ({i['tipo']}) =======================\n")
        print(f"ID : {i['id_medicamento']} \n")
        print(f"Data : {i['data']} \n")  

