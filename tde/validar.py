# ARQUIVO COM FUNÇÕES DE VALIDAÇÃO

# VALIDA O TEXTO DIGITADO
def validar_texto(valor):

    if not isinstance(valor, str):
        return False

    if not valor.strip():
        return False

    return True


# VALIDA O PREÇO
def validar_preco(valor):

    if not isinstance(valor, (int, float)) or isinstance(valor, bool):
        return False

    if valor < 0:
        return False

    return True


# VALIDA O ESTOQUE
def validar_estoque(valor):

    if not isinstance(valor, int) or isinstance(valor, bool):
        return False

    if valor < 0:
        return False

    return True


# VALIDA SE O ID ESTÁ DISPONÍVEL
def validar_id(med_id, lista_medicamentos):

    if not validar_texto(med_id):
        return False

    for medicamento in lista_medicamentos:

        if medicamento["id"] == med_id:
            return False

    return True


# VALIDA SE O NOME ESTÁ DISPONÍVEL
def validar_nome(med_nome, lista_medicamentos, ignorar_id=None):

    if not validar_texto(med_nome):
        return False

    for medicamento in lista_medicamentos:

        # Ignora o próprio medicamento durante uma alteração
        if medicamento["id"] == ignorar_id:
            continue

        if medicamento["medicamento"].strip().lower() == med_nome.strip().lower():
            return False

    return True


# VALIDA O DICIONÁRIO DE MEDICAMENTO
def validar_medicamento(medicamento, lista_medicamentos, ignorar_id=None):

    # Verifica se é um dicionário
    if not isinstance(medicamento, dict):
        return "Erro: os dados do medicamento devem estar em um dicionário."

    # Verifica os campos obrigatórios
    campos_obrigatorios = [
        "medicamento",
        "categoria",
        "estoque",
        "preco",
        "id"
    ]

    for campo in campos_obrigatorios:

        if campo not in medicamento:
            return f"Erro: o campo '{campo}' não foi informado."

    # Valida o nome
    if not validar_texto(medicamento["medicamento"]):
        return "Erro: o nome do medicamento não pode estar vazio."

    # Valida a categoria
    if not validar_texto(medicamento["categoria"]):
        return "Erro: a categoria não pode estar vazia."

    # Valida o estoque
    if not validar_estoque(medicamento["estoque"]):
        return "Erro: o estoque deve ser um número inteiro positivo ou zero."

    # Valida o preço
    if not validar_preco(medicamento["preco"]):
        return "Erro: o preço deve ser um número positivo ou zero."



    return True