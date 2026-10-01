# ARQUIVO COM FUNÇÕES DE VALIDAÇAO

def validar_texto(valor):
    if not isinstance(valor, str): # valida se é string
        return False

    if not valor.strip(): # valida se é vazio
        return False

    return True

def validar_preco(valor):
    if not isinstance(valor, (int, float)) or isinstance(valor, bool): # valida se é int ou float (se é realmente um número)
        return False

    if valor < 0: # valida se p valor é negativo
        return False

    return True

def validar_estoque(valor):
    if not isinstance(valor, int) or isinstance(valor, bool): # valida o tipo de valor  digitado
        return False

    if valor < 0: # valida se é nagativo
        return False

    return True
        