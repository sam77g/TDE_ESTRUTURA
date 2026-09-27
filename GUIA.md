# GUIA DE ESTUDOS E DESENVOLVIMENTO

## PharmaERP — Sistema de Gestão para Farmácia

**Tecnologia:** Python
**Tipo de aplicação:** Sistema de terminal/console
**Nível esperado:** Iniciante em Python
**Objetivo:** Desenvolver o TDE — Aplicação de Estruturas Lineares e Algoritmos

---

# 1. Objetivo deste documento

Este documento serve como guia para todos os integrantes do grupo durante o desenvolvimento do PharmaERP.

O objetivo não é apenas dizer "o que programar", mas explicar:

* quais conceitos de Python precisamos conhecer;
* como organizar o projeto;
* o que são módulos;
* como funciona `import`;
* como um arquivo Python conversa com outro;
* como utilizar listas;
* como representar uma pilha;
* como representar uma fila;
* como utilizar dicionários para representar os dados;
* como implementar CRUD;
* como realizar buscas;
* como implementar ordenação;
* como integrar tudo no sistema;
* quais conteúdos devemos estudar antes de implementar cada parte.

A ideia é que **todos os integrantes entendam o código**, mesmo que cada pessoa seja responsável por uma parte específica.

---

# 2. O que estamos construindo?

O projeto será um pequeno ERP para uma farmácia.

O sistema será executado pelo terminal e permitirá controlar informações como:

* medicamentos;
* fornecedores;
* estoque;
* movimentações;
* solicitações de reposição;
* histórico de operações;
* relatórios.

Não estamos tentando criar um ERP comercial completo.

O objetivo é desenvolver um sistema suficientemente funcional para demonstrar os conceitos exigidos pelo TDE.

---

# 3. Escopo do projeto

## 3.1. O que estará no projeto

O PharmaERP terá:

### Medicamentos

* cadastro;
* consulta;
* alteração;
* remoção;
* busca;
* controle de estoque;
* estoque mínimo.

### Fornecedores

* cadastro;
* consulta;
* alteração;
* remoção;
* busca.

### Estoque

* entrada de medicamentos;
* saída de medicamentos;
* verificação de quantidade disponível;
* identificação de estoque baixo.

### Pilha

Será utilizada para armazenar o histórico das movimentações.

Exemplo:

```text
Entrada de Paracetamol
Saída de Dipirona
Entrada de Ibuprofeno
```

A última movimentação será a primeira a ser retirada do histórico.

Isso representa:

```text
LIFO
Last In, First Out
```

### Fila

Será utilizada para solicitações de reposição.

Exemplo:

```text
1. Reposição de Paracetamol
2. Reposição de Dipirona
3. Reposição de Ibuprofeno
```

A primeira solicitação será atendida primeiro.

Isso representa:

```text
FIFO
First In, First Out
```

### Relatórios

O sistema poderá apresentar:

* lista de medicamentos;
* medicamentos com estoque baixo;
* fornecedores;
* histórico de movimentações;
* fila de reposição;
* resultados de buscas;
* dados ordenados.

---

# 4. O que NÃO faz parte do projeto

Para evitar que o grupo complique desnecessariamente o trabalho, não vamos implementar:

* banco de dados;
* interface gráfica;
* site;
* API;
* login;
* sistema de usuários;
* autenticação;
* integração com fornecedores reais;
* pagamentos;
* emissão de nota fiscal;
* frameworks;
* bibliotecas externas desnecessárias;
* `heapq`;
* `deque`;
* arquitetura complexa;
* POO avançada.

Também não precisamos criar classes como:

```python
class Medicamento:
```

ou:

```python
class Fila:
```

Neste momento, podemos resolver o problema utilizando:

* listas;
* dicionários;
* funções;
* condicionais;
* loops;
* módulos;
* imports.

Isso é suficiente para o escopo definido.

---

# 5. O conhecimento de Python necessário

Antes de desenvolver o sistema, todos devem conhecer pelo menos:

```text
1. Variáveis
2. Tipos de dados
3. if / elif / else
4. for
5. while
6. funções
7. parâmetros
8. return
9. listas
10. dicionários
11. append()
12. pop()
13. len()
14. busca em listas
15. módulos
16. import
17. from ... import ...
18. validações
19. tratamento básico de erros
```

