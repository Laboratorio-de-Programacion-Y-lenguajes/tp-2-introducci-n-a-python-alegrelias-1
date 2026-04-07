def crear_saludo(nombre: str) -> str:
    return f"Hola, {nombre}!"

def suma_enteros(a: int, b: int) -> int:
    return a + b

def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

def tipo_de_dato(valor) -> str:
    return type(valor).__name__

def convertir_a_float(valor: str) -> float:
    return float(valor)