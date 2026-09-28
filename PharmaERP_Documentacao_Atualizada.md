# PharmaERP --- Sistema de Gestão de Farmácia

## TDE --- Aplicação de Estruturas Lineares e Algoritmos

------------------------------------------------------------------------

# 1. Visão geral do projeto

O projeto consiste no desenvolvimento de um pequeno sistema de **ERP
para uma farmácia**, utilizando Python para representar e automatizar
alguns processos básicos de gestão.

O foco principal do trabalho não é criar um sistema comercial completo,
mas demonstrar a aplicação prática de **estruturas de dados lineares e
algoritmos** em um problema real.

O sistema deverá permitir o gerenciamento de:

-   medicamentos;
-   movimentações de estoque;
-   solicitações de reposição;
-   relatórios.

As principais estruturas de dados utilizadas serão:

-   **Lista** → cadastro e gerenciamento de medicamentos e solicitações
    de reposição;
-   **Pilha** → histórico de movimentações de estoque;
-   **Fila** → solicitações de reposição de medicamentos.

O professor informou que não é obrigatório utilizar uma implementação
avançada de fila de prioridade. Portanto, inicialmente será utilizada
uma **fila simples, baseada no princípio FIFO**, mantendo o projeto
dentro do conteúdo básico da disciplina.

------------------------------------------------------------------------

# 2. Objetivo do projeto

O objetivo é desenvolver um sistema funcional que permita demonstrar:

1.  utilização de listas;
2.  utilização de pilhas;
3.  utilização de filas;
4.  operações de CRUD sobre duas entidades;
5.  validação de dados;
6.  busca de informações;
7.  ordenação de dados;
8.  geração de relatórios;
9.  análise de complexidade;
10. justificativa das escolhas de estruturas.

Além de funcionar, o sistema deverá ser compreensível por todos os
integrantes, pois haverá possibilidade de **arguição individual durante
a apresentação**.

Portanto, não devemos implementar funcionalidades que nenhum integrante
consiga explicar.

------------------------------------------------------------------------

# 3. Escopo do projeto

## 3.1. O que estará dentro do escopo

O sistema terá:

### Medicamentos

-   cadastro;
-   consulta;
-   alteração;
-   remoção;
-   listagem;
-   busca;
-   filtro;
-   controle de estoque.

### Estoque

-   entrada de medicamentos;
-   saída de medicamentos;
-   histórico de movimentações;
-   possibilidade de desfazer a última movimentação.

### Reposição

-   identificação de medicamentos abaixo do estoque mínimo;
-   cadastro de solicitações de reposição;
-   consulta de solicitações;
-   alteração de solicitações;
-   remoção de solicitações;
-   listagem de solicitações;
-   armazenamento dos IDs das solicitações pendentes em uma fila;
-   atendimento das solicitações pela ordem de chegada.

### Relatórios

-   listagem de medicamentos;
-   filtro por categoria;
-   medicamentos abaixo do estoque mínimo;
-   histórico de movimentações;
-   fila de reposição;
-   ordenação dos medicamentos.

------------------------------------------------------------------------

# 4. O que NÃO faz parte do escopo

Para evitar aumentar desnecessariamente a complexidade, o projeto não
terá inicialmente:

-   banco de dados;
-   sistema de login;
-   autenticação;
-   interface gráfica;
-   site;
-   API;
-   conexão com internet;
-   sistema financeiro completo;
-   emissão de nota fiscal;
-   POO avançada;
-   frameworks;
-   bibliotecas externas;
-   `heapq`;
-   estruturas avançadas que não foram ensinadas.

O sistema será executado no **terminal/console utilizando Python**.

A prioridade é demonstrar corretamente as estruturas de dados e os
algoritmos solicitados no TDE.

------------------------------------------------------------------------

# 5. Estrutura geral do sistema

O sistema será organizado conceitualmente da seguinte forma:

