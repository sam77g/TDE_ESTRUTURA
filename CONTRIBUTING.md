# Contribuindo com o PharmaERP

## Preparação
```bash
git clone <url-do-repositorio>
cd pharmaerp
python --version        # requer Python 3.10+
python main.py          # executar
python -m unittest discover -s tests -v   # testar
```
Não há dependências externas.

## Fluxo de branches
```
feature/<nome> -> develop -> main
```
- `main`: versão estável, sempre funcionando
- `develop`: integração das features
- `feature/<nome>`: uma funcionalidade por branch (ex.: `feature/vendas`, `feature/reposicao`)

Antes de abrir o merge:
```bash
git status
git diff
python -m unittest discover -s tests
```

## Padrão de commits
Formato: `tipo(escopo): descrição curta no imperativo`

| Tipo | Uso |
|---|---|
| `feat` | nova funcionalidade |
| `fix` | correção de bug |
| `refactor` | mudança de código sem alterar comportamento |
| `test` | testes |
| `docs` | documentação |
| `chore` | tarefas gerais (config, limpeza) |

Escopos: `core`, `medicamentos`, `estoque`, `balcao`, `vendas`, `reposicao`, `main`.

Exemplos:
```
feat(vendas): adiciona venda com baixa no balcao
fix(reposicao): evita pedido duplicado para o mesmo medicamento
docs: atualiza README com regras de negocio
```
Um commit = uma mudança lógica. Use o corpo da mensagem (lista com `-`) para detalhes.

## Padrões de código
- **Um modelo de dados:** medicamento = `id`, `medicamento`, `categoria`, `preco`, `estoque_central`, `estoque_balcao`. Nunca usar `"nome"` nem chaves com acento.
- **Validação só em `validar.py`:** não repetir `if preco <= 0` pelo projeto. Entrada do usuário via `ler_inteiro` / `ler_decimal`.
- **Sem `print()` na lógica:** funções de regra retornam `(ok, mensagem)` ou lista de mensagens; quem imprime é o menu.
- **Movimentação de unidades:** estoque → balcão somente por `transferir_estoque_balcao()`. Nunca alterar `estoque_central`/`estoque_balcao` direto fora das funções de regra.
- **Reposição:** criar/cancelar pedidos somente por `sincronizar_reposicao()`; atender somente por `processar_fila()`.
- **Constantes:** `LIMITE_BALCAO` e `LOTE_REPOSICAO` ficam em `estruturas.py`.
- **Mensagens:** `[✓]` sucesso, `[!]` aviso, `[X]` erro (helpers `msg_ok`, `msg_aviso`, `msg_erro`).
- **Nomes:** funções e variáveis em `snake_case`, em português, como no restante do projeto.
- **Fora do escopo:** fornecedores, login, banco de dados, interface gráfica, API, POO complexa, framework, financeiro completo.

## Testes
Toda mudança de regra precisa de teste em `tests/test_cenarios.py`. Cobrir o caminho normal e o de erro (quantidade inválida, medicamento inexistente, estoque insuficiente/zerado).

## Checklist antes do commit
- [ ] Testes passando
- [ ] Sem `None` inesperado, `KeyError` ou `ValueError` em entradas inválidas
- [ ] Estoque nunca negativo; sem reposição duplicada
- [ ] Sem imports não usados nem código duplicado
- [ ] README atualizado, se a regra de negócio mudou
- [ ] Mensagem de commit no padrão
