# consultas e relatórios
# Esse arquivo será responsável pelas funcionalidades que analisam os dados.
from collections import deque 
from estruturas import historico

def entrada(med) :
    historico.append(med)
    return print(f"O {med["nome"]} foi adicionado ao sistema !")

def retirada(med) :
    historico.pop()
    return print(f"O {med["nome"].upper()} foi retirado ")

