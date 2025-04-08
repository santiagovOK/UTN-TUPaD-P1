# Trabajo práctico Nº4 - Estructuras repetitivas -  Varela Santiago Octavio (Comisión 22)

# Resolución del trabajo práctico Nº4 al 2025-04-08

# Respuestas también en https://github.com/santiagovOK/UTN-TUPaD-P1/tree/main/04EstructurasRepetitivas/VARELA_TP-04.ipynb


# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# ---

# Inicializamos `enteros` , qué será el contador que irá sumando 1 a 1 hasta 100
enteros = 0

# Bucle for, ya que sabemos cuando terminará el ciclo. 101 será el límite ya que debemos incluir hasta el 100 inclusive
for enteros in range(enteros, 101):
    print(f"Este es el entero *{enteros}*")
    enteros += 1 # Sumamos 1 a enteros en cada iteración, empezando en 0 que se imprime en el paso anterior dentro de la primera iteración.

# ---

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

# ---

num_usuario = int(input("Ingresá un número entero positivo: ")) # Solicitamos un número al usuario.

# Inicializamos `digitos` que será el contador
digitos = 0

# Inicializamos una estructura condicional, ya que debemos tratar el caso de 0 diferente al resto en `ìf`
if num_usuario == 0:
    digitos = 1
else:
    # Bucle para el resto de los casos. Sí la última división da 0 o menos (que séra en los casos donde solo hay un número de un dígito), el bucle se detiene. Es por eso que no podemos incluir un input del usuario `0` aquí, ya que sino el bucle no se ejecutaría
    while num_usuario > 0:
        digitos += 1
        num_usuario = num_usuario // 10 # Se divide por 10, ya que al hacerlo siempre se quita el último dígito de un número entero

print(f"El número ingresado tiene {digitos} digitos.") # Impresión del mensaje final para el usuario

# ---

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# ---

# Le solicitamos dos números al usuario
primer_numUsuario = int(input("Ingrese un número: "))
segundo_numUsuario = int(input("Ingrese otro número: "))

# Almacenamos los rangos en variables para una mejor lectura de código
rango_minimo = primer_numUsuario + 1
rango_maximo = segundo_numUsuario

# Inicializamos sumatoria para luego almacenar la suma
sumatoria = 0

# Primer mensaje para guiar al usuario sobre la operación que se realizará
print(f"Comprendiendo el rango entre {primer_numUsuario} y {segundo_numUsuario} sin sumar ambos...")

# Iniciamos el bucle para ir sumando los valores, excepto los extremos
for i in range(rango_minimo, rango_maximo):
    sumatoria += i # Siendo i el contador que irá de uno en uno, se irá almacenando la suma de `i` en cada iteración dentro de `sumatoria`
    print(f"Sumamos {i}") # Impresión de cada uno de los números que se van sumando

# Imprimimos el resultado final
print(f"El resultado de la suma entre todos los valores quitando ambos números es: {sumatoria}")

# ---

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# ---

# Solicitamos al usuario que ingrese un número entero positivo
num_usuario = int(input("Ingresá un número entero positivo. Cada número que ingreses se sumará con los anteriores. Para salir del programa, ingresá `0`"))
# Creamos la variable `suma` para almacenar la suma de los números ingresados
suma = 0

# Imprimimos un primer mensaje para guiar al usuario
print(f"Hasta el momento solo ingresaste un número , entonces...\n")

# Iniciamos el bucle que permitirá seguir ingresando números y sumarlos al resultado parcial
# La condición `num_usuario` distinto (!=) de 0 indica que el bucle funcionará mientras que no se ingrese 0

while num_usuario != 0:
    suma += num_usuario # Se suma el último número ingresado a la suma general
    print(f"La suma hasta el momento da como resultado {suma}")
    num_usuario = int(input("Ingresá un número entero. Cada número que ingreses se sumará con los anteriores. Para salir del programa, ingresá `0`")) # Repetimos la primer variable dentro del bucle while para que se le vuelva a solicitar al usuario un número
    print(f"Ahora ingresaste {num_usuario}, entonces...\n") # Mensaje con el núevo número ingresado, se repite el ciclo

print(f"El programa ha finalizado porque colocaste `0`. La suma de todos los números ingresados es de {suma}") # Imprimimos un mensaje con la suma final al finalizar el programa

# ---

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# ---

import random # Importamos el paquete random, que también usamos en el TP Nª3

# Establecemos el número aleatorio a adivinar, gracias a la función random
num_aleatorio = [random.randint(1, 9)]

# Le solicitamos al usuario un primer número
num_usuario = int(input("Ingresá el número entero positivo que creés que será el número ganador: "))

# Establecemos la variable `intentos` en 1, ya que el ingreso anterior ya establece un primer intento del usuario
intentos = 1

# Creamos un bucle while con `not in` para evitar errores. Mientras num_usuario no sea igual a num_aleatorio, while continuará iterando.
while num_usuario not in num_aleatorio:
    # Colocamos este mensaje primero ya que así totamos el primer intento fuera del bucle.
    print(f"Ingresaste {num_usuario}. Este fue tu intento {intentos}. ")
    print("Número equivocado, intentá nuevamente.")
    # Le solicitamos nuevamente un número al usuario en caso de que el primero no haya sido certero (y así se repetirá hasta que el bucle no se ejecute más.)
    num_usuario = int(input("Ingresá otro número entero positivo: ")) 
    # Sumamos un intento luego de haber ingresado otro número
    intentos += 1

