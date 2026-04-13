def validar_restas(cadena: str) -> bool:
    valores = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    sustracciones_validas = {"IV", "IX", "XL", "XC", "CD", "CM"}

    texto = cadena.upper()

    for i in range(len(texto) - 1):
        actual = texto[i]
        siguiente = texto[i + 1]

        # Si detectamos una resta
        if valores[actual] < valores[siguiente]:
            pareja = actual + siguiente

            # 1. ¿Es una de las 6 permitidas?
            if pareja not in sustracciones_validas:
                return False

            # 2. ¿Hay una letra repetida antes de la resta? (Ej: IIV o XXC)
            if i > 0 and texto[i - 1] == actual:
                return False

    return True
