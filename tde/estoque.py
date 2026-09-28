# movimentação do estoque - PILHA
# Esse arquivo será responsável por:
# entrada de medicamentos;
# saída de medicamentos;
# verificar estoque disponível;
# atualizar quantidade;
# registrar movimentações no histórico;
# desfazer a última movimentação.

from collections import deque 
proximo_id = 1
def gerar_id():
    global proximo_id

    id_atual = proximo_id
    proximo_id += 1

    return id_atual