# Imprimimos un mensaje final de victoria en caso de que el usuario haya acertado el número.
print(f"Ganaste! El número ingresado {num_usuario} es igual al número ganador {num_aleatorio}. Lo hiciste en {intentos} intentos.")

# ---

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

# Inicializamos `numero`
numero = 0

# Comenzamos un bucle for. Para comenzar desde 100 inclusive, tenemos que colocar `100` como primer parámetro en range, `1` como segundo 
# (iríamos de 100 hasta 2 inclusive) y por último -1 (indicando una frecuencia decreciente de -1). 
for numero in range (100, 1, -1):
    # Cada valor que irá pasando por range se filtrará con este condicional para pares, usando modulo (%)
    if numero % 2 == 0:
        print(f"Número par: {numero}")

# O

numeros = 0

# Directamente usando frecuencia -2 para ir de par en par

for numeros in range (100, 1, -2): 
    print (f"Número par: {numeros}")

# ---

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# ---

# Le solicitamos un número al usuario
numUsuario = int(input("Ingrese un número entero positivo: "))

# Inicializamos sumatoria para luego almacenar la suma
sumatoria = 0

# Primer mensaje para guiar al usuario sobre la operación que se realizará
print(f"Comprendiendo el rango entre 0 y {numUsuario} sin sumar este último...")

# Iniciamos el bucle para ir sumando los valores, excepto el número extremo ingresado por el usuario
for i in range(numUsuario):
    sumatoria += i # Siendo i el contador que irá de uno en uno, se irá almacenando la suma de `i` en cada iteración dentro de `sumatoria`
    print(f"Sumamos {i}") # Impresión de cada uno de los números que se van sumando

# Imprimimos el resultado final
print(f"El resultado de la suma entre todos los valores, quitando el número ingresado por el usuario, es: {sumatoria}")

# ---

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# ---

# Inicializamos las variables a utilizar

num_Usuario = 0
contador = 0

# Establecemos la variable `limite` en 100. Solo cambiando este número podemos probar con una cantidad menor si es necesario 
limite = 100

# Inicializamos los contadores para cada caso
contador_pares = 0
contador_impares = 0
contador_negativos = 0
contador_positivos = 0

# Inicializamos el bucle while a utilizar. `contador` arranca en 0 inclusive y el `limite` es 100

while contador < limite:

    # Le pedimos al usuario que ingrese un número dentro del bucle, para que cada vez que itere se le pida hasta llegar a la cantidad `limite`
    num_Usuario = int(input(f"Ingrese un número entero, luego deberás agregar más números hasta llegar a {limite}"))

    # Primer estructura condicional dentro del bucle para establecer si `num_Usuario` es par o impar y sumarlo a su contador correspondiente
    if num_Usuario % 2 == 0:
        contador_pares += 1
    elif num_Usuario % 2 != 0:
        contador_impares += 1

    # Segunda estructura condicional dentro del bucle para establecer si `num_Usuario` es negativo o positivo y sumarlo a su contador correspondiente
    if num_Usuario < 0:
        contador_negativos += 1
    elif num_Usuario > 0:
        contador_positivos += 1

    # Sumamos 1 al contador para que while siga iterando hasta llegar a límite
    contador += 1

# Impresión del mensaje final con todos los datos solicitados por la consigna

print(f"De los {limite} números ingresados, {contador_pares} fueron pares; \n {contador_impares} son impares; \n {contador_negativos} son negativos y {contador_positivos} son positivos.")


# ---

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

# ---

# Inicializamos las variables a utilizar

num_Usuario = 0
contador = 0
suma = 0 

# Establecemos la variable `limite` en 100. Solo cambiando este número podemos probar con una cantidad menor si es necesario 
limite = 100

# Inicializamos el bucle while a utilizar. `contador` arranca en 0 inclusive y el `limite` es 100

while contador < limite:
    # Le pedimos al usuario que ingrese un número dentro del bucle, para que cada vez que itere se le pida hasta llegar a la cantidad `limite`
    num_Usuario = int(input(f"Ingrese un número entero, luego deberás agregar más números hasta llegar a {limite}"))

    # En la variable `suma` se van almacenando cada uno de los `limite` (100) números que se ingresaran
    suma += num_Usuario

    # Sumamos 1 al contador para que while siga iterando hasta llegar a límite
    contador += 1

# Variable `media` para almacenar la media / promedio de todos los números ingresados una vez finalizado el bucle
media = suma / limite

# Impresión del mensaje final con todos los datos solicitados por la consigna

print(f"En base a los {limite} números ingresados, el total de su suma es de {suma} y la media es de {media}")

# ---

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

# ---

# Le solicitamos un número al usuario, pero en realidad directamente lo estamos pasando como texto para poder invertirlo luego con len()

numCadena_usuario = str(input("Ingresá un número entero positivo: "))

# Inicializamos una variable como cadena (str) vacía, para poder almacenar cada uno de los dígitos del números invertidos
cadena_invertida = ""

# Iniciamos un bucle for para invertir el número. 
# Si por ejemplo tenemos `547`, el rango va a empezar en 7 (posición [2], que es len(numCadena_usuario) - 1) y va a terminar en 5 (-1, posición [0]), decreciendo con una frecuencia de -1 cada iteración.
for i in range(len(numCadena_usuario) - 1, -1, -1):
    cadena_invertida += numCadena_usuario[i] 
    # En `cadena_invertida` + `numCadena_usuario[i]` lo que se está sumando es el caracter por cada posición, es por eso que `cadena_invertida` inicia vacía, para ir sumando los caractéres del número invertido.

print(cadena_invertida)

# ---
