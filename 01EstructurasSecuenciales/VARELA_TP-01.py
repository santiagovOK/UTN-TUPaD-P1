# Unidad Nª 1 - Estructuras Secuenciales - Programación 1
# Trabajo Práctico Nª 1 - Estructuras Secuenciales - Varela Santiago Octavio (Comisión 22)

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input(f"Ahora ingresá tu apellido {nombre}: ")
edad = input(f"Bien {nombre} {apellido}, ahora ingresá tu edad: ")
lugar_residencia = input (f"Por último {nombre} {apellido}, ingresá tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {lugar_residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
# Aclaración : tengo entendido que se puede usar math.pi llamando a la librería math para mayor precisión, pero dado que no lo hemos visto, lo hice con el valor 3.14.

radio = float(input("Ingrese el radio del círculo: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"El área del círculo es {area} y su perímetro es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
# Aclaración : este caso podría hacerse con un bucle `for`, pero dado que estamos en estructuras secuenciales lo realizaré manualmente con un `print` por cada multiplicación.

num = int(input("Ingrese un número:"))
print(f"{num} x 1 = {num * 1}")
print(f"{num} x 2 = {num * 2}")
print(f"{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}")
print(f"{num} x 5 = {num * 5}")
print(f"{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}")
print(f"{num} x 8 = {num * 8}")
print(f"{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}")


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
# Aclaración : al igual que el ejercicio anterior en cuanto a temas no vistos, en el primer encuentro de tutorias vimos que con una estructura condicional podríamos evitar que el usuario ingrese un 0, pero dado que estamos en estructuras secuenciales, no lo haré y "confiaremos" en el usuario.

numero1 = int(input("Ingrese un número distinto de 0: "))
numero2 = int(input("Ingrese otro número distinto de 0: "))

print(f"Caso de suma: {numero1} + {numero2} = {numero1 + numero2}")
print(f"Caso de resta: {numero1} - {numero2} = {numero1 - numero2}")
print(f"Caso de multiplicación: {numero1} * {numero2} = {numero1 * numero2}")
print(f"Caso de división: {numero1} / {numero2} = {numero1 / numero2}")


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2

peso = float(input("Ingrese su peso en kg (solo el número, sin la unidad): "))
altura = float(input("Ingrese su altura en metros (solo el número, sin la unidad): "))

imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {imc}")


# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

print(f"El promedio de los números ingresados es: {(num1 + num2 + num3) / 3}")