``` text
                         PHARMA ERP
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
       MEDICAMENTOS      ESTOQUE            REPOSIÇÃO
          │                  │                  │
          ▼                  ▼                  ▼
        LISTA              PILHA              FILA
          │                  │                  │
          ▼                  ▼                  ▼
       Cadastro         Histórico          Solicitações
       Consulta         Desfazer           Atendimento
       Alteração
       Remoção
```

------------------------------------------------------------------------

# 6. Estruturas de dados

## 6.1. Lista

A lista será utilizada para armazenar os cadastros.

Exemplo:

``` python
medicamentos = []
```

Cada medicamento poderá ser representado por um dicionário:

``` python
medicamento = {
    "id": 1,
    "nome": "Paracetamol",
    "categoria": "Analgésico",
    "estoque": 20,
    "estoque_minimo": 10,
    "preco": 8.50
}
```

A lista poderá conter vários medicamentos:

``` text
medicamentos

[0] Paracetamol
[1] Dipirona
[2] Ibuprofeno
[3] Amoxicilina
```

### Por que utilizar lista?

Porque o cadastro exige:

-   inserção;
-   consulta;
-   alteração;
-   remoção;
-   travessia dos registros.

A lista é adequada para representar uma coleção linear de registros.

------------------------------------------------------------------------

# 7. Pilha

A pilha será utilizada no histórico de movimentações.

Exemplo:

``` python
historico = []
```

Cada movimentação será adicionada ao final:

``` python
historico.append(movimentacao)
```

E a última movimentação será removida com:

``` python
historico.pop()
```

A estrutura seguirá o princípio:

**LIFO --- Last In, First Out**

Ou seja:

> O último elemento inserido é o primeiro a ser removido.

### Aplicação no sistema

Se ocorrer:

``` text
1. Entrada de 20 Paracetamol
2. Saída de 5 Paracetamol
3. Entrada de 10 Dipirona
```

A última movimentação será a primeira a ser desfeita.

Isso representa naturalmente o funcionamento de uma pilha.

------------------------------------------------------------------------

# 8. Fila

A fila será utilizada para representar solicitações de reposição.

Exemplo:

``` python
fila_reposicao = []
```

As solicitações serão adicionadas ao final:

``` python
fila_reposicao.append(solicitacao)
```

E a primeira solicitação será atendida primeiro:

``` python
fila_reposicao.pop(0)
```

A estrutura seguirá o princípio:

**FIFO --- First In, First Out**

Ou seja:

> O primeiro elemento inserido é o primeiro a ser removido.

### Exemplo

``` text
Chegada:

1. Paracetamol
2. Dipirona
3. Ibuprofeno

Atendimento:

1. Paracetamol
2. Dipirona
3. Ibuprofeno
```

------------------------------------------------------------------------

# 9. Representação dos dados

Não será necessário utilizar classes.

Como POO ainda não foi estudada formalmente na disciplina, utilizaremos
**dicionários Python** para representar os registros.

Isso mantém o projeto simples e adequado ao conteúdo estudado.

## Medicamento

``` python
{
    "id": 1,
    "nome": "Paracetamol",
    "categoria": "Analgésico",
    "estoque": 20,
    "estoque_minimo": 10,
    "preco": 8.50
}
```

## Movimentação

``` python
{
    "tipo": "entrada",
    "medicamento_id": 1,
    "quantidade": 20
}
```

## Solicitação de reposição

``` python
{
    "id": 1,
    "medicamento_id": 1,
    "quantidade": 30,
    "status": "pendente"
}
```

O campo `status` permite distinguir solicitações pendentes de
solicitações já atendidas sem precisar apagar o registro quando ele sair
da fila.

Os dicionários serão utilizados apenas para facilitar a organização dos
dados. Não haverá necessidade de criar classes ou utilizar conceitos
avançados de orientação a objetos.

------------------------------------------------------------------------

# 10. Organização dos arquivos

A estrutura planejada será:

