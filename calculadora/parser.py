from dataclasses import dataclass

from calculadora.error import ExpresionInvalida


@dataclass
class Token:
    tipo: str
    valor: str
    posicion: int

def evaluar_expresion(expresion: str) -> list[Token]:
    # Si la expresión está vacía o son solo espacios, regresamos lista vacía
    if not expresion or expresion.isspace():
        return []

    try:
        tokens = tokenizar_expresion(expresion)
        if not validar_estructura_tokens(tokens):
            raise ExpresionInvalida(f'La expresión "{expresion}" tiene una estructura inválida')
        return tokens
    except ExpresionInvalida as e:
        raise e

def tokenizar_expresion(expresion: str) -> list[Token]:
    tokens = []
    i = 0
    while i < len(expresion):
        char = expresion[i]

        if char == ' ':
            tokens.append(Token("ESPACIO", " ", i))
            i += 1
        elif char == '+':
            tokens.append(Token("SUMA", "+", i))
            i += 1
        elif char == '-':
            tokens.append(Token("RESTA", "-", i))
            i += 1
        elif char.upper() in 'IVXLCDM':
            inicio = i
            while i < len(expresion) and expresion[i].upper() in 'IVXLCDM':
                i += 1
            tokens.append(Token("ROMANO", expresion[inicio:i].upper(), inicio))
        else:
            raise ExpresionInvalida(f"Carácter inválido '{char}' en posición {i}")
    return tokens

def validar_estructura_tokens(tokens: list[Token]) -> bool:
    # Quitamos espacios para validar el orden
    filtrados = [t for t in tokens if t.tipo != 'ESPACIO']

    # REGLA DEL TEST 7.7: Si hay menos de 3 elementos (ej: solo un número), es inválido
    if len(filtrados) < 3:
        return False

    # Debe haber un número impar de tokens (Numero, Operador, Numero...)
    if len(filtrados) % 2 == 0:
        return False

    for i, token in enumerate(filtrados):
        if i % 2 == 0:  # Posiciones pares (0, 2...) DEBEN ser números
            if token.tipo != "ROMANO":
                return False
        else:           # Posiciones impares (1, 3...) DEBEN ser + o -
            if token.tipo not in ["SUMA", "RESTA"]:
                return False

    return True
