# Trabajo práctico Nº3 - Estructuras condicionales -  Varela Santiago Octavio (Comisión 22)

# Resolución del trabajo práctico Nº3 al 2025-04-02

# Respuestas también en https://github.com/santiagovOK/UTN-TUPaD-P1/blob/main/03EstructurasCondicionales/VARELA_TP-03.ipynb

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# ---

# Le solicitamos su edad al usuario y creamos una variable para albergar la edad límite de mayoría de edad (18, edad_adulto)
edad_usuario = int(input("Ingresá tu edad"))
edad_adulto = 18

# Iniciamos la condición, teniendo que ser la edad del usuario mayor (la consigna no dice mayor o igual) a 18 para imprimir el mensaje
if edad_usuario > edad_adulto:
    print("Es mayor de edad")
else:
    print("Es menor de edad.") # Mensaje que se imprimi si la edad del usuario no es más que 18.

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# Le solicitamos su nota al usuario y creamos una variable que almacene la nota límite de aprobación (nota_aprobar)
nota_usuario = float(input("Ingresá tu nota"))
nota_aprobar = 6

# Iniciamos la estructura condicional. 
# Si la nota del usuario (nota_usuario) es mayor o igual (>=) que la nota de aprobación (nota_aprobar), se imprimirá "Aprobado"
if nota_usuario >= nota_aprobar:
    print("Aprobado")
else:
    print("Desaprobado") # De lo contrario, se imprimirá "Desaprobado"

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# ---

# Le solicitamos al usuario que ingrese un número
num_ingresado = int(input("Ingresá un número entero:"))

# Iniciamos la estructura condicional. 
# Sí el número del usuario es par (módulo, dividido 2 da resto 0) se imprime el mensaje "Ha ingresado un número par."
if num_ingresado % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.") # En otro caso, se imprime "Por favor, ingrese un número par"

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ●​ Niño/a: menor de 12 años. ●​ Adolescente: mayor o igual que 12 años y menor que 18 años. ●​ Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ●​ Adulto/a: mayor o igual que 30 años.

# ---

# Le solicitamos la edad al usuario
edad_usuario = int(input("Ingrese su edad:"))

# Definimos los rangos de edades para cada categoría
rango_nino = range(0, 12)
rango_adolescente = range(12, 18)
rango_adulto_joven = range(18, 30)

# Verificamos en qué rango se encuentra la edad del usuario, según los establecidos en el paso anterior

if edad_usuario in rango_adolescente:
    print("Usted es un adolescente.") # Se imprime "Usted es un adolescente." si edad_usuario está dentro de rango_adolescente
elif edad_usuario in rango_nino:
    print("Usted es un niño/a.") # Se irmprime "Usted es un niño/a." si edad_usuario está dentro de rango_nino
elif edad_usuario in rango_adulto_joven:
    print("Usted es un adulto joven.") # Se imprime "Usted es un adulto joven." si edad_usuario esta dentro de rango_adulto_joven
else:
    print("Usted es un adulto.") # Se imprime "Usted es un adulto." para el resto de los casos

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

# ---

# Le solicitamos al usuario una contraseña en tipo de dato string (str)
contraseña_ingresada = str(input("Ingrese su contraseña:"))

# Usamos len() para poder contar la cantidad de caractéres de la contraseña_ingresada
longitud_contraseña = len(contraseña_ingresada)

# Iniciamos la estructura condicional. 

# Si la longitud_contraseña está dentro del rango 8 y 14 inclusive, se imprime "Ha ingresado una contraseña correcta."
# En el segundo se usa 15, ya que range no incluye el segundo parámetro inclusive, si el primero
if longitud_contraseña in range (8, 15):
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.") # en otro caso, se imprime "Por favor, ingrese una contraseña de entre 8 y 14 caracteres."

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente: (no copiaré la explicación aquí para evitar confusiones, esta en el PDF original que subieron)

# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. Definir la lista numeros_aleatorios de la siguiente forma: (no copiaré la explicación aquí para evitar confusiones, esta en el PDF original que subieron)

# ---