``` text
pharma_erp/
│
├── main.py
│
├── estruturas.py
│
├── medicamentos.py
│
│
├── estoque.py
│
└── reposicao.py
```

## `main.py`

Responsável pelo menu principal e integração do sistema.

## `estruturas.py`

Responsável por armazenar as listas compartilhadas pelo sistema.

Exemplo:

``` python
medicamentos = []
solicitacoes_reposicao = []
historico = []
fila_reposicao = []
```

Cada lista tem uma finalidade diferente:

-   `medicamentos` → entidade Medicamento;
-   `solicitacoes_reposicao` → entidade Solicitação de Reposição;
-   `historico` → pilha de movimentações;
-   `fila_reposicao` → fila FIFO contendo IDs de solicitações pendentes.

## `medicamentos.py`

Responsável pelo cadastro e gerenciamento de medicamentos.

## `estoque.py`

Responsável pelas entradas, saídas e histórico.

## `reposicao.py`

Responsável pelo CRUD das solicitações de reposição, pela fila FIFO e
pelo atendimento das solicitações.

Os relatórios poderão inicialmente ficar nos módulos correspondentes.
Caso a quantidade de código aumente, poderá ser criado posteriormente um
`relatorios.py`.

------------------------------------------------------------------------

# 11. Sprints

O desenvolvimento será dividido em cinco sprints principais.

``` text
Sprint 01
Modelagem + Estruturas

        ↓

Sprint 02
CRUD + Validações

        ↓

Sprint 03
Estoque + Pilha

        ↓

Sprint 04
Reposição + Fila

        ↓

Sprint 05
Relatórios + Integração + Testes
```

------------------------------------------------------------------------

# SPRINT 01 --- Modelagem e fundamentos

## Objetivo

Definir exatamente como o sistema funcionará antes de começar a
implementar todas as funcionalidades.

Nesta sprint serão estudadas e preparadas as estruturas:

-   lista;
-   pilha;
-   fila.

Também serão definidos os dados que serão armazenados.

------------------------------------------------------------------------

## Pessoa 1 --- Modelagem dos medicamentos

### Responsabilidades

-   definir os dados dos medicamentos;
-   definir quais campos são obrigatórios;
-   definir as regras básicas de estoque;
-   documentar a estrutura do medicamento.

### Estrutura inicial

``` python
{
    "id": 1,
    "nome": "Paracetamol",
    "categoria": "Analgésico",
    "estoque": 20,
    "estoque_minimo": 10,
    "preco": 8.50
}
```

### Entrega

Documento ou anotação contendo:

-   campos;
-   tipos de dados;
-   regras de validação;
-   exemplos.

------------------------------------------------------------------------

# Pessoa 2 --- Modelagem das solicitações de reposição

### Responsabilidades

-   definir os dados das solicitações de reposição;
-   definir campos obrigatórios;
-   definir os estados da solicitação;
-   pensar nas validações;
-   preparar exemplos de solicitações.

### Estrutura inicial

``` python
{
    "id": 1,
    "medicamento_id": 1,
    "quantidade": 30,
    "status": "pendente"
}
```

A solicitação será a **segunda entidade principal com CRUD** exigida
pelo TDE. A fila não substitui o cadastro da entidade: ela controla
apenas a ordem de atendimento das solicitações pendentes.

### Entrega

Definição da entidade Solicitação de Reposição e suas regras.

------------------------------------------------------------------------

# Pessoa 3 --- Estudo da Pilha

### Responsabilidades

Estudar e testar:

``` python
historico = []
```

Operações:

``` python
append()
pop()
```

Compreender:

-   LIFO;
-   topo;
-   inserção;
-   remoção;
-   complexidade.

### Teste

``` python
historico.append("Entrada +10")
historico.append("Saída -5")
historico.append("Entrada +20")

ultima = historico.pop()
```

### Entrega

Explicação de:

> Por que uma pilha é adequada para desfazer a última movimentação?

E análise:

``` text
append() → O(1)
pop() → O(1)
```

------------------------------------------------------------------------

