from calculadora.error import ExpresionInvalida
from calculadora.validaciones.alfabeto import validar_simbolos
from calculadora.validaciones.orden_descendente import validar_orden_descendente
from calculadora.validaciones.repeticiones_icxm import validar_repeticiones_icxm
from calculadora.validaciones.repeticiones_vld import validar_repeticiones_vld
from calculadora.validaciones.restas import validar_restas


def romano_a_entero(cadena: str) -> int:
    # 1. VALIDACIONE
    if not validar_simbolos(cadena):
        raise ExpresionInvalida("Símbolos inválidos")
    if not validar_repeticiones_icxm(cadena):
        raise ExpresionInvalida("Repetición inválida de I/X/C/M")
    if not validar_repeticiones_vld(cadena):
        raise ExpresionInvalida("Repetición inválida de V/L/D")
    if not validar_restas(cadena):
        raise ExpresionInvalida("Resta inválida")
    if not validar_orden_descendente(cadena):
        raise ExpresionInvalida("Orden incorrecto")

    # 2. CONVERTIR
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    texto = cadena.upper()
    total = 0

    for i in range(len(texto)):
        valor_actual = valores[texto[i]]

        if i + 1 < len(texto) and valores[texto[i + 1]] > valor_actual:
            total -= valor_actual
        else:
            total += valor_actual

    return total
