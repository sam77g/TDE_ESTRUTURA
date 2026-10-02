# PharmaERP

Sistema de controle de farmácia em Python (terminal) — TDE de Estruturas Lineares e Algoritmos.

## 1. Objetivo
Controlar medicamentos, estoque central, balcão, vendas e reposição automática.

## 2. Problema
Evitar que o balcão fique sem produto: toda venda que deixa o balcão abaixo de **15 unidades** gera um pedido de reposição, atendido a partir do estoque central.

## 3. Funcionalidades
- Medicamentos: cadastrar, alterar, remover (em cascata), listar, buscar e listar por categoria
- Estoque central: listar, buscar, entrada e ajuste
- Balcão: listar, consultar e transferir estoque → balcão
- Vendas: baixa no balcão com total e histórico
- Reposição: fila de pedidos com criticidade e processamento
- Histórico de movimentações (entrada, saída, transferência, venda, ajuste)

## 4. Estruturas utilizadas
| Estrutura | Onde | Por quê |
|---|---|---|
| Lista | `medicamentos` | percorrer, buscar, alterar e remover cadastros |
| Fila (`deque`) | `fila_reposicao` | FIFO: o primeiro pedido é o primeiro atendido |
| Pilha (`list`) | `historico` | `append` empilha; o histórico é lido do topo (mais recente) |

## 5. Algoritmos
```
Venda -> baixa o balcão -> balcão < 15? -> cria pedido -> entra na fila
Processar fila (FIFO): retira o primeiro pedido
  balcão já >= 15      -> descarta
  estoque central = 0  -> continua pendente
  senão                -> transfere min(30, estoque central) para o balcão
```

## 6. Organização
| Arquivo | Responsabilidade |
|---|---|
| `main.py` | menu principal |
| `estruturas.py` | estruturas, constantes, IDs, buscas e mensagens |
| `validar.py` | validações e leitura segura de entrada |
| `medicamentos.py` | CRUD de medicamentos |
| `estoque.py` | estoque central |
| `balcao.py` | balcão e `transferir_estoque_balcao` |
| `vendas.py` | vendas |
| `reposicao.py` | fila, criticidade e processamento |
| `relatorios.py` | histórico |
| `tests/test_cenarios.py` | testes |

## 7. Regras de negócio
- Limite do balcão: **15** (abaixo disso → reposição)
- Lote de reposição/distribuição inicial: **30** (ou o que houver no estoque)
- Criticidade: `>=15` NORMAL · `10–14` AVISO · `5–9` ALERTA · `<5` CRÍTICO
- Estoque insuficiente: transfere o que houver; nunca fica negativo
- Estoque zerado: pedido fica pendente e é atendido após nova entrada de estoque
- Pedido duplicado não é criado; pedido obsoleto (balcão normalizado) é cancelado

## Como executar
```
python main.py
python -m unittest discover -s tests -v
```
Requer Python 3.10+.