# Pessoa 4 --- Estudo da Fila

### Responsabilidades

Estudar:

``` python
fila = []
```

Operações:

``` python
append()
pop(0)
```

Compreender:

-   FIFO;
-   frente;
-   fim;
-   inserção;
-   remoção;
-   complexidade.

### Teste

``` python
fila.append("Paracetamol")
fila.append("Dipirona")
fila.append("Ibuprofeno")

primeiro = fila.pop(0)
```

### Entrega

Explicação de:

> Por que uma fila é adequada para controlar solicitações de reposição?

E análise:

``` text
append() → O(1)
pop(0) → O(n)
```

------------------------------------------------------------------------

# Resultado esperado da Sprint 01

Ao final:

``` text
✓ Entidades definidas
✓ Campos definidos
✓ Lista compreendida
✓ Pilha compreendida
✓ Fila compreendida
✓ Complexidades iniciais estudadas
✓ Estrutura de arquivos definida
```

------------------------------------------------------------------------

# SPRINT 02 --- CRUD e validações

## Objetivo

Implementar as duas entidades principais exigidas pelo TDE:

1.  Medicamentos;
2.  Solicitações de reposição.

Cada uma deverá possuir operações de CRUD adequadas ao seu ciclo de
vida.

------------------------------------------------------------------------

# Pessoa 1 --- CRUD de medicamentos

Implementar:

``` text
Cadastrar
Consultar
Alterar
Remover
Listar
```

Também deverá implementar busca por ID.

Exemplo conceitual:

``` python
for medicamento in medicamentos:
    if medicamento["id"] == id_buscado:
        ...
```

Essa será uma **busca linear**.

### Complexidade

Melhor caso:

``` text
O(1)
```

Pior caso:

``` text
O(n)
```

------------------------------------------------------------------------

# Pessoa 2 --- CRUD de solicitações de reposição

Implementar:

``` text
Cadastrar
Consultar
Alterar
Remover
Listar
```

Também deverá realizar validações e manter a solicitação sincronizada
com a fila quando necessário.

A entidade será armazenada separadamente da fila:

``` python
solicitacoes_reposicao = []
fila_reposicao = []
```

A lista `solicitacoes_reposicao` representa o cadastro da entidade. A
`fila_reposicao` armazenará os **IDs das solicitações pendentes**,
mantendo a ordem FIFO.

------------------------------------------------------------------------

# Pessoa 3 --- Validações

Responsável por ajudar a padronizar as validações.

Exemplos:

``` text
Nome não pode ser vazio
ID não pode ser duplicado
Estoque não pode ser negativo
Preço deve ser positivo
```

As validações deverão ser utilizadas pelos módulos de medicamentos e
solicitações de reposição.

------------------------------------------------------------------------

# Pessoa 4 --- Integração inicial

Responsável por criar o primeiro menu funcional do sistema.

Exemplo:

``` text
========== PHARMA ERP ==========

1 - Medicamentos
2 - Reposição
0 - Sair
```

Também deverá testar se os módulos estão funcionando corretamente
juntos.

------------------------------------------------------------------------

# Resultado esperado da Sprint 02

``` text
✓ CRUD de medicamentos
✓ CRUD de solicitações de reposição
✓ Busca linear
✓ Validação de dados
✓ Menu inicial
✓ Listagem de registros
```

------------------------------------------------------------------------

# SPRINT 03 --- Estoque e Pilha

## Objetivo

Implementar o controle de estoque e o histórico de movimentações.

A estrutura principal desta sprint será a **Pilha**.

------------------------------------------------------------------------

# Pessoa 1 --- Entrada de estoque

Implementar:

``` text
Entrada de medicamento
```

Exemplo:

``` text
Paracetamol
Estoque atual: 20

Entrada: +10

Novo estoque: 30
```

Registrar a movimentação na pilha.

------------------------------------------------------------------------

# Pessoa 2 --- Saída de estoque

Implementar:

