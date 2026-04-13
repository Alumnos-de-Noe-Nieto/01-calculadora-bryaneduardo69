


def validar_repeticiones_icxm(cadena: str) -> bool:
    # Pasamos todo a mayúsculas para que no falle por eso
    texto = cadena.upper()

    # Estos son los que no se valen en romano
    prohibidos = ["IIII", "XXXX", "CCCC", "MMMM"]

    # Revisamos si alguno de esos está en el texto
    return all(patron not in texto for patron in prohibidos)