Além disso, precisamos compreender os conceitos de:

```text
Lista
Pilha
Fila
LIFO
FIFO
Busca linear
Ordenação
Complexidade
CRUD
```

---

# 6. O conceito mais importante: módulos

Em Python, cada arquivo `.py` pode funcionar como um **módulo**.

Por exemplo:

```text
medicamentos.py
```

pode conter funções relacionadas aos medicamentos.

Outro arquivo:

```text
fornecedores.py
```

pode conter funções relacionadas aos fornecedores.

E:

```text
main.py
```

pode controlar o sistema inteiro.

Podemos pensar em cada arquivo como uma "caixa" responsável por uma parte do programa.

---

# 7. Como isso se compara ao JavaScript?

Como alguns integrantes já conhecem JavaScript, podemos fazer uma comparação.

No JavaScript:

```javascript
// medicamentos.js

export function cadastrarMedicamento() {
    // ...
}
```

E:

```javascript
// main.js

import { cadastrarMedicamento } from "./medicamentos.js";
```

Em Python:

```python
# medicamentos.py

def cadastrar_medicamento():
    # ...
```

E:

```python
# main.py

from medicamentos import cadastrar_medicamento
```

A ideia é praticamente a mesma:

```text
JavaScript:

arquivo A
   ↓
export
   ↓
import
   ↓
arquivo B
```

Python:

```text
arquivo A
   ↓
função/variável definida
   ↓
import
   ↓
arquivo B
```

---

# 8. O que é import?

`import` serve para utilizar código que está em outro módulo.

Exemplo:

```python
import medicamentos
```

Depois:

```python
medicamentos.cadastrar_medicamento()
```

Outra forma:

```python
from medicamentos import cadastrar_medicamento
```

Depois:

```python
cadastrar_medicamento()
```

---

# 9. Diferença entre import e from

## Forma 1

```python
import medicamentos
```

Uso:

```python
medicamentos.cadastrar_medicamento()
medicamentos.listar_medicamentos()
```

Essa forma deixa explícito de qual módulo veio a função.

---

## Forma 2

```python
from medicamentos import cadastrar_medicamento
```

Uso:

```python
cadastrar_medicamento()
```

É mais curto.

---

## Forma 3

Também podemos importar várias funções:

```python
from medicamentos import (
    cadastrar_medicamento,
    listar_medicamentos,
    remover_medicamento
)
```

---

# 10. Existe export em Python?

Normalmente não.

Em Python, uma função como:

```python
def cadastrar_medicamento():
    pass
```

já pode ser importada por outro arquivo.

Não precisamos escrever:

```python
export
```

como fazemos em JavaScript.

---

# 11. Estrutura de arquivos do projeto

O projeto será organizado assim:

```text
pharma_erp/
│
├── main.py
│
├── estruturas.py
│
├── medicamentos.py
│
├── fornecedores.py
│
├── estoque.py
│
├── reposicao.py
│
└── relatorios.py
```

---

# 12. Responsabilidade de cada arquivo

## `main.py`

É o ponto de entrada do sistema.

Será executado com:

```bash
python main.py
```

Responsabilidades:

* apresentar o menu;
* receber a escolha do usuário;
* chamar as funções dos outros módulos;
* controlar o fluxo geral.

Exemplo:

```python
from medicamentos import cadastrar_medicamento

cadastrar_medicamento()
```

O `main.py` não deve conter toda a lógica do sistema.

Ele funciona como o "coordenador".

---

# 13. `estruturas.py`

Esse módulo armazenará as estruturas compartilhadas pelo sistema.

Inicialmente:

```python
medicamentos = []
fornecedores = []
historico = []
fila_reposicao = []
```

Essas listas representarão os dados enquanto o programa estiver executando.

Exemplo:

```text
medicamentos
    ↓
[ medicamento 1, medicamento 2, medicamento 3 ]

fornecedores
    ↓
[ fornecedor 1, fornecedor 2 ]

historico
    ↓
[ movimentação 1, movimentação 2 ]

fila_reposicao
    ↓
[ solicitação 1, solicitação 2 ]
```