# Importamos `statistics` y las funciones respectivas (moda (mode), mediana (median), media (mean))
from statistics import mode, median, mean

# Importamos `random` para la selección de números aleatorios entre 1 y 100
import random

# Establecemos `numeros_aleatorios` como variable para incluir en ella 50 valores numéricos del 1 al 100 con `random`
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Creamos variables para almacenar la media, mediana y moda del rango `numeros_aleatorios` 
mode_output = mode(numeros_aleatorios)
median_output = median(numeros_aleatorios)
mean_output = mean(numeros_aleatorios)

# Imprimimos la media, moda y mediana para referencia
print(f"La media es {mean_output}, la mediana {median_output} y la moda {mode_output}. Entonces...")

# Iniciamos la estructura condicional

# Sí la media es mayor que la mediana y (and) la mediana es mayor que la moda, se imprime "El sesgo es positivo (o a la derecha)."
if (mean_output > median_output) and (median_output > mode_output):
    print("El sesgo es positivo (o a la derecha).")
elif (mean_output < median_output) and (median_output < mode_output): # Sí la media es menor que la mediana y (and) la mediana es menor que la moda, se imprime "El sesgo es negativo (o a la izquierda)."
    print("El sesgo es negativo (o a la izquierda).")
elif mean_output == median_output and median_output == mode_output: # Sí la media es igual que la mediana y (and) la mediana es igual que la moda, se imprime "No hay sesgo."
    print("No hay sesgo.")
else:
    print("Otro resultado, fuera de las tres opciones.") # Para el resto de las combinaciones posible, se imprime "Otro resultado, fuera de las tres opciones."

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# ---

# Le solicitamos una palabra o frase al usuario
frase_usuario = str(input("Escribí una frase o una palabra"))

# Almacenamos en una variable las vocales, tanto en mayúscula cómo en minúscula.
vocales = str("aeiouAEIOU")

# Iniciamos la estructura condicional
# Si la frase o palabra que incresó el usuario termina (por eso la posición [-1] en frase_usuario) en una vocal, se imprime "!"
if frase_usuario[-1] in vocales:
    print("!")
else:
    print(frase_usuario) # En otro caso, se imprime la frase que ingresó el usuario

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1.​ Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2.​ Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3.​ Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Le solicitamos el nombre al usuario
nombre_usuario = str(input("Ingresá tu nombre:"))

# Le solicitamos al usuario que ingrese una opción entre 1, 2 y 3
opcion_usuario = int(input("Ahora ingresá 1, 2 o 3 en función de la opción que desees: \n 1. Si querés que tu nombre aparezca en mayúsculas. \n 2. Si querés que tu nombre aparezca en minúsculas. \n 3. Si querés que tu nombre aparezca con la primera letra en mayúscula."))

# Iniciamos la estructura condicional
# Sí la opción es 1, se imprime el nombre en mayúsculas junto con información adicional
if opcion_usuario == 1:
    nombre_usuario = nombre_usuario.upper()
    print(f"{nombre_usuario}, este es tu resultado dado que elegiste la opción {opcion_usuario}.")
# Sí la opción es 2, se imprime el nombre en minúsculas junto con información adicional
elif opcion_usuario == 2:
    nombre_usuario = nombre_usuario.lower()
    print(f"{nombre_usuario}, este es tu resultado dado que elegiste la opción {opcion_usuario}.")
# Sí la opción es 3, se imprime el nombre con la primera letra mayúscula junto con información adicional
elif opcion_usuario == 3:
    nombre_usuario = nombre_usuario.title()
    print(f"{nombre_usuario}, este es tu resultado dado que elegiste la opción {opcion_usuario}.")
# En otro caso, se imprime "Ingresá una opción válida"
else:
    print("Ingresá una opción válida.")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: ●​ Menor que 3: "Muy leve" (imperceptible). ●​ Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible). ●​ Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). ●​ Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). ●​ Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos). ●​ Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# ---

# Le solicitamos la magnitud del terremoto sufrido al usuario
magnitud_usuario = float(input("Brindame la magnitud del terremoto que sufrió tu ciudad:"))

