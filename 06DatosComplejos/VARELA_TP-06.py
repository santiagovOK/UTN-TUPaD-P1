# Trabajo práctico Nº6 - Estructuras de datos complejas -  Varela Santiago Octavio (Comisión 22)

# Resolución del trabajo práctico Nº6 al 2025-06-23

# Respuestas también en https://github.com/santiagovOK/UTN-TUPaD-P1/tree/main/06DatosComplejos/VARELA_TP-06.ipynb

# ----------------------------------------------------------------------

# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las siguientes frutas con sus respectivos precios:
# ●​ Naranja = 1200
# ●​ Manzana = 1500
# ●​ Pera = 2300

# ----------------------------------------------------------------------

# Establecemos el diccionario con los precios de las frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadimos nuevas llaves y valores al diccionario según el enunciado
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})

# Imprimimos el diccionario actualizado
print(precios_frutas)

# ----------------------------------------------------------------------

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ●​ Banana = 1330
# ●​ Manzana = 1700
# ●​ Melón = 2800

# ----------------------------------------------------------------------

# Establecemos el diccionario con los precios de las frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadimos nuevas llaves y valores al diccionario según el enunciado
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})

# Imprimimos el diccionario actualizado
print(f"Precio luego de añadir las nuevas frutas: {precios_frutas}")

# Actualizamos los precios de las frutas según el enunciado 2) usando el método update(). Es lo mismo que hacer precios_frutas['Banana'] = 1330 , etc. pero más eficiente para actualizar varios valores a la vez.

precios_frutas.update({'Banana': 1330, 'Manzana':1700, 'Melón': 2800})

# Imprimimos el diccionario actualizado
print(f"\nPrecio luego de actualizar los precios de las frutas según enunciado 2): {precios_frutas}")

# ----------------------------------------------------------------------

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

# ----------------------------------------------------------------------

# Establecemos el diccionario con los precios de las frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadimos nuevas llaves y valores al diccionario según el enunciado
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})

# Imprimimos el diccionario actualizado
print(f"Precio luego de añadir las nuevas frutas: {precios_frutas}")

# Actualizamos los precios de las frutas según el enunciado 2) usando el método update(). Es lo mismo que hacer precios_frutas['Banana'] = 1330 , etc. pero más eficiente para actualizar varios valores a la vez.


precios_frutas.update({'Banana': 1330, 'Manzana':1700, 'Melón': 2800})

print(f"\nPrecio luego de actualizar los precios de las frutas según enunciado 2): {precios_frutas}")

# Creamos una lista con los nombres de las frutas

frutas = list(precios_frutas.keys())

# Imprimimos la lista de frutas, que solo contiene los nombres de las frutas

print(f"\nLista de frutas: {frutas} que es de tipo '{type(frutas)}'")

# ----------------------------------------------------------------------

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# •Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# •Luego, pedí un nombre y mostrale el número asociado, si existe. Ejemplo (ver en PDF)

# ----------------------------------------------------------------------

# Creamos un diccionario vacío para almacenar los contactos
contactos = {}


print("Cargá 5 contactos con su número telefónico:")

# Cargamos los 5 contactos usando un bucle `for`

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    telefono = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = telefono

# Mostramos todos los contactos ingresados yendo item por item del diccionario

print("\nLista de contactos cargados:")

for contacto, telefono in contactos.items():
    print(f"Contacto: {contacto}, Teléfono: {telefono}")

# Agregamos la posibilidad de consultar un número por nombre

consulta = input("\nIngresá el nombre que querés buscar: ")

# Verificamos si el contacto existe en el diccionario y mostramos el número correspondiente
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró el contacto '{consulta}'.")

# ----------------------------------------------------------------------

# 5) Solicita al usuario una frase e imprime:
# •Las palabras únicas (usando un set).
# •Un diccionario con la cantidad de veces que aparece cada palabra. Ejemplo (ver en PDF)


# ----------------------------------------------------------------------


# ----------------------------------------------------------------------

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno. Ejemplo (ver en PDF)

# ----------------------------------------------------------------------


# ----------------------------------------------------------------------


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:

# •Mostrá los que aprobaron ambos parciales.
# •Mostrá los que aprobaron solo uno de los dos.
# •Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


# ----------------------------------------------------------------------


# ----------------------------------------------------------------------

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# •Consultar el stock de un producto ingresado.
# •Agregar unidades al stock si el producto ya existe.
# •Agregar un nuevo producto si no existe.


# ----------------------------------------------------------------------


# ----------------------------------------------------------------------


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

# Ejemplo (ver en PDF)

# Permití consultar qué actividad hay en cierto día y hora.


# ----------------------------------------------------------------------


# ----------------------------------------------------------------------


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# •Las capitales sean las claves.
# •Los países sean los valores. Ejemplo (ver en PDF)


# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