``` text
Saída de medicamento
```

Deverá impedir situações inválidas, como:

``` text
Estoque = 5
Saída = 10
```

Nesse caso:

``` text
Operação inválida:
estoque insuficiente.
```

Também deverá registrar a movimentação.

------------------------------------------------------------------------

# Pessoa 3 --- Pilha e desfazer

Implementar o histórico:

``` python
historico = []
```

E as operações:

``` text
Registrar movimentação
Visualizar histórico
Desfazer última movimentação
```

O desfazer deverá utilizar:

``` python
pop()
```

para remover o elemento do topo.

------------------------------------------------------------------------

# Pessoa 4 --- Integração e testes

Integrar:

``` text
Medicamentos
     ↓
Estoque
     ↓
Histórico
     ↓
Pilha
```

Criar testes para:

-   entrada;
-   saída;
-   estoque insuficiente;
-   histórico vazio;
-   desfazer movimentação.

------------------------------------------------------------------------

# Resultado esperado da Sprint 03

``` text
✓ Entrada de estoque
✓ Saída de estoque
✓ Histórico
✓ Pilha
✓ Desfazer
✓ Validações de estoque
```

------------------------------------------------------------------------

# SPRINT 04 --- CRUD de Reposição e Fila

## Objetivo

Criar o processo de reposição de medicamentos.

A estrutura utilizada será a **Fila**.

------------------------------------------------------------------------

# Pessoa 1 --- Identificação de estoque crítico

Criar uma função que percorra os medicamentos e encontre:

``` text
estoque < estoque_minimo
```

Exemplo:

``` text
Paracetamol
Estoque: 5
Mínimo: 20
```

Resultado:

``` text
Paracetamol precisa de reposição.
```

------------------------------------------------------------------------

# Pessoa 2 --- CRUD das solicitações de reposição

Criar a estrutura:

``` python
{
    "id": 1,
    "medicamento_id": 1,
    "quantidade": 30,
    "status": "pendente"
}
```

As solicitações deverão ser cadastradas em uma lista própria:

``` python
solicitacoes_reposicao.append(solicitacao)
```

Quando uma solicitação pendente for criada, seu ID será adicionado ao
final da fila:

``` python
fila_reposicao.append(solicitacao["id"])
```

Além do cadastro, o módulo deverá permitir consultar, alterar e remover
solicitações. Se uma solicitação ainda estiver pendente e for removida,
seu ID também deverá ser retirado da fila.

------------------------------------------------------------------------

# Pessoa 3 --- Implementação da fila

Implementar:

``` text
Adicionar solicitação à fila
Visualizar fila
Atender próxima solicitação
```

A fila armazenará IDs e o atendimento deverá utilizar:

``` python
id_solicitacao = fila_reposicao.pop(0)
```

Depois disso, o sistema deverá localizar a solicitação pelo ID e alterar
seu status para `"atendida"`.

------------------------------------------------------------------------

# Pessoa 4 --- Integração e regras

Integrar:

``` text
Estoque crítico
       ↓
Criação da solicitação
       ↓
Cadastro da entidade
       ↓
Fila
       ↓
Atendimento
       ↓
Status = atendida
```

Também deverá testar:

-   fila vazia;
-   uma solicitação;
-   várias solicitações;
-   atendimento na ordem correta;
-   alteração de uma solicitação;
-   remoção de uma solicitação pendente.

------------------------------------------------------------------------

# Separação entre entidade e fila

É importante distinguir o **cadastro das solicitações** da **fila de
atendimento**.

A entidade será armazenada em:

``` python
solicitacoes_reposicao = []
```

A fila armazenará apenas os IDs das solicitações pendentes:

``` python
fila_reposicao = []
```

Exemplo:

``` text
solicitacoes_reposicao

[0] ID 1 → Paracetamol → 30 unidades → pendente
[1] ID 2 → Dipirona    → 20 unidades → pendente
[2] ID 3 → Ibuprofeno  → 15 unidades → atendida
```

