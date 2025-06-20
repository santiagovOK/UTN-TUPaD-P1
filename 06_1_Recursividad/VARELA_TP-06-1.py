# Trabajo práctico Nº7 - Recursividad -  Varela Santiago Octavio (Comisión 22)

# Resolución del trabajo práctico Nº7 al 2025-05-26

# Respuestas también en https://github.com/santiagovOK/UTN-TUPaD-P1/tree/main/06_1_Recursividad/VARELA_TP-06-1.ipynb

# ----------------------------------------------------------------------

"""
1. Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario.

"""

# ----------------------------------------------------------------------

# Utilizamos la función recursiva para calcular el factorial de un número. Similar a uno de los ejemplos vistos en las actividades de esta unidad

def factorial_recur(x):
    if x == 0:
        return 1
    else:
        return x * factorial_recur(x - 1)

# Creamos una variable que almacenará el número ingresado por el usuario
num_usuario = int(input("Ingrese un número: "))

# Creamos una estructura condicional para verificar si el número ingresado es negativo, cero o positivo
if num_usuario < 0:
    print("El factorial no está definido para números negativos.")
elif num_usuario == 0:
    print("El factorial de 0 es 1.")   
# Si el número es positivo, calculamos el factorial de todos los números enteros entre 1 y el número ingresado
else:
    print(f"Ingresaste {num_usuario}")
    print(f"Calculemos los factoriales de los números enteros entre 1 y {num_usuario}...")
    # Utilizamos un bucle for para iterar sobre los números enteros entre 1 y el número ingresado
    for i in range(1, num_usuario + 1):
        print(f"El factorial de {i} es {factorial_recur(i)}")


# ----------------------------------------------------------------------

"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

"""

# ----------------------------------------------------------------------

# Definimos la función recursiva para calcular el valor de la serie de Fibonacci en una posición específica, similar a uno de los ejemplos vistos en las actividades

def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

# Le solicitamos al usuario que ingrese la posición de la serie de Fibonacci que desea calcular
pos_usuario = int(input("Ingrese la posición de la serie de Fibonacci que desea calcular: "))

# Creamos una condición para verificar que la posición ingresada sea un número entero no negativo, en donde también irá el bucle for para mostrar la serie completa hasta la posición elegida por el usuario
if pos_usuario < 0:
    print("La posición debe ser un número entero no negativo.")
# Caso positivo
else:
    print(f"La posición elegida por el usuario es: {pos_usuario}")
    print("Serie de Fibonacci completa hasta la posición elegida", pos_usuario, ":")
    # Bucle for para mostrar la serie completa hasta la posición elegida por el usuario, utilizando la función recursiva definida anteriormente.
    for i in range(pos_usuario + 1):
        print(fibonacci_recursivo(i))

# ----------------------------------------------------------------------

"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula n^m = n ∗ n^(m−1). Prueba esta función en un algoritmo general.
"""

# ----------------------------------------------------------------------

# Creamos la función recursiva para calcular la potencia de un número base elevado a un exponente
def potencia_recursiva(base, exponente):
    if exponente == 0: # Caso base
        return 1
    elif exponente < 0: # Caso para exponentes negativos
        return 1 / potencia_recursiva(base, -exponente)
    else:
        return base * potencia_recursiva(base, exponente - 1) # Llamada recursiva
    
# Programa principal - Probamos la función recursiva `potencia_recursiva`

# Le solicitamos al usuario que ingresa una base y su exponente
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Mostramos el resultado de la potencia, ingresando como argumentos la base y el exponente a la `potencia_recursiva`

print(f"{base} elevado a la {exponente} es igual a {potencia_recursiva(base, exponente)}")


# ----------------------------------------------------------------------

"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
"""

# ----------------------------------------------------------------------

def decimal_a_binario(numero):

    # Almacenamos el residuo de la división del número por 2 en `residuo`
    residuo = numero % 2

    # Establecemos el caso base: si el número es 0 o 1, devolvemos su representación en binario como cadena de texto
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    # En el último caso, llamamos a la función recursivamente con el cociente de la división del número por 2, y concatenamos el residuo como cadena de texto
    else:
        # Almacenamos el resultado de la llamada recursiva en `resultado` para poder imprimir el paso a paso de la recursividad.
        resultado = decimal_a_binario(numero // 2) + str(residuo)
        print(f"decimal_a_binario({numero}) = {resultado}")        
        return resultado

print((decimal_a_binario(10)))  # Salida esperada: 1010 ; si se usa `type` es posible ver que el resultado final es una cadena (str)

# ----------------------------------------------------------------------

"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
"""

