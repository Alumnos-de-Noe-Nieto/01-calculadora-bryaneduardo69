

def validar_repeticiones_vld(cadena: str) -> bool:
    texto = cadena.upper()

    # Estos NO se pueden repetir ni una vez
    prohibidos = ["VV", "LL", "DD"]

    return all(patron not in texto for patron in prohibidos)