---

# 14. `medicamentos.py`

Responsável por tudo relacionado aos medicamentos.

Funções previstas:

```python
cadastrar_medicamento()
listar_medicamentos()
buscar_medicamento()
alterar_medicamento()
remover_medicamento()
```

Também poderá conter validações específicas.

Exemplo de medicamento:

```python
{
    "id": 1,
    "nome": "Paracetamol",
    "categoria": "Analgésico",
    "estoque": 20,
    "estoque_minimo": 10,
    "preco": 8.50
}
```

---

# 15. `fornecedores.py`

Responsável pelo CRUD dos fornecedores.

Funções previstas:

```python
cadastrar_fornecedor()
listar_fornecedores()
buscar_fornecedor()
alterar_fornecedor()
remover_fornecedor()
```

Exemplo:

```python
{
    "id": 1,
    "nome": "Distribuidora Saúde",
    "cnpj": "00.000.000/0001-00",
    "telefone": "75999999999"
}
```

---

# 16. `estoque.py`

Responsável pelas movimentações do estoque.

Funções previstas:

```python
entrada_estoque()
saida_estoque()
consultar_estoque()
desfazer_ultima_movimentacao()
```

Exemplo:

```text
Paracetamol
Estoque atual: 20

Entrada de 10

Estoque:
20 + 10 = 30
```

Saída:

```text
30 - 5 = 25
```

Também deverá registrar a movimentação no histórico.

---

# 17. `reposicao.py`

Responsável pela fila de reposição.

Funções previstas:

```python
verificar_estoque_baixo()
criar_solicitacao()
adicionar_fila()
atender_solicitacao()
listar_fila()
```

Exemplo:

```text
Paracetamol
Estoque: 5
Mínimo: 10
```

Como:

```text
5 < 10
```

o sistema pode identificar que é necessário fazer uma reposição.

A solicitação entra na fila:

```python
fila_reposicao.append(solicitacao)
```

---

# 18. `relatorios.py`

Responsável por consultas e relatórios.

Exemplos:

```python
listar_medicamentos()
filtrar_estoque_baixo()
mostrar_historico()
mostrar_fila()
ordenar_medicamentos()
```

Também será um dos locais onde poderemos demonstrar algoritmos de busca e ordenação.

---

# 19. Como os módulos se comunicam?

A ideia geral será:

```text
                         main.py
                            │
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
      medicamentos    fornecedores      estoque
             │              │              │
             └──────────────┼──────────────┘
                            ↓
                      estruturas.py
                            ↑
                  ┌─────────┴─────────┐
                  │                   │
             reposicao.py       relatorios.py
```

O `main.py` coordena.

Os módulos executam responsabilidades específicas.

`estruturas.py` mantém as estruturas compartilhadas.

---

# 20. Exemplo simples de integração

## `estruturas.py`

```python
medicamentos = []
```

## `medicamentos.py`

```python
from estruturas import medicamentos


def cadastrar_medicamento(nome):
    medicamentos.append(nome)


def listar_medicamentos():
    print(medicamentos)
```

## `main.py`

```python
from medicamentos import cadastrar_medicamento, listar_medicamentos


cadastrar_medicamento("Paracetamol")
cadastrar_medicamento("Dipirona")

listar_medicamentos()
```

Resultado:

```text
['Paracetamol', 'Dipirona']
```

Esse exemplo representa a ideia básica de integração que será usada no projeto.

---

# 21. Listas em Python

Uma lista é uma estrutura que permite armazenar vários valores.

```python
medicamentos = []
```

Adicionar:

```python
medicamentos.append("Paracetamol")
```

Resultado:

```python
["Paracetamol"]
```

Adicionar outro:

```python
medicamentos.append("Dipirona")
```

Resultado:

```python
["Paracetamol", "Dipirona"]
```

Quantidade:

```python
len(medicamentos)
```

Acessar:

```python
medicamentos[0]
```

Remover:

```python
medicamentos.pop()
```

---

# 22. Lista no nosso projeto

Uma lista poderá armazenar vários dicionários:

