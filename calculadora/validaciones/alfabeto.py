def validar_simbolos(cadena: str) -> bool:
    texto = cadena.strip().upper()

    if not texto:
        return False

    alfabeto = "IVXLCDM"

    return all(letra in alfabeto for letra in texto)
