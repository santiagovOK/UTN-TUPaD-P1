# Trabajo práctico Nº5 - Funciones -  Varela Santiago Octavio (Comisión 22)

# Resolución del trabajo práctico Nº5 al 2025-04-14

# Respuestas también en https://github.com/santiagovOK/UTN-TUPaD-P1/tree/main/05Funciones/VARELA_TP-05.ipynb

# 1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.


# ---

# Funciones

# Creamos la función solicitada, que solo imprimirá "Hola Mundo!"

def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal

# Llamamos a la función creada, sin parámetros ya que no tiene

imprimir_hola_mundo()

# ---

# 2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# ---

# Funciones

# Función saludar_usuario, con un único argumento (nombre)
def saludar_usuario(nombre):
    print(f"Hola {nombre}!") # La función imprime este mensaje al ser ejecutada

# Programa principal

# Le solicitamos su nombre al usuario
nombre = input("Ingresá tu nombre, así recibirás un saludo:")

# Llamamos a la función, ingresando `nombre` que es el nombre que le dimos a la variable  que almacenara el nombre del usuario
saludar_usuario(nombre)

# ---

# 3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# ---

# Funciones

# Función informacion_personal, con varios argumentos (nombre, apellido, edad, residencia)
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}") # La función imprime este mensaje al ser ejecutada

# Programa principal

# Le solicitamos datos al usuario que luego pasarán como argumentos en la función (podrían llamarse distinto)
nombre = input("Ingresá tu nombre")
apellido = input("Ingresá tu apellido")
edad = int(input("Ingresá tu edad:"))
residencia = input("Ingresá tu lugar de residencia:")

# Ejecutamos la función ingresando como argumento las variables que almacenan los valores que ingresó el usuario
informacion_personal(nombre, apellido, edad, residencia)

# ---

# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. `calcular_perimetro_circulo(radio)` que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# ---

# Funciones

# Importamos math para usar la función pi, necesaria para calcular área y perímetro de forma precisa

import math

# Construimos la primera funcion

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2) # Calculamos el area usando la función `pi` y el argumento `radio`
    print(f"El área del circulo es {area}") # Imprimimos el valor resultante de `area`

# Construimos la segunda funcion

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio # Calculamos el perimetro usando la función `pi` y el argumento `radio`
    print(f"El perímetro del circulo es {perimetro}") # Imprimimos el valor resultante de `perimetro`

# Programa principal

# Le solicitamos un valor de radio al usuario (en decimal)

radio_usuario = float(input("Ingrese un valor para el radio del círculo:"))

# Llamamos a las dos funciones anteriormente creadas para realizar los cálculos, teniendo como argumento `radio_usuario` (radio ingresado por el usuario), que corresponde al argumento `radio` dentro de la funcion propiamente dicha

calcular_area_circulo(radio_usuario)

calcular_perimetro_circulo(radio_usuario)


# ---

# 5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# ---

# Funciones

# Función para pasar segundos a horas. 
def segundos_a_horas(segundos):
    # Dividimos los segundos por la cantidad de segundos correspondientes a una hora (60 * 60 = 3600) 
    hora = float(segundos / 3600)
    # Imprimimos el mensaje correspodiente
    print(f"Los segundos ingresados {segundos} corresponden a {hora} horas")

# Programa principal

# Primero solicitamos una cantidad de segundos al usuario
segundos_usuario = int(input("Ingresá la cantidad de segundos que buscás que transformemos en horas: "))

# Luego ejecutamos la función, ingresando como argumento los `segundos_usuario`
segundos_a_horas(segundos_usuario)

# ---

# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# ---

# Funciones

# Definimos la función tabla_multiplicar, en donde se ingresa cualquier número como argumento `numero` para ser multiplicado hasta 10
def tabla_multiplicar(numero):
    # # Operación para cada una de las 10 multiplicaciones, almacenadas en la variable resultado1, etc
    resultado1 = numero * 1 
    resultado2 = numero * 2
    resultado3 = numero * 3
    resultado4 = numero * 4
    resultado5 = numero * 5
    resultado6 = numero * 6
    resultado7 = numero * 7
    resultado8 = numero * 8
    resultado9 = numero * 9
    resultado10 = numero * 10
    # Imprimimos cada uno de los resultados de forma coherente y espaciada con `\n` 
    print(f"La tabla de multiplicar para {numero} es la siguiente:\n{numero} x 1 = {resultado1}\n{numero} x 2 = {resultado2}\n{numero} x 3 = {resultado3}\n{numero} x 4 = {resultado4}\n{numero} x 5 = {resultado5}\n{numero} x 6 = {resultado6}\n{numero} x 7 = {resultado7}\n{numero} x 8 = {resultado8}\n{numero} x 9 = {resultado9}\n{numero} x 10 = {resultado10}")

