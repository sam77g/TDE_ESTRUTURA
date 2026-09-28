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

# def alterar_medicamento() :

def remover_medicamento(nome) :  
    for medicamento in medicamentos:
        if medicamento["nome"].lower() == nome.lower():
            medicamentos.pop(medicamento)
            return print(f"{nome} removido ! ")
    
    return None   