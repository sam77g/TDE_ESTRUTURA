<div align="center">

# PharmaERP

**Sistema de gerenciamento de medicamentos e solicitações de reposição para uma farmácia, desenvolvido em Python como projeto acadêmico de Estruturas de Dados.**

![Status](https://img.shields.io/badge/status-vers%C3%A3o%20final-green)
![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Estruturas](https://img.shields.io/badge/estruturas-Lista%20%7C%20Pilha%20%7C%20Fila-blue)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)

</div>

---

## Sumário

1. [Sobre o Projeto](#1-sobre-o-projeto)
2. [Objetivos](#2-objetivos)
3. [Funcionalidades](#3-funcionalidades)
4. [Estruturas de Dados](#4-estruturas-de-dados)
5. [Algoritmos](#5-algoritmos)
6. [Regras de Negócio](#6-regras-de-negócio)
7. [Arquitetura do Projeto](#7-arquitetura-do-projeto)
8. [Tecnologias e Dependências](#8-tecnologias-e-dependências)
9. [Pré-requisitos](#9-pré-requisitos)
10. [Como Executar](#10-como-executar)
11. [Fluxo do Sistema](#11-fluxo-do-sistema)
12. [Complexidade](#12-complexidade)
13. [Versionamento e Git](#13-versionamento-e-git)
14. [Status do Projeto](#14-status-do-projeto)
15. [Licença](#15-licença)

---

## 1. Sobre o Projeto

O **PharmaERP** é um sistema de gerenciamento de uma farmácia executado diretamente no terminal.

O projeto foi desenvolvido como atividade acadêmica da disciplina de **Algoritmos e Estruturas de Dados**, com foco na aplicação prática de **estruturas de dados lineares**, algoritmos de busca, ordenação e manipulação de registros.

O sistema permite cadastrar e administrar medicamentos, acompanhar o estoque, criar e gerenciar solicitações de reposição e registrar as movimentações realizadas.

O projeto demonstra, de forma prática, a utilização de:

- **Lista** para armazenamento e gerenciamento dos medicamentos;
- **Pilha** para controle do histórico e operação de desfazer;
- **Fila** para gerenciamento das solicitações de reposição;
- **Prioridade por criticidade** para atender primeiro situações mais urgentes.

> **Observação:** os dados são mantidos somente em memória. Ao encerrar o programa, os registros são perdidos.

---

## 2. Objetivos

O desenvolvimento do PharmaERP tem como principais objetivos:

- Aplicar estruturas de dados lineares em um sistema funcional;
- Implementar inserção, busca, alteração e remoção;
- Utilizar busca linear;
- Implementar manualmente um algoritmo de ordenação;
- Trabalhar com comportamento **LIFO** através de uma pilha;
- Trabalhar com **FIFO combinado com prioridade** nas solicitações de reposição;
- Praticar modularização em Python;
- Implementar validação e tratamento de entradas;
- Demonstrar conceitos de complexidade de algoritmos.

---

## 3. Funcionalidades

### 3.1. Gerenciamento de medicamentos

O sistema permite:

- Cadastrar medicamentos;
- Alterar categoria, estoque e preço;
- Remover medicamentos;
- Listar todos os medicamentos;
- Buscar medicamento pelo nome;
- Filtrar medicamentos por categoria;
- Listar medicamentos ordenados por preço;
- Validar os dados antes do cadastro;
- Impedir nomes duplicados.

Cada medicamento possui informações como:

```text
medicamento
categoria
estoque
preco
id
```

Categorias disponíveis:

- **Ético**
- **Genérico**
- **Similar**

---

### 3.2. Gerenciamento de reposições

Quando o estoque de um medicamento fica abaixo do limite mínimo, o sistema cria automaticamente uma solicitação de reposição.

Uma solicitação possui:

```text
medicamento
id_repo
id_medicamento
criticidade
quantidade_solicitada
```

O sistema permite:

- Buscar uma solicitação;
- Listar solicitações pendentes;
- Atender uma solicitação;
- Cancelar uma solicitação;
- Alterar a quantidade solicitada;
- Evitar solicitações duplicadas.

---

### 3.3. Criticidade e prioridade

As solicitações recebem uma classificação automática de acordo com a quantidade disponível no estoque.

| Estoque | Criticidade | Prioridade |
|---:|:---|---:|
| Menor que 5 | **CRÍTICO** | 1ª |
| 5 a 9 | **ALERTA** | 2ª |
| 10 a 14 | **AVISO** | 3ª |
| 15 ou mais | Sem reposição | — |

As solicitações são organizadas de acordo com a criticidade.

Quando duas solicitações possuem a mesma criticidade, a ordem de chegada é preservada.

Dessa forma:

```text
CRÍTICO
   ↓
ALERTA
   ↓
AVISO
```

Em caso de empate:

```text
Primeiro a chegar
       ↓
Primeiro a ser atendido
```

---

### 3.4. Histórico e desfazer

As entradas e saídas de medicamentos são registradas no histórico.

O sistema permite:

- Visualizar o histórico;
- Registrar data e hora das movimentações;
- Desfazer a última movimentação.

A operação de desfazer utiliza o princípio:

**LIFO — Last In, First Out**

Exemplo:

```text
Movimentação A
Movimentação B
Movimentação C ← última movimentação

Desfazer → Movimentação C
```

---

### 3.5. DEBUG

O sistema possui um menu de **DEBUG** utilizado para visualizar diretamente o conteúdo das principais estruturas de dados.

São exibidos:

- Lista de medicamentos;
- Pilha de histórico;
- Fila de solicitações de reposição.

Esse recurso facilita a demonstração prática das estruturas durante a apresentação acadêmica.

---

## 4. Estruturas de Dados

### 4.1. Lista

A lista Python é utilizada para armazenar os medicamentos:

```python
medicamentos = []
```

Ela permite realizar:

- Inserção;
- Remoção;
- Busca;
- Percurso;
- Filtragem;
- Ordenação.

A lista representa o cadastro principal do sistema.

---

### 4.2. Pilha — LIFO

O histórico utiliza uma lista Python como estrutura de pilha:

```python
historico = []
```

Novas movimentações são adicionadas utilizando `append()` e a última movimentação é retirada utilizando `pop()`.

Isso representa o comportamento:

**Last In, First Out — LIFO**

---

### 4.3. Fila de reposição

As solicitações utilizam `collections.deque`:

```python
from collections import deque

solicitacoes_reposicao = deque()
```

O sistema combina o conceito de fila com prioridade por criticidade.

A prioridade utilizada é:

```text
CRÍTICO → ALERTA → AVISO
```

Quando duas solicitações possuem a mesma prioridade, o sistema preserva a ordem de chegada.

---

## 5. Algoritmos

### 5.1. Busca Linear

A busca linear é utilizada para localizar medicamentos e solicitações de reposição.

O algoritmo percorre os elementos sequencialmente até encontrar o registro desejado.

Complexidade:

- Melhor caso: **O(1)**
- Pior caso: **O(n)**

---

### 5.2. Filtragem por Categoria

O sistema percorre a lista de medicamentos e seleciona os registros que pertencem à categoria informada.

Complexidade:

**O(n)**

---

### 5.3. Bubble Sort

A listagem de medicamentos por preço utiliza uma implementação manual do **Bubble Sort**.

O algoritmo possui uma otimização de parada antecipada: caso nenhuma troca ocorra durante uma passagem, significa que a lista já está ordenada.

Complexidade:

- Melhor caso: **O(n)**
- Pior caso: **O(n²)**

---

### 5.4. Inserção por Prioridade

As solicitações são inseridas de acordo com sua criticidade.

A prioridade pode ser representada por:

```python
PRIORIDADE = {
    "CRÍTICO": 0,
    "ALERTA": 1,
    "AVISO": 2
}
```

A inserção procura a posição adequada para manter a fila organizada.

Complexidade:

- Melhor caso: **O(1)** quando a inserção ocorre no final;
- Pior caso: **O(n)**.

---

## 6. Regras de Negócio

| Regra | Comportamento |
|---|---|
| Estoque mínimo | **15 unidades** |
| Estoque < 5 | **CRÍTICO** |
| Estoque de 5 a 9 | **ALERTA** |
| Estoque de 10 a 14 | **AVISO** |
| Estoque ≥ 15 | Não cria nova reposição |
| Quantidade solicitada padrão | `15 - estoque atual` |
| Reposição duplicada | Não permitida |
| Empate de criticidade | Mantém ordem de chegada |
| Medicamento removido | Cancela reposição pendente |
| Estoque alterado para ≥ 15 | Cancela reposição pendente |

### Atendimento de uma reposição

O processo de atendimento segue aproximadamente estas etapas:

1. Identificar a solicitação prioritária;
2. Localizar o medicamento pelo ID;
3. Informar a quantidade a ser adicionada;
4. Atualizar o estoque;
5. Remover a solicitação atendida;
6. Verificar novamente a situação do estoque.

---

## 7. Arquitetura do Projeto

A aplicação foi dividida em módulos para separar responsabilidades.

```text
TDE_ESTRUTURA/
│
├── tde/
│   ├── main.py
│   ├── estruturas.py
│   ├── medicamentos.py
│   ├── reposicao.py
│   ├── relatorios.py
│   ├── estoque.py
│   └── validar.py
│
├── CONTRIBUTING.md
├── DOCUMENTAÇÃO.md
├── LICENSE
├── README.md
└── .gitignore
```

### Responsabilidade dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Inicialização e menus principais |
| `estruturas.py` | Estruturas globais e funções de DEBUG |
| `medicamentos.py` | CRUD e consultas de medicamentos |
| `reposicao.py` | Solicitações, criticidade, prioridade e atendimento |
| `relatorios.py` | Histórico, entradas, saídas e desfazer |
| `estoque.py` | Geração dos IDs |
| `validar.py` | Validação e leitura segura dos dados |

A modularização permite separar responsabilidades e facilita a manutenção do código.

---

## 8. Tecnologias e Dependências

### Linguagem

- **Python 3.12+**

### Bibliotecas externas

| Biblioteca | Finalidade |
|---|---|
| `pyfiglet` | Geração do título ASCII do PharmaERP |
| `colorama` | Cores e estilos no terminal |

### Biblioteca padrão

| Recurso | Finalidade |
|---|---|
| `collections.deque` | Estrutura das solicitações de reposição |
| `datetime` | Registro de data e hora |
| `os` | Operações relacionadas ao terminal |

---

## 9. Pré-requisitos

Para executar o projeto, é necessário possuir:

- **Python 3.12 ou superior**;
- Terminal compatível com execução de programas Python;
- Git, caso queira clonar o projeto.

Verifique a versão instalada:

```bash
python --version
```

Caso seu sistema utilize `python3`:

```bash
python3 --version
```

---

## 10. Como Executar

### 10.1. Clonar o repositório

```bash
git clone https://github.com/sam77g/TDE_ESTRUTURA.git
```

### 10.2. Acessar o projeto

```bash
cd TDE_ESTRUTURA/tde
```

### 10.3. Instalar as dependências

```bash
pip install pyfiglet colorama
```

Ou:

```bash
pip3 install pyfiglet colorama
```

### 10.4. Executar

```bash
python main.py
```

Ou:

```bash
python3 main.py
```

---

### Menus principais

```text
Menu principal

├── [1] Medicamentos
│   ├── Adicionar
│   ├── Alterar
│   ├── Remover
│   ├── Listar
│   ├── Buscar
│   ├── Listar por categoria
│   └── Ordenar por preço
│
├── [2] Reposição
│   ├── Buscar
│   ├── Listar
│   ├── Atender
│   ├── Cancelar
│   └── Alterar
│
├── [3] Histórico
│   ├── Listar
│   └── Desfazer
│
├── [4] DEBUG
│
└── [0] Sair
```

---

## 11. Fluxo do Sistema

O fluxo geral do PharmaERP pode ser representado da seguinte maneira:

```text
                    ┌──────────────────┐
                    │    PharmaERP     │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
        Medicamentos     Reposição       Histórico
              │              │              │
              ▼              ▼              ▼
           Lista       Prioridade/FIFO     Pilha
              │              │              │
              ▼              ▼              ▼
       CRUD / Busca      Criticidade      Desfazer
       / Ordenação       / Atendimento
```

### Fluxo de reposição

```text
Cadastro/alteração do medicamento
              │
              ▼
        Estoque < 15?
         /        \
       não        sim
        │           │
        ▼           ▼
   Sem pedido   Criar pedido
                    │
                    ▼
              Classificar por
               criticidade
                    │
                    ▼
             Inserir na fila
                    │
                    ▼
          Buscar / Alterar / Cancelar
                    │
                    ▼
                  Atender
```

---

## 12. Complexidade

| Operação | Estrutura / Algoritmo | Complexidade |
|---|---|---|
| Inserção de medicamento | Lista `append()` | O(1) |
| Busca de medicamento | Busca linear | O(n) |
| Filtro por categoria | Percurso sequencial | O(n) |
| Ordenação por preço | Bubble Sort | O(n²) |
| Registro no histórico | Pilha `append()` | O(1) |
| Desfazer histórico | `pop()` + ajustes | O(n) no pior caso |
| Busca de reposição | Busca linear | O(n) |
| Inserção por prioridade | Percurso + inserção | O(n) no pior caso |
| Cancelamento de reposição | Busca + remoção | O(n) |
| Atendimento | Busca do medicamento + remoção | O(n) |

> As complexidades representam o custo das operações sobre as estruturas utilizadas. Operações auxiliares, como localizar um medicamento antes de atualizar seu estoque, também influenciam o custo total.

---

## 13. Versionamento e Git

O desenvolvimento utiliza **Git** para controle de versões e organização das funcionalidades.

Branches utilizadas durante o desenvolvimento:

```text
main
develop
feature/*
fix/*
final_version
```

A branch **`final_version`** representa a versão consolidada utilizada para a entrega final do projeto.

### Conventional Commits

O projeto utiliza a convenção de commits:

| Prefixo | Utilização |
|---|---|
| `feat` | Nova funcionalidade |
| `fix` | Correção de problema |
| `docs` | Documentação |
| `refactor` | Refatoração |
| `test` | Testes |

Exemplo:

```bash
git commit -m "feat: adiciona prioridade por criticidade na fila"
```

Para informações sobre colaboração e organização do repositório, consulte o [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## 14. Status do Projeto

**Versão final acadêmica.**

### Implementado

- [x] CRUD de medicamentos;
- [x] Validação de dados;
- [x] Busca linear;
- [x] Filtro por categoria;
- [x] Bubble Sort por preço;
- [x] IDs independentes para medicamentos e reposições;
- [x] Criação automática de solicitações;
- [x] Criticidade **CRÍTICO**, **ALERTA** e **AVISO**;
- [x] Fila com prioridade;
- [x] FIFO em casos de empate;
- [x] Busca de reposições;
- [x] Alteração de solicitações;
- [x] Cancelamento de solicitações;
- [x] Atendimento de reposições;
- [x] Histórico de entradas e saídas;
- [x] Desfazer última movimentação;
- [x] DEBUG das estruturas;
- [x] Interface de terminal com `pyfiglet` e `colorama`.

### Fora do escopo da versão atual

- [ ] Persistência em arquivos;
- [ ] Banco de dados;
- [ ] Autenticação de usuários;
- [ ] Interface gráfica;
- [ ] API;
- [ ] Integração com fornecedores.

Esses recursos não fazem parte do escopo da versão acadêmica atual.

---

## 15. Licença

Este projeto está licenciado sob a **MIT License**.

Consulte o arquivo [`LICENSE`](./LICENSE) para obter o texto completo da licença.

---

<div align="center">

**PharmaERP — TDE Estruturas de Dados**

Desenvolvido por **Samuel, Samoel, Marcos e Gabriel**.

</div>