Enquanto a fila poderá estar:

``` text
fila_reposicao

[1, 2]
```

Assim, o CRUD atua sobre a entidade e a fila atua sobre a **ordem de
atendimento**. Quando a primeira solicitação for atendida, seu ID sai da
fila com `pop(0)` e o registro correspondente recebe o status
`"atendida"`.

Essa separação permite cumprir o requisito de CRUD para duas entidades
sem perder a aplicação prática da estrutura de fila.

------------------------------------------------------------------------

# Observação sobre prioridade

O projeto inicialmente utilizará uma **fila convencional FIFO**, porque
o professor informou que a fila de prioridade não é obrigatória.

Caso o grupo queira adicionar prioridade posteriormente, isso poderá ser
feito como uma melhoria.

Entretanto, isso **não deve comprometer o funcionamento da fila básica
nem consumir tempo que deveria ser utilizado para os requisitos
obrigatórios**.

------------------------------------------------------------------------

# Resultado esperado da Sprint 04

``` text
✓ Identificação de estoque crítico
✓ CRUD de solicitações de reposição
✓ Fila funcionando
✓ Atendimento FIFO
✓ Atualização de status
✓ Validações
✓ Integração com estoque
```

------------------------------------------------------------------------

# SPRINT 05 --- Relatórios, ordenação, integração e testes finais

## Objetivo

Finalizar o sistema e prepará-lo para apresentação.

------------------------------------------------------------------------

# Pessoa 1 --- Relatórios de medicamentos

Criar:

``` text
Listar todos os medicamentos
Filtrar por categoria
Pesquisar medicamento
```

Exemplo:

``` text
Categoria: Analgésico

Paracetamol
Dipirona
Ibuprofeno
```

------------------------------------------------------------------------

# Pessoa 2 --- Ordenação

Implementar manualmente um algoritmo de ordenação.

Sugestão:

**Bubble Sort**

Exemplo:

``` text
Antes:

Dipirona       R$ 10
Paracetamol    R$ 8
Ibuprofeno     R$ 15
```

Depois:

``` text
Paracetamol    R$ 8
Dipirona       R$ 10
Ibuprofeno     R$ 15
```

A implementação deverá ser própria, sem utilizar diretamente:

``` python
sort()
```

ou:

``` python
sorted()
```

Isso é importante porque o TDE quer avaliar o conhecimento dos
algoritmos.

------------------------------------------------------------------------

# Pessoa 3 --- Relatórios de estoque e histórico

Criar:

``` text
Medicamentos abaixo do mínimo
Histórico de movimentações
Fila de reposição
```

Exemplo:

``` text
====== ESTOQUE CRÍTICO ======

Paracetamol
Estoque: 5
Mínimo: 20

Dipirona
Estoque: 3
Mínimo: 15
```

------------------------------------------------------------------------

# Pessoa 4 --- Integração final e testes

Responsável por verificar o sistema completo.

Menu final:

``` text
========== PHARMA ERP ==========

1 - Medicamentos
2 - Estoque
3 - Reposição
4 - Relatórios
0 - Sair
```

Testar todos os fluxos.

------------------------------------------------------------------------

# 12. Testes obrigatórios antes da entrega

## Medicamentos

``` text
✓ Cadastro válido
✓ Cadastro com nome vazio
✓ ID duplicado
✓ Consulta existente
✓ Consulta inexistente
✓ Alteração
✓ Remoção
```

## Estoque

``` text
✓ Entrada
✓ Saída
✓ Estoque insuficiente
✓ Histórico
✓ Desfazer
```

## Pilha

``` text
✓ Inserção
✓ Remoção do topo
✓ Pilha vazia
```

## Solicitações de reposição

``` text
✓ Cadastro
✓ Consulta
✓ Alteração
✓ Remoção
✓ Dados obrigatórios
```

## Fila

``` text
✓ Inserção
✓ Atendimento FIFO
✓ Fila vazia
✓ Múltiplas solicitações
✓ Atendimento atualiza status
```

