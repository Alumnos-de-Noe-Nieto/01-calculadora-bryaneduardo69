def validar_orden_descendente(cadena: str) -> bool:
    # 1. Valores de cada letra
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sustracciones_validas = {"IV", "IX", "XL", "XC", "CD", "CM"}

    texto = cadena.upper()
    i = 0
    ultimo_valor = 4000  # Mayor que M (1000)

    while i < len(texto):
        pareja = texto[i : i + 2]

        if len(pareja) == 2 and pareja in sustracciones_validas:
            valor_sustraccion = valores[pareja[1]] - valores[pareja[0]]

            if valor_sustraccion >= ultimo_valor:
                return False

            if i > 0 and texto[i - 1] == pareja[0]:
                return False

            ultimo_valor = valor_sustraccion
            i += 2
        else:
            valor_actual = valores[texto[i]]

            if valor_actual > ultimo_valor:
                return False

            ultimo_valor = valor_actual
            i += 1

    return True