# Programa principal

# Le solicitamos el número a multiplicar al usuario
num_usuario = int(input("Ingresá el número sobre el que quieras conocer su tabla de multiplicar hasta 10: "))

# Llamamos a la función para mostrar la tabla de multiplicar, reemplazando el argumento default por `num_usuario`
tabla_multiplicar(num_usuario)

# ---

# 7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# ---

# Funciones

# Función que contiene todas las operaciones, ingresado numeros por argumentos `a` y `b`
def operaciones_basicas(a, b):
    # Operaciones en base a `a` y `b`
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    # Usamos `return` para que vuelva los valores de las variables como `tuple`
    return (suma, resta, multiplicacion, division)

# Programa principal

# Le solicitamos al usuario 2 números y los almacenamos en dos variables respectivamente
num1_usuario = int(input("Ingresá un primer número para realizar operaciones de suma, resta, multiplicación y división: "))
num2_usuario = int(input("Ingresá un segundo número para realizar operaciones de suma, resta, multiplicación y división: ")) 

# Almacenamos las operaciones contenidas en la función `operaciones_basicas` a partir de los númeeros del usuario como argumentos

resultados = operaciones_basicas(num1_usuario, num2_usuario)

# Imprimimos un mensaje para las operaciones, más apropiado para el formato tupla
print(f"Los resultados de cada una de las operaciones (suma, resta, multiplicación y división) entre {num1_usuario} y {num2_usuario} son: {resultados} \n")

# Demostración de que la variable `resultados` está siendo tomada como tipo tupla

print("`resultados` es...")
print(type(resultados))


# ---

# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# ---

# Funciones

# Función para calcular imc, ingresando como argumentos peso y altura
def calcular_imc(peso, altura):
    # Operación para calcular imc en base a peso y altura (lo vimos en el tp Nº 1)
    imc = (peso / (altura ** 2))
    # Imprimimos el mensaje con la variable `imc` y, al llamarla, agregamos `:.2f` para que el output, que será de float o punto flotante, se limite hasta el segundo decimal.
    print (f"Su índice de masa corporal es: {imc:.2f}")

# Programa principal

# Le solicitamos la altura y peso al usuario
peso_usuario = float(input("Ingresá tu peso en kilogramos (solo el número, sin la unidad): "))
altura_usuario = float(input("Ingresá tu altura en metros (solo el número, sin la unidad): "))

# Llamamos a la función previamente creada `calcular_imc`, teniendo como argumento las últimas dos varibles que contienen los valores ingresados por el usuario.

calcular_imc(peso_usuario, altura_usuario)

# ---

# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# ---

# Funciones

# Función para pasar de grados Celsius a Fahrenheit, teniendo como único argumento los grados `celsius`
def celsius_a_fahrenheit(celsius):
    # Operación para pasar los grados `celsius` a fahrenheit, almacenados en `fahrenheit`
    fahrenheit = (celsius * 9/5) + 32
    # Imprimimos el resultado del pasaje con un mensaje acorde
    print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# Programa principal

# Le solicitamos los grados celsius al usuario
celsius_usuario = int(input("Ingresá la temperatura en Celsius (Cº) que hace en tu ciudad. La pasaremos a fahrenheit..."))

# Utilizamos la función creada para pasar los `celsius_usuario` que solicitamos a fahrenheit
celsius_a_fahrenheit(celsius_usuario)

# ---

# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# --- 

# Funciones

# Creamos la función para calcular el promedio de los tres números, siendo estos argumentos contenidos en `a`, `b` y `c`
def calcular_promedio(a, b, c):
    # Operación para calcular el promedio
    promedio = (a + b + c) / 3
    # Retornamos la variable `promedio` con el valor final almacenado en ella
    return promedio

# Programa principal

# Le solicitamos al usuarios los tres númerosa ingresar como argumentos
num1_usuario = float(input("Ingresá un primer número: "))
num2_usuario = float(input("Ingresá un segundo número: "))
num3_usuario = float(input("Ingresá un tercer número, calcularemos el promedio junto con los dos últimos que ingresaste: "))

# Almacenamos el valor obtenido en `promedio` al haber llamado `calcular_promedio` para hacer el promedio de los tres valores solicitados al usuario anteriormente
promedio = calcular_promedio(num1_usuario, num2_usuario, num3_usuario)

# Imprimimos un mensaje acorde para el usuario, con los tres numeros que ingresó y su promedio final almacenado en `promedio`
print(f"El promedio resultante de {num1_usuario}, {num2_usuario} y {num3_usuario} es {promedio}. ")

# --- 