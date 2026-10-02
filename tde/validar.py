# ARQUIVO COM FUNÇÕES DE VALIDAÇÃO E LEITURA SEGURA DE ENTRADA


# ===== VALIDAÇÕES =====
def validar_texto(valor):
    return isinstance(valor, str) and bool(valor.strip())


def validar_preco(valor):
    if not isinstance(valor, (int, float)) or isinstance(valor, bool):
        return False
    return valor >= 0


def validar_estoque(valor):
    """Inteiro >= 0 (estoque pode ser zero)."""
    if not isinstance(valor, int) or isinstance(valor, bool):
        return False
    return valor >= 0


def validar_quantidade(valor):
    """Inteiro > 0 (quantidade de uma operação: venda, transferência, entrada)."""
    if not isinstance(valor, int) or isinstance(valor, bool):
        return False
    return valor > 0


def validar_id(med_id, lista_medicamentos):
    """ID inteiro positivo que ainda não esteja em uso."""
    if not isinstance(med_id, int) or isinstance(med_id, bool) or med_id <= 0:
        return False
    return all(m["id"] != med_id for m in lista_medicamentos)


def validar_nome(med_nome, lista_medicamentos, ignorar_id=None):
    """Nome não vazio e ainda não cadastrado (ignora o próprio em alterações)."""
    if not validar_texto(med_nome):
        return False
    for medicamento in lista_medicamentos:
        if ignorar_id is not None and medicamento["id"] == ignorar_id:
            continue
        if medicamento["medicamento"].strip().lower() == med_nome.strip().lower():
            return False
    return True


def validar_medicamento(medicamento, lista_medicamentos, ignorar_id=None):
    """Retorna True se válido; senão, a mensagem de erro. (O ID é gerado depois.)"""
    if not isinstance(medicamento, dict):
        return "Erro: os dados do medicamento devem estar em um dicionário."

    for campo in ("medicamento", "categoria", "estoque_central", "estoque_balcao", "preco"):
        if campo not in medicamento:
            return f"Erro: o campo '{campo}' não foi informado."

    if not validar_texto(medicamento["medicamento"]):
        return "Erro: o nome do medicamento não pode estar vazio."
    if not validar_nome(medicamento["medicamento"], lista_medicamentos, ignorar_id):
        return "Erro: já existe um medicamento com esse nome."
    if not validar_texto(medicamento["categoria"]):
        return "Erro: a categoria não pode estar vazia."
    if not validar_estoque(medicamento["estoque_central"]):
        return "Erro: o estoque central deve ser um número inteiro maior ou igual a zero."
    if not validar_estoque(medicamento["estoque_balcao"]):
        return "Erro: o estoque do balcão deve ser um número inteiro maior ou igual a zero."
    if not validar_preco(medicamento["preco"]):
        return "Erro: o preço deve ser um número maior ou igual a zero."
    return True


# ===== LEITURA SEGURA (nunca levanta ValueError) =====
def ler_inteiro(mensagem, minimo=None):
    while True:
        try:
            valor = int(input(mensagem).strip())
        except ValueError:
            print("[X] Digite apenas números inteiros.")
            continue
        if minimo is not None and valor < minimo:
            print(f"[X] O valor deve ser maior ou igual a {minimo}.")
            continue
        return valor


def ler_decimal(mensagem, minimo=None):
    while True:
        try:
            valor = float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("[X] Digite um número válido (ex.: 12.50).")
            continue
        if minimo is not None and valor < minimo:
            print(f"[X] O valor deve ser maior ou igual a {minimo}.")
            continue
        return valor