#----------------------------------------------------------------------

def es_palindromo(palabra):
    # Caso base: una palabra de longitud 0 o 1 es un palíndromo por definición
    if len(palabra) <= 1:
        print("\nCaso base: la palabra es un palíndromo - Entonces...")
        return True
    # Comparamos los extremos. Si son diferentes, no es un palíndromo por definición
    elif palabra[0] != palabra[-1]:
        print("\nLos extremos son diferentes - Entonces...")
        return False
    # Establecemos el caso recursivo: si los extremos son iguales, llamamos a la función con la palabra sin los extremos hasta el caso base (longitud 0 o 1)
    else:
        print(f"{palabra}") # Imprimimos el paso a paso de la recursividad
        resultado = es_palindromo(palabra[1:-1])
        return resultado # Devolvemos el resultado final de la llamada recursiva

print(es_palindromo("radar"))  # Salida esperada: True
print("\n")
print(es_palindromo("reconocer")) # Salida esperada: True
print("\n")
print(es_palindromo("hola"))  # Salida esperada: False

#----------------------------------------------------------------------

"""
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.

Restricciones:

No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.

Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
"""

# ----------------------------------------------------------------------

def suma_digitos(n):
    if n == 0: # Establecemos el caso base: si n es 0, la suma de los dígitos es 0.
        return 0
    else:
        print(f"Actual iteración `n`:{n}") # Imprimimos el valor actual de n para ver cómo cambia en cada iteración.
        return n % 10 + suma_digitos(n // 10) # Sumamos el último dígito de n (n % 10) y llamamos recursivamente a la función con el resto de los dígitos (n // 10).

# Imprimimos los resultados de las pruebas para verificar que la función funciona correctamente.
print(suma_digitos(1234)) # Output: 10
print("\n")
print(suma_digitos(321)) # Output: 6
print("\n")
print(suma_digitos(305)) # Output: 8

# ----------------------------------------------------------------------


"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.

Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.

Ejemplos:
contar_bloques(1) → 1
(1)
contar_bloques(2) → 3
(2 + 1)
contar_bloques(4) → 10
(4 + 3 + 2 + 1)

"""
# ----------------------------------------------------------------------

def contar_bloques(n):
    if n == 1: # Establecemos el caso base: si n es 1, el número de bloques es 1.
        print(f"Actual iteración `n`:{n}") # Imprimimos el valor actual de n para ver cómo cambia en cada iteración (en este caso, solo se imprime una vez, cuando se llega al caso base).
        return 1
    else:
        print(f"Actual iteración `n`:{n}") # Imprimimos el valor actual de n para ver cómo cambia en cada iteración.
        return n + contar_bloques(n - 1) # Sumamos el número de bloques en el nivel actual (n) y llamamos recursivamente a la función con el nivel anterior (n - 1).
# Imprimimos los resultados de las pruebas para verificar que la función funciona correctamente.

print(contar_bloques(1)) # Output: 1
print("\n")
print(contar_bloques(2)) # Output: 3
print("\n")
print(contar_bloques(4)) # Output: 10

# ----------------------------------------------------------------------


"""
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.

Ejemplos:

contar_digito(12233421, 2) → 3
contar_digito(5555, 5) →4
contar_digito(123456, 7) →0
"""

# ----------------------------------------------------------------------

def contar_digito(numero, digito):
    if numero == 0: # Establecemos el caso base: si numero es 0, el dígito no aparece en el número.
        return 0
    else:
        print(f"Actual iteración `numero`:{numero}") # Imprimimos el valor actual de numero para ver cómo cambia en cada iteración.
        
        # Si el último dígito de numero es igual al dígito buscado, sumamos 1 y llamamos recursivamente a la función con el resto de los dígitos.
        
        if numero % 10 == digito: 
            return 1 + contar_digito(numero // 10, digito)
        else:
            
        # Si el último dígito de numero no es igual al dígito buscado, llamamos recursivamente a la función con el resto de los dígitos para seguir contando.
            return contar_digito(numero // 10, digito)

# Imprimimos los resultados de las pruebas para verificar que la función funciona correctamente.

print(contar_digito(12233421, 2)) # Output: 3
print("\n")
print(contar_digito(5555, 5)) # Output: 4
print("\n")
print(contar_digito(123456, 7)) # Output: 0

# ----------------------------------------------------------------------