## Relatórios

``` text
✓ Listagem
✓ Filtro
✓ Busca
✓ Ordenação
✓ Histórico
✓ Fila
```

------------------------------------------------------------------------

# 13. Distribuição final das responsabilidades

A divisão geral ficará:

  Pessoa         Responsabilidade principal
  -------------- ----------------------------------------------------
  **Pessoa 1**   Medicamentos + busca + relatórios
  **Pessoa 2**   Solicitações de reposição + validações + ordenação
  **Pessoa 3**   Estoque + Pilha + histórico
  **Pessoa 4**   Fila + integração + testes

Essa divisão é uma **divisão de desenvolvimento**, não uma divisão de
conhecimento.

Todos devem entender:

-   como a lista funciona;
-   como a pilha funciona;
-   como a fila funciona;
-   como funciona o CRUD;
-   como funciona a busca;
-   como funciona a ordenação;
-   quais são as complexidades;
-   por que cada estrutura foi escolhida.

------------------------------------------------------------------------

# 14. Complexidades que deverão ser estudadas

Ao final do projeto, precisamos conseguir explicar pelo menos:

  Operação                                Estrutura/algoritmo   Complexidade
  --------------------------------------- --------------------- -------------------
  Inserção no final                       Lista Python          O(1)
  Busca linear --- melhor caso            Lista                 O(1)
  Busca linear --- pior caso              Lista                 O(n)
  Remoção por posição/ID                  Lista                 O(n) no pior caso
  Inserção na pilha                       Pilha                 O(1)
  Remoção da pilha                        Pilha                 O(1)
  Inserção na fila                        Fila                  O(1)
  Remoção da frente com `pop(0)`          Fila                  O(n)
  Bubble Sort --- melhor caso otimizado   Ordenação             O(n)
  Bubble Sort --- pior caso               Ordenação             O(n²)

As complexidades devem ser explicadas pelo funcionamento das operações,
e não simplesmente decoradas.

------------------------------------------------------------------------

# 15. Regras para o desenvolvimento

## Regra 1 --- Não utilizar soluções que não conseguimos explicar

Se alguém encontrar na internet uma implementação muito complexa de uma
fila, por exemplo:

``` python
heapq
deque
classes avançadas
```

não devemos simplesmente copiar.

Primeiro devemos entender se aquilo realmente é necessário.

------------------------------------------------------------------------

## Regra 2 --- Não utilizar algoritmos prontos quando o objetivo é implementar o algoritmo

Para a ordenação, por exemplo, não devemos fazer:

``` python
medicamentos.sort()
```

se queremos demonstrar um algoritmo de ordenação.

Devemos implementar o algoritmo manualmente.

------------------------------------------------------------------------

## Regra 3 --- Código simples é uma vantagem

Não precisamos tentar escrever código extremamente sofisticado.

Um código como:

``` python
for medicamento in medicamentos:
    if medicamento["id"] == id_buscado:
        return medicamento
```

é perfeitamente válido.

O importante é saber explicar o que está acontecendo.

------------------------------------------------------------------------

## Regra 4 --- Evitar POO

Não precisamos utilizar:

``` python
class Medicamento:
```

ou:

``` python
class Pilha:
```

A utilização de dicionários é suficiente para representar os dados.

Caso utilizemos algum recurso de objetos posteriormente, ele deverá ser
pequeno e todos deverão entender sua finalidade.

------------------------------------------------------------------------

# 16. Fluxo que deverá ser demonstrado na apresentação

Uma boa demonstração do sistema será:

``` text
1. Cadastrar medicamento
          ↓
2. Consultar medicamento
          ↓
4. Alterar medicamento
          ↓
5. Fazer entrada no estoque
          ↓
6. Fazer saída no estoque
          ↓
7. Mostrar histórico
          ↓
8. Desfazer última movimentação
          ↓
9. Mostrar medicamento abaixo do estoque mínimo
          ↓
10. Criar solicitação de reposição
          ↓
11. Adicionar à fila
          ↓
12. Mostrar fila
          ↓
13. Atender primeira solicitação
          ↓
14. Gerar relatório
          ↓
15. Demonstrar busca
          ↓
16. Demonstrar ordenação
```