# Establecemos en diferentes variables el rango de valores para cada categoria
richter_muy_leve = magnitud_usuario < 3
richter_leve = magnitud_usuario >= 3 and magnitud_usuario < 4 
richter_moderado = magnitud_usuario >= 4 and magnitud_usuario < 5 
richter_fuerte = magnitud_usuario >= 5 and magnitud_usuario < 6
richter_muy_fuerte = magnitud_usuario >= 6 and magnitud_usuario < 7
richter_extremo = magnitud_usuario >= 7

# Iniciamos la estructura condicional
# Para cada categoría escala, en función de las relaciones lógicas para la escala Richter establecidas anteriormente
# se imprimirá un mensaje que refleje cada categoría determinada por la magnitud del terremoto ingresada por el usuario
if richter_muy_leve:
    print(f"La escala de Richter según la magnitud {magnitud_usuario}, nos indica que el terremoto es muy leve (imperceptible)")
elif richter_leve:
    print(f"La escala de Richter según la magnitud {magnitud_usuario}, nos indica que el terremoto es leve (ligeramente perceptible)")
elif richter_moderado:
    print(f"La escala de Richter según la magnitud {magnitud_usuario}, nos indica que el terremoto es moderado (sentido por personas, pero generalmente no causa daños)")
elif richter_fuerte:
    print(f"La escala de Richter según la magnitud {magnitud_usuario}, nos indica que el terremoto es fuerte (puede causar daños en estructuras débiles)")
elif richter_muy_fuerte:
    print(f"La escala de Richter según la magnitud {magnitud_usuario}, nos indica que el terremoto es muy fuerte (puede causar daños significativos)")
else:
    print(f"La escala de Richter según la magnitud {magnitud_usuario}, nos indica que el terremoto es extremo (puede causar graves daños a gran escala)")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año: (cuadro clasificatorio en el PDF del TP). Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# ---

# Le solicitamos al usuario el hemisferio, el mes y el día en el cuál se encuentra
hemisferio_usuario = str(input("Ingresá en que hemisferio te encontras. Escribí 'N' para norte o 'S' para Sur:"))
mes_usuario = int(input("Ingresá el número de mes en el que te encontrás (1-12):"))
dia_usuario = int(input("Ingresá el número de día en el que te encontrás (1-31):"))

# Iniciamos una primera estructura condicional
# Manejo de errores básico en cuanto a día, mes o mal ingreso de la letra de hemisferio 
if mes_usuario < 1 or mes_usuario > 12:
    print("Error: Mes incorrecto. Intentá nuevamente.")
elif dia_usuario < 1 or dia_usuario > 31:
    print("Error: Día inexistente. Intentá nuevamente.")
elif hemisferio_usuario not in ["N", "S"]:
    print("Error: No ingresaste correctamente tu hemisferio. Intentá otra vez.")
# En caso de que lo anterior esté bien ingresado
# esta parte de la estructura evalua la estación en función del hemisferio, el mes y el día que ingresó el usuario
else:
    if (mes_usuario == 12 and dia_usuario >= 21) or (1 <= mes_usuario <= 2) or (mes_usuario == 3 and dia_usuario <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes_usuario == 3 and dia_usuario >= 21) or (4 <= mes_usuario <= 5) or (mes_usuario == 6 and dia_usuario <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes_usuario == 6 and dia_usuario >= 21) or (7 <= mes_usuario <= 8) or (mes_usuario == 9 and dia_usuario <= 20): 
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

# Iniciamos una última estructura condicional
# En base al resultado de la estructura condicional previa, en donde se establecen valores para `estacion_norte` y `estacion_sur`
# Aquí indicamos que en funcion de "N" o "S" se corresponde una de esas dos estaciones.
if hemisferio_usuario == "N":
    print(f"La estación en la que te encontrás es {estacion_norte}")
elif hemisferio_usuario == "S":
    print(f"La estación en la que te encontrás es {estacion_sur}")
else:
    print("") # Para que no se imprima nada en caso de error de hemisferio en la primera estructura, dado que se está ejecutando igual