```python
medicamentos = [
    {
        "id": 1,
        "nome": "Paracetamol",
        "estoque": 20
    },
    {
        "id": 2,
        "nome": "Dipirona",
        "estoque": 15
    }
]
```

Percorrendo:

```python
for medicamento in medicamentos:
    print(medicamento["nome"])
```

Resultado:

```text
Paracetamol
Dipirona
```

Esse conceito será fundamental para o CRUD.

---

# 23. Dicionários

Os registros do sistema serão representados por dicionários.

Exemplo:

```python
medicamento = {
    "id": 1,
    "nome": "Paracetamol",
    "estoque": 20
}
```

Podemos acessar:

```python
print(medicamento["nome"])
```

Resultado:

```text
Paracetamol
```

Alterar:

```python
medicamento["estoque"] = 30
```

---

# 24. Lista + dicionário

Essa combinação será a principal forma de armazenar nossas entidades.

```python
medicamentos = []

medicamento = {
    "id": 1,
    "nome": "Paracetamol",
    "estoque": 20
}

medicamentos.append(medicamento)
```

Temos:

```text
medicamentos
    │
    └── lista
          │
          └── dicionário
                ├── id
                ├── nome
                └── estoque
```

---

# 25. O que é uma pilha?

Uma pilha funciona no modelo:

```text
LIFO
Last In, First Out
```

O último elemento colocado é o primeiro a sair.

Exemplo:

```text
Entrada A
Entrada B
Entrada C
```

A retirada será:

```text
C
B
A
```

Uma situação cotidiana seria uma pilha de pratos.

O último prato colocado em cima é o primeiro que conseguimos retirar.

---

# 26. Implementando uma pilha com lista

No Python:

```python
historico = []
```

Adicionar:

```python
historico.append("Entrada de Paracetamol")
historico.append("Saída de Dipirona")
historico.append("Entrada de Ibuprofeno")
```

Temos:

```text
Entrada de Paracetamol
Saída de Dipirona
Entrada de Ibuprofeno
                      ↑
                    topo
```

Remover:

```python
historico.pop()
```

Sai:

```text
Entrada de Ibuprofeno
```

---

# 27. Por que usar pilha no PharmaERP?

Porque queremos manter um histórico reversível de movimentações.

Imagine:

```text
1. Entrada de Paracetamol
2. Saída de Dipirona
3. Entrada de Ibuprofeno
```

Se o usuário escolher "desfazer última movimentação", queremos desfazer:

```text
Entrada de Ibuprofeno
```

Ela foi a última movimentação realizada.

Portanto:

```text
Pilha
+
LIFO
=
boa representação para histórico reversível
```

---

# 28. O que é uma fila?

Uma fila funciona no modelo:

```text
FIFO
First In, First Out
```

O primeiro elemento que entra é o primeiro que sai.

Exemplo:

```text
João
Maria
Pedro
```

A ordem de atendimento será:

```text
João
Maria
Pedro
```

---

# 29. Implementando fila com lista

Criamos:

```python
fila = []
```

Adicionar:

```python
fila.append("Paracetamol")
fila.append("Dipirona")
fila.append("Ibuprofeno")
```

Temos:

```text
Paracetamol
Dipirona
Ibuprofeno
    ↑
 primeiro
```

Para retirar:

```python
fila.pop(0)
```

Sai:

```text
Paracetamol
```

Restam:

```text
Dipirona
Ibuprofeno
```

---

# 30. Por que usar fila no PharmaERP?

As solicitações de reposição podem seguir uma ordem de chegada.

Exemplo:

```text
1. Reposição de Paracetamol
2. Reposição de Dipirona
3. Reposição de Ibuprofeno
```

A primeira solicitação cadastrada será atendida primeiro.

Portanto:

```text
Fila
+
FIFO
=
ordem de atendimento das reposições
```

---

# 31. Não confundir lista, pilha e fila

Embora todas possam utilizar `list` em Python, o comportamento é diferente.

| Estrutura | Regra                    | Exemplo      |
| --------- | ------------------------ | ------------ |
| Lista     | acesso/manipulação geral | medicamentos |
| Pilha     | LIFO                     | histórico    |
| Fila      | FIFO                     | reposição    |

O professor pode perguntar:

