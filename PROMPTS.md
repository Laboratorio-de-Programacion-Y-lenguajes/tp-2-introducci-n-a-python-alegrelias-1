# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**:Gemini 

**Prompt usado**:
Quiero que completes cada una de las funciones sin implementar, presta atención a los comentarios dentro de las funciones y sigue sus instrucciones al pie de la letra, luego elimina los comentarios (ya sean comentarios con comillas o con numerales, deja el codigo limpio)
> 

**Resultado obtenido**:
```py
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
```

**¿Lo usaste tal cual o lo modificaste?**: No hice cambios

---

### 2 - condicionales.py

### Ejercicio 1: Clasificar Número (`evaluar_numero`)

**Herramienta**: Gemini

**Prompt usado**:
> Desde ahora, necesito que me hagas preguntas para realizar una función que clasifique un numero automaticamente. Cuando tengas suficiente información, crea un script en Python para realizar dicha tarea.

**Resultado obtenido**: Activación del patrón de Interacción Invertida. La IA generó preguntas de aclaración sobre los criterios matemáticos, el formato exacto del texto de retorno y el manejo del cero. Una vez respondidas las preguntas, se obtuvo el código exacto de la función `evaluar_numero(n: int) -> str` con la estructura `if/elif/else` necesaria.

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual.

---

### Ejercicio 1: Mayor de tres

**Herramienta**: Gemini

**Prompt usado**:
> Desde ahora, necesito que me hagas preguntas para realizar una función que calcule el mayor de tres números. Cuando tengas suficiente información, crea un script en Python para realizar dicha tarea.

**Resultado obtenido**: La IA solicitó confirmar los tipos de datos de las variables, el comportamiento esperado en caso de empate y si estaba permitido el uso de funciones nativas. Tras responder, devolvió la función `mayor_de_tres(a, b, c)` resuelta de manera óptima utilizando `max()`.

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual.

---

### Ejercicio 2: Clasificar Nota

**Herramienta**: Gemini

**Prompt usado**:
> Desde ahora, necesito que me hagas preguntas para realizar una función que clasifique una nota automaticamente. Cuando tengas suficiente información, crea un script en Python para realizar dicha tarea.

**Resultado obtenido**: La IA preguntó por la escala de notas válida, los textos exactos a retornar para cada rango y cómo manejar valores fuera de la escala. El resultado fue la función `clasificar_nota(nota: float) -> str` que evalúa los rangos solicitados y retorna un mensaje de error específico si el número no está entre 0 y 10.

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual.

---

### Ejercicio 3: Año Bisiesto

**Herramienta**: Gemini

**Prompt usado**:
> Desde ahora, necesito que me hagas preguntas para realizar una función que verifique si un año es o no bisiesto. Cuando tengas suficiente información, crea un script en Python para realizar dicha tarea.

**Resultado obtenido**: Consultas de la IA sobre la regla matemática a aplicar (estándar gregoriana) y el manejo de años inválidos. Se obtuvo la función `es_bisiesto(anio: int) -> bool` con la lógica matemática correcta y validaciones mediante el levantamiento de excepciones (`raise TypeError` y `raise ValueError`).

**¿Lo usaste tal cual o lo modificaste?**: Se usó tal cual.


---

### 3 - listas.py

**Herramienta**: Gemini

**Prompt usado**:
> Tengo que escribir una funciones en Python: que Dada una lista de listas, retorna todos los elementos en una sola lista. Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]. Mi lógica es utilizar el metodo chain() de python. [Requerimientos: anidamiento multinivel, elementos solos permitidos, sin librerías externas].

**Resultado obtenido**:
```python
def aplanar_lista(lista: list) -> list:
    resultado = []
    for elemento in lista:
        if isinstance(elemento, list):
            resultado.extend(aplanar_lista(elemento))
        else:
            resultado.append(elemento)
    return resultado
```
**¿Lo usaste tal cual o lo modificaste?**
Se usó tal cual. Se validó la inicialización del producto en 1 para evitar que el resultado fuera siempre 0.

PD: Habia mas prompts pero le pedi a la IA que olvide una solicitud que le hice y BORRO TODA LA CONVERSACION antes de esa solicitud.
---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
