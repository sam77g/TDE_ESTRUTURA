# AQUI VAI FICAR AS ESTRUTURAS DE PILHA, LISTA E FILA
#  ex de estruturas que ficarão aqui : 
# medicamentos = []
# historico = []
# fila_reposicao = []
from collections import deque 
import os
medicamentos = []  # medicamentos.py
historico = []  # relatorios.py
solicitacoes_reposicao = deque()  # reposicao.py

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# FUNÇÃO DE DEBUG 
def DEBUG() :
    print("-- PILHA DO HISTÓRICO -- \n")
    print(historico,"\n")
    print("-- REPOSIÇAO -- \n")
    print(solicitacoes_reposicao,"\n")
    print("-- MEDICAMENTOS -- \n")
    print(medicamentos,"\n")