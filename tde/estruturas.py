# AQUI VAI FICAR AS ESTRUTURAS DE PILHA, LISTA E FILA
from collections import deque
lista = []
while True:

 print ("\n::::\nSistema de Estoque de Medicamentos\n::::\n")
 print ("1 - Adicionar medicamento")
 print ("2 - Quantos medicamentos ja estão em estoque?")
 print ("3 - Sair do Programa")

 opcao = input("Escolha uma opção:")
 if opcao == "1":
    medicamento = {
        "nome": input ("Qual nome:"),
        "categoria": input ("Qual a categoria:"),
        "estoque": int(input ("estoque:")),
        "preco": float (input ("Qual o preço:"))
    }
    lista.append(medicamento)

 elif opcao == "2":
    print ("\nJa temos:",len(lista), "em estoque")

 elif opcao == "3":
    print ("\nPrograma encerrado")
    break
 else:
    print ("\nEscolha uma opção válida")