> "Mas vocês utilizaram `list` para tudo?"

A resposta correta é:

> "Sim. A lista do Python é a estrutura de armazenamento que utilizamos para implementar os comportamentos necessários. O que diferencia cada estrutura é a forma como permitimos as operações sobre ela."

---

# 32. CRUD

CRUD significa:

```text
C → Create
R → Read
U → Update
D → Delete
```

Em português:

```text
Create → Cadastrar
Read   → Consultar
Update → Alterar
Delete → Remover
```

No nosso projeto teremos CRUD de pelo menos duas entidades.

Principalmente:

```text
Medicamentos
Fornecedores
```

---

# 33. Busca linear

Precisaremos localizar medicamentos e fornecedores.

Podemos fazer uma busca percorrendo a lista:

```python
for medicamento in medicamentos:
    if medicamento["id"] == id_medicamento:
        return medicamento
```

Isso é uma **busca linear**.

No pior caso precisamos verificar todos os elementos.

Complexidade:

```text
O(n)
```

Melhor caso:

```text
O(1)
```

se o primeiro elemento for o procurado.

---

# 34. Ordenação

Também precisamos compreender algoritmos de ordenação.

Uma opção adequada para o TDE é o:

```text
Bubble Sort
```

A ideia é comparar elementos vizinhos e trocar quando estiverem fora de ordem.

Exemplo:

```text
[30, 10, 20]
```

Comparamos:

```text
30 > 10
```

Troca:

```text
[10, 30, 20]
```

Depois:

```text
30 > 20
```

Troca:

```text
[10, 20, 30]
```

No pior caso:

```text
O(n²)
```

Isso também será útil para a parte de análise de complexidade exigida no trabalho.

---

# 35. Complexidade que devemos conhecer

Não precisamos estudar toda a teoria de complexidade.

Precisamos saber explicar pelo menos:

```text
O(1)
O(n)
O(n²)
```

### O(1)

Tempo aproximadamente constante.

Exemplo:

```python
historico.pop()
```

A operação trabalha com o topo da pilha.

---

### O(n)

Pode precisar percorrer todos os elementos.

Exemplo:

```python
for medicamento in medicamentos:
    ...
```

Busca linear.

---

### O(n²)

Normalmente aparece quando temos dois loops dependentes.

Exemplo:

```python
for i in range(n):
    for j in range(n):
        ...
```

Bubble Sort no pior caso.

---

# 36. Atenção ao `pop(0)`

Nossa fila inicialmente será:

```python
fila.pop(0)
```

Essa operação tem custo:

```text
O(n)
```

porque, ao remover o primeiro elemento, os demais precisam ser deslocados.

Para o nosso trabalho isso é aceitável porque estamos implementando uma fila simples utilizando `list`, de forma didática.

Não vamos substituir por `collections.deque` neste momento porque o objetivo é justamente compreender e implementar a estrutura básica.

---

# 37. Ordem de estudo recomendada

Não tentem aprender tudo ao mesmo tempo.

A sequência recomendada é:

```text
ETAPA 1
Python básico
    ↓
ETAPA 2
Funções
    ↓
ETAPA 3
Listas
    ↓
ETAPA 4
Dicionários
    ↓
ETAPA 5
Módulos e import
    ↓
ETAPA 6
CRUD
    ↓
ETAPA 7
Pilha
    ↓
ETAPA 8
Fila
    ↓
ETAPA 9
Busca
    ↓
ETAPA 10
Ordenação
    ↓
ETAPA 11
Integração
    ↓
ETAPA 12
Testes
```

---

# 38. Roteiro de estudos no YouTube

## 38.1. Módulos e import

### Curso em Vídeo — Curso Python #08: Utilizando Módulos

Conteúdo:

* módulos;
* `import`;
* `from`;
* utilização de código de outros arquivos.

É especialmente importante para este projeto porque é exatamente o conceito que será utilizado para integrar `main.py`, `medicamentos.py`, `estoque.py` etc.

