#  Arquivo principal que orquestrará o sistema
# Ele será responsável por:
#     mostrar o menu principal;
#     receber as escolhas do usuário;
#     chamar as funções dos outros arquivos;
#     controlar o fluxo geral do programa.


# IMPORTS
from medicamentos import cadastrar_medicamento, listar_medicamentos

cadastrar_medicamento("Paracetamol")
cadastrar_medicamento("Dipirona")

listar_medicamentos()