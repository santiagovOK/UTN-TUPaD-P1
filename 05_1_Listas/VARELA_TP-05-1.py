""" 

Trabajo práctico Nº5.1 - Listas -  Varela Santiago Octavio (Comisión 22)

Resolución del trabajo práctico Nº5 al 2025-04-28

Respuestas también en https://github.com/santiagovOK/UTN-TUPaD-P1/tree/main/05_1_Listas/VARELA_TP-05-1.ipynb

"""
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

# ---

# Creamos la variable multiplos_cuatro para almacenar el rango que nos pide la consigna
multiplos_cuatro = range(4,101,4)

# Creamos una segunda variable en donde pasaremos la variable anterior a tipo `list` 
multiplos_cuatro_lista= list(multiplos_cuatro)

# También podría almacenarse de la siguiente manera `multiplos_cuatro_lista = list(range(4, 101, 4))`

# Imprimimos la lista anteriormente almacenada en `multiplos_cuatro_lista`

print(multiplos_cuatro_lista)

# Imprimimos el detalle del tipo de dato que es `multiplos_cuatro_lista` para que se comprenda que es una lista
print("Tipo de dato de lo impreso en la línea anterior:")
print(type(multiplos_cuatro_lista))

# ---

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

# ---

# Creamos la variable `lista_frutas`, en donde almacenamos los elementos de la lista
lista_frutas = ["banana", "manzana", "naranja", "frutillas", "kiwi"]

# Imprimimos el penúltimo elemento de `lista_frutas` con la posición `[-2]`, que es la forma de indexing con números negativos que correspondería a la posición `[3]` en positivo en este caso
print(lista_frutas [-2])

# ---

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

# ---

# Creamos la variable `lista_vacía` que almacenará los elementos
lista_vacia = []

# Agregamos elementos a `lista_vacia` con `.append` (uno a la vez)
lista_vacia.append("Así")
lista_vacia.append("agrego")
lista_vacia.append("elementos")

# Imprimimos la `lista_vacia` con los elementos ya ingresados
print(lista_vacia)

# ---

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

# ---

# Creamos la variable `animales` para almacenar los elementos de la lista original
animales = ["perro", "gato", "conejo", "pez"]

# Imprimimos la lista original `animales` para mejor entendimiento en la salida
print("Lista original: ", animales)

# Cambiamos el segundo `[1]` y el último `[3]` elemento de la lista por los solicitados, pasando por las posiciones respectivas
animales[1] = "loro"
animales[3] = "oso"

# Imprimimos la lista modificada
print("Lista modificada: ", animales)

# ---

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)

# ---

""" 
El programa expuesto anteriormente, dentro de la consigna 5), contiene una variable `numeros` que almacena una lista de números en su primer línea y luego borra el número máximo de esa lista.

En la siguiente línea se realiza justamente ese proceso. Se llama a la variable `numeros` junto con la función `.remove` para borrar uno de los elementos y se ingresa como argumento `max(numeros)` para obtener el número máximo de la lista en `numeros`. Por lo tanto, es ese número máximo que ingresa como argumento para borrarse de la lista.

Al finalizar, se imprime con `print` la variable `numeros`,  que ya fue actualizada sin ese elemento eliminado, que corresponde al número `22`.

"""

# ---

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

# ---

# Creamos la variable `lista_en_cinco` que almacena la lista con el rango propuesto (similar a la consigna 1.)
lista_en_cinco = list(range(10, 31, 5))

# Imprimimos la lista completa
print("Lista completa:")
print(lista_en_cinco)

# Imprimimos los números que nos propone la consigna (los dos primeros)
print("Primeros dos números de la lista:")
print(lista_en_cinco[0], lista_en_cinco[1])

# Imprimimos el tipo de dato para hacer notar que es una lista y no otro
print("Tipo de dato de lo impreso en la línea anterior:")
print(type(lista_en_cinco))

# ---

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

# ---

# Creamos la variable `autos` para almacenar los elementos de la lista original
autos = ["sedan", "polo", "suran", "gol"]

# Imprimimos la lista original `autos` para referencia
print("Lista original: ", autos)

# Reemplazamos los valores de las posiciones `[0]` y `[1]`
autos[1] = "gris"
autos[2] = "oscuro"

# Imprimimos la lista modificada
print("Lista modificada: ", autos)

# ---

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

# ---

# Creamos la variable `dobles` como lista vacía
dobles = []

# Usamos `append` multiplicando(*) por 2 en cada caso para añadir el doble de cada número por cada elemento 
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

# Imprimimos la lista resultante
print(dobles)

# ---

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# a- Agregar "jugo" a la lista del tercer cliente usando append.
# b- Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c- Eliminar "pan" de la lista del primer cliente.
# d- Imprimir la lista resultante por pantalla

# ---

# Creamos la variable `compras` que incluirá la lista general y sus listas anidadas
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

# Añadimos "jugo" a la tercera lista anidada (posición [2]) - punto a)
compras[2].append("jugo")

# Imprimimos la lista anidada [2] para mostrar el cambio
print(compras[2])

# Cambiamos el elemento "fideos" `[1][1]` de la lista anidada `[1]` por "tallarines" - punto b)
compras[1][1] = "tallarines"

# Imprimimos la lista anidada con el cambio anterior
print(compras[1])

# Eliminamos "pan" de la lista anidada `[0]` del primer cliente
compras[0].remove("pan")

# Imprimimos la lista anidada `[0]`
print(compras[0])

# Imprimimos la lista final con todos los cambios en las listas anidadas
print("Lista final con todos los cambios en las compras de los clientes: ", compras)

# ---

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

# ---

# Creamos la variable `lista_anidada`
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# Imprimimos la `lista_anidada[0]` con el elemento `15`. Dado que es un solo elemento no es necesario anidar
print(lista_anidada[0])

# Imprimimos la `lista_anidada[1]` con el elemento `True`. Dado que es un solo elemento no es necesario anidar
print(lista_anidada[1])

# Imprimimos los diferentes elementos `[2][0]` , `[2][1]` , `[2][2]` de la `lista_anidada[2]`
print(lista_anidada[2][0])
print(lista_anidada[2][1])
print(lista_anidada[2][2])

# Imprimimos la `lista_anidada[2]` para mejor referencia de lo anterior
print(lista_anidada[2])

# Imprimimos la `lista_anidada[3]` con el elemento `False`. Dado que es un solo elemento no es necesario anidar
print(lista_anidada[3])
# ---