Esse fluxo permite demonstrar praticamente todos os requisitos do TDE em
poucos minutos.

------------------------------------------------------------------------

# 17. O que cada integrante deverá saber para a apresentação

## Pessoa 1

Deverá dominar:

-   lista;
-   cadastro de medicamentos;
-   busca linear;
-   filtros;
-   complexidade da busca.

## Pessoa 2

Deverá dominar:

-   validação;
-   ordenação;
-   Bubble Sort;
-   complexidade da ordenação.

## Pessoa 3

Deverá dominar:

-   pilha;
-   LIFO;
-   `append()`;
-   `pop()`;
-   histórico;
-   desfazer;
-   complexidade O(1).

## Pessoa 4

Deverá dominar:

-   fila;
-   FIFO;
-   `append()`;
-   `pop(0)`;
-   reposição;
-   complexidade O(n) da remoção da frente.

------------------------------------------------------------------------

# 18. Resultado final esperado

Ao final do projeto, devemos possuir um sistema de terminal que permita:

``` text
                    PHARMA ERP
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
      LISTA           PILHA             FILA
        │               │                │
        ▼               ▼                ▼
 Medicamentos      Movimentações     Reposições
 Solicitação de reposiçãoes      de estoque        de estoque
        │               │                │
        ▼               ▼                ▼
      CRUD           Desfazer          FIFO
        │
        ▼
 Busca + Filtros + Ordenação
                        │
                        ▼
                    RELATÓRIOS
```

O objetivo não é criar um ERP comercial completo. O objetivo é mostrar
que conseguimos **modelar um problema real e escolher estruturas
lineares adequadas para resolvê-lo**, implementando as operações e
explicando suas complexidades.

------------------------------------------------------------------------

# 19. Checklist geral do projeto

### Sprint 01

-   [ ] Definir entidades
-   [ ] Definir atributos
-   [ ] Definir regras
-   [ ] Estudar lista
-   [ ] Estudar pilha
-   [ ] Estudar fila
-   [ ] Definir estrutura de arquivos

### Sprint 02

-   [ ] CRUD de medicamentos
-   [ ] CRUD de solicitações de reposição
-   [ ] Busca linear
-   [ ] Validações
-   [ ] Menu inicial

### Sprint 03

-   [ ] Entrada de estoque
-   [ ] Saída de estoque
-   [ ] Histórico
-   [ ] Pilha
-   [ ] Desfazer

### Sprint 04

-   [ ] Detectar estoque crítico
-   [ ] Criar reposição
-   [ ] Fila
-   [ ] Atendimento FIFO
-   [ ] Testar fila

### Sprint 05

-   [ ] Relatórios
-   [ ] Filtros
-   [ ] Ordenação manual
-   [ ] Integração
-   [ ] Testes finais
-   [ ] Preparação da apresentação
-   [ ] Revisão das complexidades

------------------------------------------------------------------------

# 20. Princípio principal do projeto

Durante todo o desenvolvimento devemos manter uma pergunta como
referência:

> **"Por que essa estrutura é adequada para esse problema?"**

Não basta dizer:

> "Usamos uma lista porque Python tem lista."

Precisamos conseguir dizer:

> "Utilizamos listas para representar entidades porque precisamos
> percorrer, consultar, alterar e remover registros."

Da mesma forma:

> "Utilizamos uma pilha para o histórico porque precisamos desfazer a
> última movimentação, seguindo o comportamento LIFO."

E:

> "Utilizamos uma fila para as solicitações de reposição porque queremos
> processá-las pela ordem de chegada, seguindo o comportamento FIFO."

Essa justificativa é uma das partes mais importantes do TDE.
