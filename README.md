<div align="center">

# PharmaERP

Sistema ERP de linha de comando para o controle de estoque e reposição de uma farmácia, desenvolvido como trabalho acadêmico (TDE) da disciplina de **Algoritmos e Estruturas de Dados**, ministrada pelo Prof. Gean Paulo (UNIFAN - Centro Universitário Nobre, 2026.2).

![Status](https://img.shields.io/badge/status-Entrega%20TDE-green)
![Versão](https://img.shields.io/badge/vers%C3%A3o-v1.1.0-green)
![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Estruturas](https://img.shields.io/badge/estruturas-Lista%20%7C%20Pilha%20%7C%20Fila-blue)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)

</div>

---

## Sumário

1. [Sobre o Projeto](#1-sobre-o-projeto)
2. [Funcionalidades](#2-funcionalidades)
3. [Estruturas de Dados e Algoritmos](#3-estruturas-de-dados-e-algoritmos)
4. [Regras de Negócio](#4-regras-de-negócio)
5. [Tecnologias Utilizadas](#5-tecnologias-utilizadas)
6. [Estrutura do Projeto](#6-estrutura-do-projeto)
7. [Pré-requisitos](#7-pré-requisitos)
8. [Como Executar](#8-como-executar)
9. [Versionamento](#9-versionamento)
10. [Fluxo de Desenvolvimento](#10-fluxo-de-desenvolvimento)
11. [Status do Projeto](#11-status-do-projeto)
12. [Licença](#12-licença)

---

## 1. Sobre o Projeto

O **PharmaERP** é um sistema de ERP (*Enterprise Resource Planning*) executado no terminal, ambientado em uma farmácia. Ele controla o cadastro de medicamentos, a fila de pedidos de reposição de estoque e o histórico de movimentações, com possibilidade de desfazer a última ação.

O projeto tem finalidade acadêmica e busca aplicar, de forma prática, os conceitos de estruturas de dados lineares (**lista**, **pilha** e **fila**), algoritmos de busca e ordenação implementados manualmente e análise de complexidade, conforme a proposta do TDE.

> Os dados são mantidos **em memória**: ao encerrar o programa, as informações são descartadas.

## 2. Funcionalidades

- **CRUD de Medicamentos**: cadastro, consulta, alteração (categoria, estoque e preço) e remoção, com validação dos dados obrigatórios e bloqueio de nomes duplicados.
- **CRUD de Reposição**: consulta, listagem, alteração da quantidade solicitada, cancelamento e atendimento das solicitações de reposição.
- **Reposição automática**: ao cadastrar ou alterar um medicamento com estoque abaixo do mínimo, uma solicitação é criada na fila.
- **Histórico com desfazer**: registro de entradas e saídas, com opção de desfazer a última movimentação.
- **Relatórios**: listagem de todos os registros, filtro por categoria, listagem ordenada por preço, exibição da fila de reposição e exibição do histórico.
- **Entrada de dados segura**: valores não numéricos nos campos numéricos são recusados e solicitados novamente, sem encerrar o programa.
- **Modo DEBUG**: exibe o conteúdo bruto das estruturas para conferência durante a apresentação.

## 3. Estruturas de Dados e Algoritmos

### 3.1. Estruturas utilizadas

| Estrutura | Implementação | Onde é usada | Operações permitidas |
| --------- | ------------- | ------------ | -------------------- |
| **Lista** | `list` | Cadastro de medicamentos (`medicamentos`) | Inserção, remoção, busca e travessia |
| **Pilha (LIFO)** | `list` | Histórico de movimentações (`historico`) | Apenas `append` e `pop` no topo |
| **Fila (FIFO)** | `collections.deque` | Solicitações de reposição (`solicitacoes_reposicao`) | `append` no fim e `popleft` no início |

**Por que cada estrutura?**

- **Lista**: o cadastro precisa de inserção, remoção, busca e percurso completo para os relatórios.
- **Pilha**: desfazer sempre atua sobre a ação **mais recente**, comportamento natural de uma pilha (último a entrar, primeiro a sair).
- **Fila**: as reposições devem ser atendidas na **ordem de chegada** (primeiro a entrar, primeiro a sair). O `deque` foi escolhido porque o `popleft()` é O(1), enquanto `list.pop(0)` seria O(n).

### 3.2. Algoritmos implementados manualmente

| Algoritmo | Uso |
| --------- | --- |
| **Busca linear** | Localizar medicamentos e reposições pelo nome |
| **Filtro sequencial** | Listar medicamentos por categoria |
| **Bubble Sort** (com parada antecipada) | Listar medicamentos ordenados por preço |

### 3.3. Complexidade

| Operação | Estrutura / algoritmo | Melhor caso | Pior caso |
| -------- | --------------------- | ----------- | --------- |
| Cadastrar medicamento | Lista (`append`) | O(1) | O(1) |
| Buscar medicamento por nome | Busca linear | O(1) | O(n) |
| Listar por categoria | Filtro sequencial | O(n) | O(n) |
| Listar ordenado por preço | Bubble Sort | O(n) (já ordenado) | O(n²) |
| Registrar movimentação | Pilha (`append`) | O(1) | O(1) |
| Desfazer última movimentação | Pilha (`pop`) + ajuste na lista | O(1) (histórico vazio) | O(n)* |
| Criar solicitação de reposição | Fila (`append`) | O(1) (fila vazia) | O(n)** |
| Atender próxima reposição | Fila (`popleft`) | O(1) | O(n)*** |
| Cancelar reposição | Fila (`remove` no meio) | O(1) | O(n) |

\* Desfazer percorre a lista de medicamentos (para remover o item) ou a fila (para recriar a reposição). O `pop` da pilha em si é O(1).

\** O `append` é O(1); o que custa O(n) é a verificação de duplicidade feita antes de inserir.

\*** O `popleft` é O(1); o que custa O(n) é localizar o medicamento na lista para somar a quantidade recebida ao estoque.

> O **cancelamento** remove um item do meio da fila (O(n)). Trata-se de uma exceção ao comportamento FIFO, justificada porque o fluxo normal usa apenas `append` e `popleft`.

## 4. Regras de Negócio

| Regra | Valor |
| ----- | ----- |
| Estoque mínimo | **15 unidades** (abaixo disso, é criada uma reposição) |
| Criticidade **CRÍTICO** | estoque menor que 5 |
| Criticidade **ALERTA** | estoque de 5 a 9 |
| Criticidade **AVISO** | estoque de 10 a 14 |
| Quantidade solicitada (padrão) | `15 - estoque atual` |
| Categorias | Ético, Genérico e Similar |

**Atendimento de reposição:** o primeiro da fila é atendido, a quantidade recebida é somada ao estoque do medicamento e, se o estoque continuar abaixo do mínimo, uma nova solicitação é colocada no **fim** da fila.

**Desfazer:**

- Desfazer uma **entrada** remove o medicamento cadastrado e cancela a reposição pendente.
- Desfazer uma **saída** devolve o medicamento e recria a reposição, caso o estoque esteja abaixo do mínimo.

## 5. Tecnologias Utilizadas

| Tecnologia | Finalidade |
| ---------- | ---------- |
| **Python 3.12+** | Linguagem de desenvolvimento |
| **`collections.deque`** | Implementação da fila |
| **`datetime`** | Registro de data e hora das movimentações |
| **`match/case`** | Controle dos menus |

> O projeto utiliza apenas a biblioteca padrão do Python. Não há dependências externas.

## 6. Estrutura do Projeto

```text
TDE_ESTRUTURA/
├── tde/
│   ├── main.py            # Menu principal e controle do fluxo
│   ├── estruturas.py      # Lista, pilha e fila (estruturas globais) e DEBUG
│   ├── medicamentos.py    # CRUD de medicamentos, filtro e Bubble Sort
│   ├── reposicao.py       # CRUD de reposição e atendimento da fila
│   ├── relatorios.py      # Histórico (pilha) e desfazer
│   ├── estoque.py         # Geração de IDs
│   └── validar.py         # Validações e leitura segura de dados
├── DOCUMENTAÇÃO.md        # Planejamento e estudo das estruturas
├── LICENSE                # Licença MIT
└── README.md              # Documentação geral do projeto
```

## 7. Pré-requisitos

- **Python 3.12 ou superior** (o código usa `match/case` e f-strings com aspas aninhadas).
- Terminal (Prompt de Comando, PowerShell, Terminal do Linux ou macOS).
- *(Opcional)* [Git](https://git-scm.com/) para clonagem do repositório.
- *(Opcional)* Editor de código, como o [Visual Studio Code](https://code.visualstudio.com/).

Para verificar a versão instalada:

```bash
python --version
```

## 8. Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/sam77g/TDE_ESTRUTURA.git
   ```

2. Acesse a pasta do código-fonte:

   ```bash
   cd TDE_ESTRUTURA/tde
   ```

3. Execute o sistema:

   ```bash
   python main.py
   ```

> O programa deve ser executado **de dentro da pasta `tde/`**, pois os módulos são importados diretamente. Por se tratar de um projeto sem dependências, não há etapa de instalação.

### Menus do sistema

```text
Menu principal
├── [1] Medicamentos
│   ├── Adicionar / Alterar / Remover
│   ├── Listar / Buscar
│   ├── Listar por categoria
│   └── Listar ordenado por preço
├── [2] Reposição
│   ├── Buscar / Listar
│   ├── Atender (próxima da fila)
│   ├── Cancelar
│   └── Alterar quantidade solicitada
├── [3] Histórico
│   ├── Listar
│   └── Desfazer última movimentação
├── [4] DEBUG
└── [0] Sair
```

### Roteiro de demonstração

1. Cadastre **Dipirona** com estoque **3** e **Amoxicilina** com estoque **8** (duas reposições entram na fila).
2. Em **Reposição → Listar**, confira a ordem de chegada.
3. **Atenda** a primeira reposição com quantidade **5**: a Dipirona vai para 8 e volta ao fim da fila.
4. **Altere** a quantidade solicitada e **cancele** uma reposição.
5. Em **Histórico**, liste as movimentações e **desfaça** a última.
6. Use **DEBUG** para mostrar o estado das três estruturas.

## 9. Versionamento

O projeto adota **Git Tags** para identificar seus marcos de desenvolvimento.

| Versão | Descrição |
| ------ | --------- |
| `v0.1.10` | Estrutura inicial e estudo de lista, pilha e fila |
| `v0.1.35` | CRUD de medicamentos, reposição e histórico |
| `v1.1.0` | Versão final para entrega e apresentação |

As versões publicadas não devem ser alteradas. Correções em versões já publicadas devem originar uma nova versão.

## 10. Fluxo de Desenvolvimento

O desenvolvimento segue um fluxo baseado em *branches* e *Pull Requests*:

- **`main`**: versão estável, destinada à entrega. Não recebe *commits* diretos.
- **`feature/*` e `fix/*`**: *branches* de trabalho (por exemplo, `feature/novo-estoque`), integradas à `main` por *Pull Request*.
- **develop** : versão de teste / produção 

```text
feature/nome-da-tarefa ──► Pull Request ──► main
```

**Padrão de commits:** [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/).

| Prefixo | Uso |
| ------- | --- |
| `feat` | Nova funcionalidade |
| `fix` | Correção de problema |
| `docs` | Alteração na documentação |
| `refactor` | Reorganização de código sem alteração de comportamento |

Exemplo:

```bash
git commit -m "feat: adiciona atendimento da fila de reposição"
```

## 11. Status do Projeto

🚧 **Entrega do TDE** — etapa `v1.1.0` (lista, pilha, fila, busca, ordenação, CRUD e relatórios).

- [x] Lista: cadastro de medicamentos (CRUD completo)
- [x] Pilha: histórico de movimentações com desfazer
- [x] Fila: solicitações de reposição (FIFO) com atendimento
- [x] CRUD de uma segunda entidade (Reposição)
- [x] Busca linear e ordenação manual (Bubble Sort)
- [x] Validação de dados e leitura segura de entradas
- [x] Relatórios: listar, filtrar, exibir fila e exibir histórico
- [ ] Persistência dos dados em arquivo (hoje os dados ficam apenas em memória)
- [ ] Cadastro de fornecedores
- [ ] Prioridade na fila de reposição por criticidade (hoje a fila é FIFO simples)

## 12. Licença

Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo [`LICENSE`](./LICENSE) para mais informações.