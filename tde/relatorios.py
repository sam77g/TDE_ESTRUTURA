# consultas e relatórios
# Esse arquivo será responsável pelas funcionalidades que analisam os dados.
from collections import deque 
from datetime import datetime
from estruturas import historico, limpar_tela


# FUNÇÃO DE REGISTRO DE ENTRADA NO ESTOQUE
def entrada(med, quantidade=None) :
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y %H:%M") # SALVA O DIA E HORA DE ENTRADA
    
    entry_med = {
        "medicamento" : med["medicamento"],
        "id_medicamento" : med["id"],
        "categoria" : med["categoria"],
        "data" : data_formatada, # saída: dd/mm/2026 hr:min
        "tipo" : "ENTRADA",
        "quantidade" : quantidade # unidades recebidas (None se não informado)
    }
    
    historico.append(entry_med) # ENTRADA NO TOPO DA PILHA
    if quantidade is None:
        return print(f"O {med["medicamento"]} foi adicionado ao sistema !")
    return print(f"Entrada de {quantidade} unidade(s) de {med["medicamento"]} registrada !")

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
    limpar_tela()
    for i in historico :
        print(f"==================== {i['medicamento'].upper()} ({i['tipo']}) =======================\n")
        print(f"ID : {i['id_medicamento']}")
        if i.get("quantidade") is not None:
            print(f"Quantidade : {i['quantidade']}")
        print(f"Data : {i['data']} ") 
        print(f"Categoria : {i['categoria']} \n")