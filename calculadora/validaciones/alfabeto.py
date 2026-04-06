def validar_simbolos(cadena: str) -> bool:
    # 1. Limpiar espacios laterales (Pista: .strip())
    limpia = cadena.strip().upper()
    
    # 2. Si queda vacía después de limpiar, es False
    if not limpia:
        return False
        
    # 3. Alfabeto permitido
    alfabeto = "IVXLCDM"
    
    # 4. Verificar cada letra
    for letra in limpia:
        if letra not in alfabeto:
            return False
            
    return True