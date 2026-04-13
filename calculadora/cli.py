from calculadora.error import ExpresionInvalida
from calculadora.expresion import evaluar

PROMPT = '> '
INTRO = """
============================================================
Calculadora Romana - REPL
============================================================
Ingrese expresiones aritmeticas con numeros romanos.
Ejemplos: "XIV + LX", "X - V", "MMM + D"
Escribe "salir" o "exit" para terminar.
============================================================
"""

def main() -> None:
    """Funcion principal del REPL de la calculadora."""
    print(INTRO)

    while True:
        try:
            # Leer entrada del usuario
            entrada = input(PROMPT).strip()

            # Verificar comandos de salida
            if not entrada or entrada.lower() in ('salir', 'exit', 'quit'):
                print('Adios!')
                break

            # Calcular resultado usando la funcion evaluar
            resultado = evaluar(entrada)
            print(f'Resultado: {resultado}')
            print()

        except ExpresionInvalida as e:
            print(f'Error: {e}')
            print()
        except (EOFError, KeyboardInterrupt):
            print('\nAdios!')
            break
        except Exception as e:
            print(f'Error inesperado: {e}')
            print()

if __name__ == "_main_":
    main()
