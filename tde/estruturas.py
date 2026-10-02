# AQUI VAI FICAR AS ESTRUTURAS DE PILHA, LISTA E FILA
#  ex de estruturas que ficarão aqui : 
# medicamentos = []
# historico = []
# fila_reposicao = []
from collections import deque 
import os
medicamentos = []  # medicamentos.py
historico = []  # relatorios.py
fila_reposicao = deque()  # reposicao.py
solicitacoes_reposicao = deque()  # reposicao.py
fornecedores = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
