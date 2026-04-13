from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida
from calculadora.parser import evaluar_expresion as parsear_expresion


def evaluar(expresion: str) -> int:
    tokens = parsear_expresion(expresion)
    tokens_utiles = [t for t in tokens if t.tipo != 'ESPACIO']

    if not tokens_utiles:
        raise ExpresionInvalida("La expresion esta vacia")

    resultado = romano_a_entero(tokens_utiles[0].valor)

    for i in range(1, len(tokens_utiles), 2):
        operador = tokens_utiles[i].tipo
        valor_entero = romano_a_entero(tokens_utiles[i+1].valor)

        if operador == 'SUMA':
            resultado += valor_entero
        elif operador == 'RESTA':
            resultado -= valor_entero

    if resultado <= 0:
        raise ExpresionInvalida(f"Resultado invalido ({resultado})")

    return resultado
