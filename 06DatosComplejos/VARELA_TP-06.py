# Trabajo práctico Nº6 - Estructuras de datos complejas -  Varela Santiago Octavio (Comisión 22)

# Resolución del trabajo práctico Nº6 al 2025-06-21

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

# Solicitamos una frase al usuario
frase = input("Introduce una frase: ")

# Separamos las palabras con split()
palabras = frase.split() 
# Creamos un set para las palabras únicas y un diccionario para contar las apariciones
palabras_unicas = set(palabras)
# Creamos un diccionario para contar las apariciones de cada palabra
contador_palabras = {}

# Contamos las apariciones de cada palabra con un bucle `for`
for palabra in palabras:
    # Si la palabra ya está en el diccionario, incrementamos su contador
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    # Si no está, la añadimos con un contador inicial de 1
    else:
        contador_palabras[palabra] = 1

# Imprimimos los resultados
print("Palabras únicas:", palabras_unicas)
print("Cantidad de veces que aparece cada palabra:", contador_palabras)

# ----------------------------------------------------------------------

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno. Ejemplo (ver en PDF)

# ----------------------------------------------------------------------

# Creamos un diccionario para almacenar los alumnos y sus notas
alumnos = {}

# Recolectamos datos de los 3 alumnos con un bucle `for` que itera 3 veces
for i in range(3):
    # Almacenamos el nombre del alumno y sumamos 1 al contador
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    # Almacenamos las notas como una tupla de enteros, separadas por espacios con `map` y split()
    notas = tuple(map(int, input(f"Ingrese las 3 notas de {nombre}, separadas por espacios: ").split()))
    # Verificamos que se hayan ingresado exactamente 3 notas
    alumnos[nombre] = notas

# Mostramos los promedios de cada alumno, que se calcularán sumando las notas y dividiendo por la cantidad de notas en cada caso
print("\n--- Promedios ---")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}") # 2f es para mostrar 2 decimales

# ----------------------------------------------------------------------


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:

# •Mostrá los que aprobaron ambos parciales.
# •Mostrá los que aprobaron solo uno de los dos.
# •Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


# ----------------------------------------------------------------------

# Definimos los sets de estudiantes aprobados en cada parcial
parcial1 = {"Ana", "Luis", "Pedro", "María"}
parcial2 = {"Pedro", "María", "Sofía", "Tomás"}

# Definimos los estudiantes que aprobaron ambos parciales con la intersección de ambos conjuntos (usado en matemática para el integrador)
ambos = parcial1 & parcial2 # también se puede usar .intersection()

# Definimos los estudiantes que aprobaron solo uno de los dos con la diferencia simétrica de ambos conjuntos (usado en matemática para el integrador)
solo_uno = parcial1 ^ parcial2  # también se puede usar .symmetric_difference()

# Definimos los estudiantes que aprobaron al menos uno de los parciales con la unión de ambos conjuntos (usado en matemática para el integrador)
al_menos_uno = parcial1 | parcial2  # también se puede usar .union()

# Mostramos los resultados
print(f"\nAprobados en ambos parciales: {ambos}")
print(f"\nAprobados sólo en uno de los parciales: {solo_uno}")
print(f"\nTotal de estudiantes que aprobaron al menos un parcial: {al_menos_uno}\n")

# ----------------------------------------------------------------------

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# •Consultar el stock de un producto ingresado.
# •Agregar unidades al stock si el producto ya existe.
# •Agregar un nuevo producto si no existe.


# ----------------------------------------------------------------------

# Creamos el diccionario de productos y stock para ya comenzar con algunos valores en el inventario.
stock = {
    "pan": 10,
    "leche": 5,
    "huevos": 12
}

bandera = True
# Creamos un bucle `while` para mostrar el menú y permitir al usuario interactuar con el inventario.

while bandera:
    # Mostramos el menú de opciones al usuario.
    print("\n--- Menú ---")
    print("1. Consultar stock (por producto)")
    print("2. Agregar unidades al stock")
    print("3. Agregar nuevo producto")
    print("4. Ver stock actual en general")
    print("5. Salir")

    # Pedimos al usuario que seleccione una opción que se almacenará en `opción`
    opcion = input("Seleccioná una opción (1-5): ")

    # Usamos estructuras condicionales para manejar cada opción del menú
    if opcion == "1":
        producto = input("Ingresá el nombre del producto: ").lower() # usamos `.lower()` para evitar problemas con mayúsculas y minúsculas.
        # Verificamos si el producto está en el inventario o no con otra estructura condicional anidada
        if producto in stock:
            print(f"Stock de {producto}: {stock[producto]}")
        else:
            print("El producto no está en el inventario.")

    elif opcion == "2":
        producto = input("Ingresá el nombre del producto: ").lower()
        # Verificamos si el producto está en el inventario o no con otra estructura condicional anidada
        if producto in stock:
            # Esta vez pedimos la cantidad de unidades a agregar
            cantidad = int(input(f"¿Cuántas unidades agregar a {producto}? "))
            # Actualizamos el stock del producto
            stock[producto] += cantidad
            print(f"Ahora hay {stock[producto]} unidades de {producto}.")
        else:
            print("El producto no existe. Use la opción 3 para agregarlo.")

    elif opcion == "3":
        # Le damos la opción al usuario de agregar un nuevo producto al inventario
        producto = input("Ingresá el nuevo producto: ").lower()
        # Verificamos si el producto está en el inventario o no con otra estructura condicional anidada
        if producto not in stock:
            # Pedimos la cantidad inicial del producto si no está en stock
            cantidad = int(input("Ingresá la cantidad inicial: "))
            # Agregamos el producto al inventario con su cantidad
            stock[producto] = cantidad
            print(f"Producto {producto} agregado con {cantidad} unidades.")
        else:
            print("ℹEl producto ya existe. Usá la opción 2 para agregar unidades.")

    elif opcion == "4":
        # Mostramos el stock actual
        print("\n--- Stock Actual ---")
        for producto, cantidad in stock.items(): # Iteramos sobre el diccionario con items()
            print(f"{producto}: {cantidad}")

    elif opcion == "5":
        # Finalizamos el programa cambiando `bandera` a `False`
        print("Programa finalizado.")
        bandera = False
    else:
        print("Opción inválida.")


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