[Assistir no YouTube](https://www.youtube.com/watch?v=oOUyhGNib2Q)

O vídeo é do Curso em Vídeo, com Gustavo Guanabara, e aborda especificamente `import` e `from/import`.

---

# 39. Listas

### Curso em Vídeo — Curso Python #17: Listas (Parte 1)

Estudar:

* criação de listas;
* índices;
* armazenamento de vários valores;
* manipulação de listas.

[Assistir no YouTube](https://www.youtube.com/watch?v=N1hTsbW50eM)

A aula é especificamente sobre listas em Python.

Também é recomendável continuar as aulas seguintes do Curso de Python relacionadas a listas.

---

# 40. Funções

### Curso em Vídeo — Curso Python #20: Funções (Parte 1)

Estudar:

* `def`;
* criação de funções;
* parâmetros;
* organização do código;
* reutilização de funções.

[Assistir no YouTube](https://www.youtube.com/watch?v=ezfr9d7wd_k)

Essa aula aborda justamente funções e parâmetros em Python.

Esse conteúdo é fundamental porque praticamente todos os módulos do nosso sistema serão compostos por funções.

---

# 41. Lista × Pilha × Fila

### Bóson Treinamentos — Listas, Pilhas e Filas em Estruturas de Dados

Esse vídeo é particularmente útil para compreender a **diferença conceitual** entre:

* lista;
* pilha;
* fila;
* LIFO;
* FIFO;
* operações dessas estruturas.

[Assistir no YouTube](https://www.youtube.com/watch?v=OwiHoj-mAi8)

O vídeo explica justamente as diferenças entre essas estruturas lineares e apresenta LIFO e FIFO.

---

# 42. Estruturas de Dados com Python

Também podemos utilizar:

### Estruturas de Dados com Python — Lista, Pilha (LIFO), Fila (FIFO) e Árvore Binária

[Assistir no YouTube](https://www.youtube.com/watch?v=bpt21iwiq_g)

O vídeo aborda estruturas de dados em Python, incluindo lista, pilha e fila. A parte de árvore não é necessária para o nosso TDE; podemos ignorá-la.

---

# 43. Bubble Sort

Para a parte de ordenação, podemos estudar o conceito de Bubble Sort e depois implementar nós mesmos.

Um exemplo encontrado em português:

[Bubble Sort usando Python em Português](https://www.youtube.com/watch?v=HJUVKtaihdc)

O foco deve ser entender o algoritmo, e não simplesmente copiar o código.

---

# 44. O que estudar no Curso em Vídeo antes de programar

Se vocês estiverem muito enferrujados em Python, não precisam assistir um curso inteiro novamente.

Priorizar:

```text
✓ Variáveis
✓ Tipos de dados
✓ Condicionais
✓ Repetições
✓ Listas
✓ Dicionários
✓ Funções
✓ Módulos
```

Depois disso, começar diretamente os exercícios do projeto.

---

# 45. Exercícios obrigatórios antes do projeto

Cada integrante deve conseguir fazer estes exercícios sozinho.

## Exercício 1 — Lista

Criar:

```python
medicamentos = []
```

Adicionar:

```text
Paracetamol
Dipirona
Ibuprofeno
```

Depois:

* imprimir;
* contar;
* remover;
* procurar um medicamento.

---

## Exercício 2 — Dicionário

Criar:

```python
medicamento = {
    "id": 1,
    "nome": "Paracetamol",
    "estoque": 20
}
```

Depois:

* imprimir o nome;
* alterar estoque;
* adicionar uma nova informação;
* remover uma informação.

---

## Exercício 3 — Lista de dicionários

Criar:

```python
medicamentos = []
```

Adicionar três medicamentos como dicionários.

Depois:

* listar todos;
* buscar pelo ID;
* alterar um medicamento;
* remover um medicamento.

Esse exercício praticamente introduz o CRUD.

---

## Exercício 4 — Pilha

Criar:

```python
historico = []
```

Adicionar três operações.

Depois:

```python
historico.pop()
```

E explicar por que o último elemento saiu primeiro.

---

## Exercício 5 — Fila

Criar:

```python
fila = []
```

Adicionar três solicitações.

Depois:

```python
fila.pop(0)
```

E explicar por que o primeiro elemento saiu primeiro.

---

## Exercício 6 — Import

Criar:

```text
teste/
├── main.py
└── funcoes.py
```

No `funcoes.py`:

```python
def saudacao():
    print("Olá!")
```

No `main.py`:

```python
from funcoes import saudacao

saudacao()
```

Todos devem entender o que aconteceu.

---

# 46. Como dividir os estudos entre as pessoas

## Pessoa 1

Foco inicial:

```text
Listas
Dicionários
CRUD
Medicamentos
```

---

## Pessoa 2

Foco inicial:

```text
Funções
Módulos
Import
Fornecedores
```

---

## Pessoa 3

Foco inicial:

```text
Pilha
LIFO
Histórico
Estoque
```

---

## Pessoa 4

Foco inicial:

```text
Fila
FIFO
Reposição
Relatórios
```

---

# 47. Mas todos precisam aprender tudo

A divisão de tarefas serve para organizar o desenvolvimento.

Não significa:

```text
Pessoa 1 sabe medicamentos.
Pessoa 2 sabe fornecedores.
Pessoa 3 sabe pilha.
Pessoa 4 sabe fila.
```

E ninguém mais sabe nada.

Isso seria perigoso para a apresentação.

Todos devem saber explicar:

```text
✓ Lista
✓ Pilha
✓ Fila
✓ LIFO
✓ FIFO
✓ CRUD
✓ Busca linear
✓ Complexidade
✓ import
✓ módulos
✓ funcionamento geral do sistema
```

A divisão significa apenas:

> "Essa pessoa será a principal responsável por implementar e testar essa parte."

---

# 48. Fluxo de desenvolvimento

O desenvolvimento seguirá aproximadamente esta ordem:

```text
1. Estudar Python necessário
        ↓
2. Testar listas
        ↓
3. Testar dicionários
        ↓
4. Testar funções
        ↓
5. Testar import
        ↓
6. Criar estrutura de arquivos
        ↓
7. Criar CRUD de medicamentos
        ↓
8. Criar CRUD de fornecedores
        ↓
9. Implementar estoque
        ↓
10. Implementar pilha/histórico
        ↓
11. Implementar fila/reposição
        ↓
12. Criar relatórios
        ↓
13. Implementar busca
        ↓
14. Implementar ordenação
        ↓
15. Integrar tudo
        ↓
16. Testar
        ↓
17. Documentar
        ↓
18. Preparar apresentação
```

---

# 49. Regra importante durante o desenvolvimento

Não façam:

```text
Copiar código do YouTube
↓
colar no projeto
↓
"funcionou"
↓
seguir para a próxima parte
```

O objetivo do trabalho é justamente conseguir explicar as estruturas e os algoritmos.

Sempre que encontrarem um código, perguntem:

```text
O que essa linha faz?

Por que essa função existe?

Qual estrutura está sendo utilizada?

Por que utilizamos essa estrutura?

Qual é a complexidade?

O que acontece se o dado não existir?

O que acontece se o usuário digitar algo inválido?
```

---

# 50. Regra para usar IA

A IA pode ser utilizada como ferramenta de apoio, mas o grupo precisa compreender o código entregue.

Se a IA gerar:

```python
def buscar_medicamento(id):
    ...
```

não basta copiar.

O integrante responsável deve conseguir explicar:

```text
1. O que a função recebe?
2. O que ela procura?
3. Onde ela procura?
4. Como percorre a lista?
5. O que acontece se encontrar?
6. O que acontece se não encontrar?
7. Qual a complexidade?
```

Isso também evita que o grupo tenha dificuldades caso o professor peça para modificar uma parte do código durante a apresentação.

---

# 51. Fluxo final esperado do sistema

Um exemplo de utilização do PharmaERP será:

```text
INICIAR
   ↓
MENU PRINCIPAL
   ↓
Cadastrar medicamento
   ↓
Cadastrar fornecedor
   ↓
Consultar medicamento
   ↓
Alterar medicamento
   ↓
Registrar entrada
   ↓
Registrar saída
   ↓
Registrar movimentação no histórico
   ↓
Mostrar histórico
   ↓
Desfazer última movimentação
   ↓
Verificar estoque mínimo
   ↓
Criar solicitação de reposição
   ↓
Adicionar à fila
   ↓
Atender primeira solicitação
   ↓
Gerar relatório
   ↓
Pesquisar
   ↓
Ordenar
   ↓
FINALIZAR
```

---

# 52. Estrutura final resumida

```text
pharma_erp/
│
├── main.py
│   └── controla o sistema
│
├── estruturas.py
│   └── listas compartilhadas
│
├── medicamentos.py
│   └── CRUD de medicamentos
│
├── fornecedores.py
│   └── CRUD de fornecedores
│
├── estoque.py
│   └── entradas, saídas e histórico
│
├── reposicao.py
│   └── fila de reposição
│
└── relatorios.py
    └── consultas, filtros e ordenação
```

---

# 53. Checklist de conhecimento

Antes da entrega, cada integrante deve conseguir marcar:

### Python

* [ ] Sei criar variáveis.
* [ ] Sei utilizar `if`.
* [ ] Sei utilizar `for`.
* [ ] Sei utilizar `while`.
* [ ] Sei criar funções.
* [ ] Sei passar parâmetros.
* [ ] Sei usar `return`.
* [ ] Sei trabalhar com listas.
* [ ] Sei trabalhar com dicionários.
* [ ] Sei usar `append()`.
* [ ] Sei usar `pop()`.
* [ ] Sei usar `len()`.

### Módulos

* [ ] Sei o que é um módulo.
* [ ] Sei criar um arquivo `.py` para funcionar como módulo.
* [ ] Sei utilizar `import`.
* [ ] Sei utilizar `from ... import ...`.
* [ ] Sei chamar uma função de outro arquivo.

### Estruturas

* [ ] Sei explicar lista.
* [ ] Sei explicar pilha.
* [ ] Sei explicar fila.
* [ ] Sei explicar LIFO.
* [ ] Sei explicar FIFO.
* [ ] Sei implementar uma pilha com `append()` e `pop()`.
* [ ] Sei implementar uma fila com `append()` e `pop(0)`.

### Algoritmos

* [ ] Sei fazer busca linear.
* [ ] Sei explicar O(1).
* [ ] Sei explicar O(n).
* [ ] Sei explicar O(n²).
* [ ] Sei explicar o funcionamento básico do Bubble Sort.

### Projeto

* [ ] Sei explicar o papel de cada arquivo.
* [ ] Sei explicar o CRUD.
* [ ] Sei explicar como o estoque funciona.
* [ ] Sei explicar o histórico.
* [ ] Sei explicar a fila de reposição.
* [ ] Sei explicar como os módulos são integrados.
* [ ] Consigo executar o projeto sozinho.
* [ ] Consigo modificar uma função sem depender de copiar código.

---

# 54. Ordem de estudo recomendada para esta semana

Se o prazo estiver próximo, não tentem estudar Python inteiro.

Façam:

### Dia 1

```text
Funções
Listas
Dicionários
```

### Dia 2

```text
Módulos
import
from ... import
Integração entre arquivos
```

### Dia 3

```text
Lista
Pilha
Fila
LIFO
FIFO
```

### Dia 4

```text
CRUD
Busca linear
Validações
```

### Dia 5

```text
Ordenação
Bubble Sort
Complexidade
```

### Depois

```text
Implementação
Integração
Testes
Documentação
Apresentação
```

---

# 55. O que realmente precisamos dominar

O objetivo não é sair deste trabalho sabendo Python profissionalmente.

O objetivo é terminar o projeto sabendo explicar:

```text
"Eu tenho vários arquivos Python."

        ↓

"Cada arquivo possui uma responsabilidade."

        ↓

"Eu consigo importar funções de um módulo para outro."

        ↓

"Utilizo listas para armazenar os dados."

        ↓

"Utilizo dicionários para representar os registros."

        ↓

"Utilizo uma pilha para o histórico porque preciso de LIFO."

        ↓

"Utilizo uma fila para reposições porque preciso de FIFO."

        ↓

"Utilizo busca linear para encontrar registros."

        ↓

"Utilizo um algoritmo de ordenação para gerar relatórios."

        ↓

"E consigo explicar a complexidade das operações."
```

Esse é o conhecimento central que o grupo precisa ter para construir e defender o PharmaERP.
