# AQUI VAI FICAR AS ESTRUTURAS DE PILHA, LISTA E FILA
#  ex de estruturas que ficarão aqui : 
# medicamentos = []
# historico = []
# fila_reposicao = []
from collections import deque 

medicamentos = [] # medicamentos.py
historico = deque() # relatórios.py
fila_reposicao = deque() # reposição.py - armazenará os IDs das solicitações pendentes
solicitacoes_reposicao = deque() # reposição.py - representa o cadastro da entidade