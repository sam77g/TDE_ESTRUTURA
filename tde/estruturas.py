# AQUI VAI FICAR AS ESTRUTURAS DE PILHA, LISTA E FILA
from collections import deque

fila = deque()
while True:
   
 print ("\n::::\nSistema de Estoque de Medicamentos\n::::\n")
 print ("1 - Adicionar medicamento")
 print ("2 - Quantos medicamentos ja estão em estoque?")
 print ("3 - Sair do Programa")

 opcao = input("Escolha uma opção:")
 if opcao == "1":
    medicamento = input ("Qual nome:")
    categoria = input ("Qual a categoria:")
    estoque = int(input ("estoque:"))
    preco = float (input ("Qual o preço:"))

 elif opcao == "2":
    print ("\nJa tem esses medicamentos no estoque:",medicamento)
 
 elif opcao == "3":
    print ("Programa encerrado")
    break
 else: 
    print ("Escolha uma opção válida")
