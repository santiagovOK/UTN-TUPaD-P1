""" 

Trabajo práctico Nº5.1 - Listas -  Varela Santiago Octavio (Comisión 22)

Resolución del trabajo práctico Nº5 al 2025-04-27

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

# ---

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

# ---

# ---

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

# ---

# ---

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# a- Agregar "jugo" a la lista del tercer cliente usando append.
# b- Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c- Eliminar "pan" de la lista del primer cliente.
# d- Imprimir la lista resultante por pantalla

# ---

# ---

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.