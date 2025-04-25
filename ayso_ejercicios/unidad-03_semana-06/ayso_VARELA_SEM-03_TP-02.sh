# Arquitectura y Sistemas Operativos - Unidad 3 - Semana 6

# Trabajo práctico Nº2 - Bash Scripting -  Varela Santiago Octavio (Comisión 22)

# Resolución del trabajo práctico Nº6 al 2025-04-25

# Respuestas también en https://github.com/santiagovOK/UTN-TUPaD-P1/tree/main/ayso_ejercicios/unidad-03_semana-06/ayso_VARELA_SEM-03_TP-02.ipynb


# ---------------------------

# Ejercicio 1.1: Crear un script en Bash que muestre el valor de seis variables de entorno del sistema.
# Requisitos:
# 1. El script debe mostrar el valor de las siguientes variables de entorno:
#    o LOGNAME: El nombre del usuario con el que se ha iniciado sesión.
#    o HOME: El directorio home del usuario.
#    o SHELL: El shell predeterminado del usuario.
#    o PWD: El directorio de trabajo actual.
#    o USER: El nombre de usuario del que se ha iniciado sesión.
#    o SSH_TTY: El terminal asociado a la sesión SSH, si está disponible.
# 2. El script debe mostrar el valor de cada una de estas variables de entorno de forma clara y enunciativa, por ejemplo:
#    o "La variable LOGNAME tiene el valor XXX"
#    o "La variable HOME tiene el valor YYY"
# 3. Pasos adicionales:
#    o El script puede comenzar limpiando la pantalla para una mejor presentación, aunque esto es opcional.


# ---------------------------

#!/bin/bash

# Limpiamos la pantalla con `clear`

clear

# Imprimimos los 6 mensajes respectivos a cada variable de entorno, con sus valores
# No es necesario mucho más ya que, justamente, no precisamos de definir cada una de las variables

echo "La variable LOGNAME tiene el valor de" $LOGNAME
echo "La variable HOME tiene el valor de" $HOME
echo "La variable SHELL tiene el valor de" $SHELL
echo "La variable PWD tiene el valor de" $PWD
echo "La variable USER tiene el valor de" $USER
echo "La variable SSH_TTY tiene el valor de" $SSH_TTY

# ---------------------------

# Ejercicio 1.2: Crear un script en Bash que pida un nombre de usuario y un mensaje, y luego envíe ese mensaje al usuario especificado utilizando el comando write.
# Requisitos:
# 1. El script debe pedir al usuario que ingrese un nombre de usuario.
# 2. Luego debe solicitar un mensaje que el script enviará al usuario indicado previamente.
# 3. El script debe enviar el mensaje al usuario especificado utilizando el comando write.
# Pasos del ejercicio:
# 1. El script debe realizar lo siguiente:
# 2. Pedir un nombre de usuario y almacenarlo en una variable.
# 3. Pedir un mensaje y almacenarlo en una variable.
# 4. Usar un redireccionamiento para guardar el mensaje en un archivo temporal (mensaje.txt).
# 5. Utilizar el comando write para enviar el mensaje al usuario especificado.
# 6. Como alternativa, también se puede usar una tubería (pipe) para enviar el mensaje sin necesidad de un archivo intermedio.


# ---------------------------


#!/bin/bash

# Primero solicitamos con `read` el nombre del usuario, que almacenamos en la variable `nombre`. Agrego la flag -p para enviar un mensaje al usuario por terminal al mismo tiempo que se almacenan los valores en la variable.
read -p "Ingresá tu nombre: " nombre

# Imprimimos la variable anterior con un mensaje acorde 
echo "Hola" $nombre "ahora sigamos con lo siguiente."

# Solicitamos el mensaje al usuario, con el mismo procedicimiento que en el caso de `nombre`
read -p "Ingresá un mensaje que te quieras enviar a vos mismo:" mensaje 

# Redireccionamos el output de `mensaje` al archivo mensaje.txt 
echo $mensaje > mensaje.txt

# Enviamos un mensaje a `nombre` que contenga el archivo previamente creado.
# **Aclaración** este archivo no se va a enviar si $nombre no existe como usuario en la sesión 
write $nombre < mensaje.txt

# Borramos el archivo .txt previamente creado, ya que su uso era temporal
rm mensaje.txt

# ---------------------------

# Ejercicio 1.3: Crear un script en Bash que reciba varios parámetros al ejecutarse y muestre un mensaje indicando el valor de cada uno de los parámetros. Además, debe mostrar el número total de parámetros y el nombre del archivo del script.
# Requisitos:
# 1. El script debe aceptar hasta 9 parámetros de entrada.
# 2. El script debe mostrar un mensaje para cada parámetro indicando el valor de los parámetros $1, $2, ..., $9.
# 3. El script debe mostrar el número total de parámetros recibidos utilizando $#.
# 4. El script debe mostrar todos los parámetros concatenados utilizando $*.
# 5. El script debe mostrar el nombre del archivo ejecutado utilizando $0.
# Pasos del ejercicio:
# 1. Al ejecutar el script, se deben pasar varios parámetros en la línea de comandos.
# 2. El script debe imprimir un mensaje para cada parámetro indicando su valor en la forma:
#    El parámetro $1 es <valor1>
#    El parámetro $2 es <valor2>
#    ...
# 3. Además de los mensajes de los parámetros, el script debe mostrar:
#    o El número total de parámetros.
#    o Todos los parámetros juntos.
#    o El nombre del archivo que contiene el script.


# ---------------------------

#!/bin/bash

# **Aclaración**: Este script supone que, al ejecutarlo junto parametros en una terminal, se irán imprimiendo esos parámetros hasta nueve.
# Por ejemplo, si ejecutaramos en una terminal `./parametros.sh uno dos` el parámetro $1 sería `uno`, el $2 `dos` y así sucesivamente si aclararamos alguno más.

# Mostrar el valor de cada parámetro
echo "El parámetro \$1 es $1"
echo "El parámetro \$2 es $2"
echo "El parámetro \$3 es $3"
echo "El parámetro \$4 es $4"
echo "El parámetro \$5 es $5"
echo "El parámetro \$6 es $6"
echo "El parámetro \$7 es $7"
echo "El parámetro \$8 es $8"
echo "El parámetro \$9 es $9"

# Mostrar el número total de parámetros con `$#` como comando preestablecido en Bash
echo "El número total de parámetros es $#"

# Mostrar todos los parámetros concatenados con `$*` como comando preestablecido en Bash
echo "Todos los parámetros juntos: $*"

# Mostrar el nombre del archivo ejecutado con `$0` como comando preestablecido en Bash
echo "El nombre del archivo ejecutado es $0"

# ---------------------------


# Ejercicio 1.4: Crear un script en Bash que pida al usuario dos cadenas de texto, verifique si alguna de ellas está vacía y, finalmente, compare ambas cadenas para determinar si son iguales o no.
# Requisitos:
# 1. El script debe pedir al usuario que ingrese dos cadenas de texto.
# 2. El script debe verificar si la primera cadena (cadena1) está vacía. Si está vacía, mostrar un mensaje indicando que "La cadena1 está vacía", de lo contrario, mostrar que "La cadena1 no está vacía".
# 3. El script debe verificar si la segunda cadena (cadena2) está vacía. Si está vacía, mostrar un mensaje indicando que "La cadena2 está vacía", de lo contrario, mostrar que "La cadena2 no está vacía".
# 4. El script debe comparar ambas cadenas y mostrar un mensaje indicando si son iguales o no.
# Pasos del ejercicio:
# 1. Al ejecutar el script, el usuario deberá ingresar dos cadenas de texto.
# 2. El script debe verificar si cada una de las cadenas ingresadas está vacía.
# 3. El script debe realizar una comparación entre ambas cadenas.
# 4. Según el resultado de la comparación, el script debe indicar si las cadenas son iguales o diferentes.


# ---------------------------

#!/bin/bash

# Solicitamos ambas cadenas de texto al usuario con `read -p` y almacenando los valores en `cadena1` y `cadena2` respectivamente.

read -p "Ingrese una frase:" cadena1
read -p "Ingrese otra frase:" cadena2

# Iniciamos un primer condicional, usando `-z` para controlar si las cadenas están vacías o no

if [ -z $cadena1 ]; then
    echo "La cadena1 está vacía"
elif [ -z $cadena2 ]; then
    echo "La cadena2 está vacía"
elif [ -z $cadena1 && -z $cadena2 ]; then
    echo "Ambas cadenas están vacías"
else
    echo "Las dos cadenas contienen algún texto."
fi

# Imprimimos una línea para separa un poco la lectura entre ambas impresiones luego ejecutar los condicionales
echo "----"

# Iniciamos una segunda estructura condicional para evaluar si las cadenas son iguales o diferentes entre sí.

if [ "$cadena1" == "$cadena2" ]; then
    echo "Las cadenas son iguales entre sí"
else
echo "Las cadenas son diferentes entre sí."
fi

# ---------------------------

# Ejercicio 1.5: Crear un script que realice las cuatro operaciones básicas (suma, resta, multiplicación, división) con dos números proporcionados como parámetros. El script debe comprobar la cantidad de parámetros y realizar diferentes acciones según el número de parámetros ingresados, mostrando mensajes adecuados en cada caso.
# Requisitos:
# 1. El script debe aceptar dos parámetros numéricos desde la línea de comandos.
# 2. El script debe verificar la cantidad de parámetros y comportarse de la siguiente manera:
#    o Si no se ha introducido ningún parámetro, preguntará al usuario si desea introducirlos ahora, y si la respuesta es afirmativa, solicitará los dos números.
#    o Si se ha introducido solo un parámetro, preguntará al usuario si desea introducir el segundo, y si la respuesta es afirmativa, usará el primer parámetro proporcionado y solicitará el segundo.
#    o Si se han introducido más de dos parámetros, el script tomará los dos primeros parámetros y mostrará un mensaje indicando que se han proporcionado demasiados parámetros.
#    o Si se han introducido exactamente dos parámetros, el script procederá a realizar las operaciones con esos dos números.
# 3. Una vez que se han obtenido los dos números, el script debe realizar y mostrar los resultados de las cuatro operaciones básicas:
#    o Suma: número1 + número2
#    o Resta: número1 - número2
#    o Multiplicación: número1 * número2
#    o División: número1 / número2 (debe manejarse adecuadamente la división por cero)
# Mensajes a mostrar según la cantidad de parámetros:
# • Si no se introducen parámetros: "No ha introducido ninguno. ¿Quiere ahora s/n?"
# • Si se introduce solo un parámetro: "Ha introducido uno. ¿Quiere ahora s/n?"
# • Si se introducen más de dos parámetros: "Demasiados parámetros, tomo los dos primeros."
# • Si se introducen exactamente dos parámetros: "CORRECTO"
# Pasos del ejercicio:
# 1. Utilizar la variable especial $# para determinar cuántos parámetros se han pasado al script.
# 2. Dependiendo de la cantidad de parámetros, mostrar los mensajes correspondientes y utilizar el comando read para obtener los números del usuario.
# 3. Utilizar $(()) para realizar las operaciones aritméticas.
# 4. Imprimir los resultados de cada operación de forma clara.
# 5. Incluir una condición para evitar la división por cero, mostrando un mensaje de error en ese caso.

# ---------------------------

#!/bin/bash

# Evaluamos / verificamos con una estructura condicional el número de parámetros ingresados al ejecutar el script con `$#`, para ver los diferentes casos planteados en la consigna
# -eq 0 es un operador de comparación aritmético que, en este caso, indica si el número total de parámetros ($#) es igual a 0

if [ $# -eq 0 ]; then
  echo "No ingresaste ningún parámetro. ¿Queres hacerlo ahora? s/n"
  read respuesta
  # Si la respuesta es sí ("s"), se habilitara al usuario a ingresar valores para `num1` y `num2`
  if [ "$respuesta" == "s" ]; then 
    echo "Introduzca el primer número:"
    read num1
    echo "Introduzca el segundo número:"
    read num2
    # En otro caso (else), se cancela la operación
  else
    echo "Operación cancelada."
    exit 1 # `exit 1` sirve para detener la ejecución del script
  fi

    # Similar a la estructura condicional anterior, pero solo ingresando un número (por eso `$# -eq 1` )

elif [ $# -eq 1 ]; then
  echo "Ha introducido uno. ¿Quiere ahora s/n?"
  read respuesta
  if [ "$respuesta" == "s" ]; then
    num1=$1
    echo "Introduzca el segundo número:"
    read num2
  else
    echo "Operación cancelada."
    exit 1
  fi
    # Caso en el que se ingresan los dos parámetros esperados o más (else)
elif [ $# -eq 2 ]; then
  echo "CORRECTO"
  num1=$1
  num2=$2
else
  echo "Demasiados parámetros, tomo los dos primeros."
  num1=$1
  num2=$2
fi

# Realizamos las operaciones, una vez num1 y num2 están definidos

echo "Suma: $((num1 + num2))"
echo "Resta: $((num1 - num2))"
echo "Multiplicación: $((num1 * num2))"

# Establecemos la estructura condicional para evaluar, en el caso de la división, si el divisor es 0.

if [ "$num2" -eq 0 ]; then
  echo "División: Error, no se puede dividir por cero."
else
  echo "División: $((num1 / num2))"
fi

# ---------------------------

# Ejercicio 2.1: Crear un script en Bash que reciba una nota numérica e imprima la calificación correspondiente en formato alfabético, siguiendo el sistema de calificación estándar:
# • Sobresaliente para notas de 9 o más.
# • Notable para notas de 7 o más, pero menores que 9.
# • Bien para notas de 6 o más, pero menores que 7.
# • Suficiente para notas de 5 o más, pero menores que 6.
# • Insuficiente para notas menores que 5.
# Requisitos:
# 1. El script debe solicitar al usuario que ingrese una nota numérica.
# 2. Debe validar que la entrada es un número entero positivo.
# 3. Según la nota proporcionada, debe mostrar el correspondiente nivel de calificación alfabética (Sobresaliente, Notable, Bien, Suficiente, Insuficiente).
# 4. Si el usuario ingresa un valor no numérico, el script debe mostrar un mensaje de error e indicar que se debe introducir un número válido.
# Mensajes:
# • Si la entrada no es un número válido, mostrar: "Por favor, introduce un número válido."
# • Dependiendo de la nota ingresada, mostrar el correspondiente nivel de calificación (por ejemplo, "Sobresaliente", "Notable", etc.).

# ---------------------------

#!/bin/bash

read -p "Ingresá tu nota numérica (en un número entero, del 1 al 10) a este sistema de calificaciones:" nota

# Validamos si la entrada es un número válido (1 al 10)
# Para esto tuve que utilizar una expresión regular que funcione como condición para el rango que queremos incluir como válido. Ya algo conocía de expresiones regulares y no conozco otra manera más sencilla en Bash.
if ! [ "$nota" =~ ^[0-9]+$ ]; then
    echo "Por favor, introduce un número válido."
    exit 1
fi

# Verificamos si la nota es un número positivo o no con una estructura condicional y el operador de comparación -gt anteriormente utilizado
if [ "$nota" -gt 0 ]; then
    echo "La nota ingresada es un número positivo"
else
    echo "La nota ingresada no es un número positivo"
    exit 1
fi

# Establecemos la estructura condicional para las calificaciones y sus respectivas categorias por caso, usando una estructura `case` como está en nuestro material de lectura
case $nota in
    9|10)
        echo "Tu nota es $nota, por lo tanto es **sobresaliente**."
        ;;
    7|8)
        echo "Tu nota es $nota, por lo tanto es **notable**."
        ;;
    6)
        echo "Tu nota es $nota, por lo tanto es **bien**."
        ;;
    5)
        echo "Tu nota es $nota, por lo tanto es **suficiente**."
        ;;
    1|2|3|4)
        echo "Tu nota es $nota, por lo tanto es **insuficiente**."
        ;;
    *)
        echo "Por favor, introduce un número válido entre 1 y 10."
        ;;
esac

# ---------------------------

# Ejercicio 2.2: Crear un script en Bash que simule un menú interactivo con las siguientes opciones:
# 1. Calcular el área de un rectángulo.
# 2. Calcular el perímetro de un rectángulo.
# 3. Salir.
# Se deberán cumplir los siguientes requisitos:
# • Mostrar un menú con las opciones disponibles.
# • Leer la opción seleccionada por el usuario.
# o Si la opción es 1, solicitar la base y la altura del rectángulo y calcular su área.
# o Si la opción es 2, solicitar la base y la altura del rectángulo y calcular su perímetro.
# o Si la opción es 3, mostrar un mensaje de despedida y terminar el script.
# o Si la opción es inválida, mostrar un mensaje de error.


# ---------------------------

#!/bin/bash

# Imprimimos el menú de opciones para el usuario
echo "1. Calcular el área de un rectángulo"
echo "2. Calcular el perímetro de un rectángulo" 
echo "3. Salir" 

# Leemos la opción seleccionada por el usuario, solicitándole con un mensaje qué opción elegir.
read -p "Seleccione una opción(1, 2, 3): " opcion

# Usamos una estructura condicional para evaluar la opción seleccionada por el usuario
# Si ingresa la opción 1, se solicita la base y la altura del rectángulo y se calcula el área
if [ $opcion -eq 1 ]; then
    read -p "Ingrese la base del rectángulo: " base
    read -p "Ingrese la altura del rectángulo: " altura
    area=$((base * altura))
    echo "El área del rectángulo es: $area"
# Si ingresa la opción 2, se solicita la base y la altura del rectángulo y se calcula el perímetro
elif [ $opcion -eq 2 ]; then
    read -p "Ingrese la base del rectángulo: " base
    read -p "Ingrese la altura del rectángulo: " altura
    perimetro=$((2 * (base + altura)))
    echo "El perímetro del rectángulo es: $perimetro"
# Si ingresa la opción 3, se sale del programa
elif [ $opcion -eq 3 ]; then
    echo "Saliendo del programa."
    exit 1
# Si ingresa una opción no válida, se muestra un mensaje de error.
else
    echo "Opción no válida. Por favor, seleccione 1, 2 o 3."
fi

# ---------------------------

# Ejercicio 2.3: Crear un script en Bash que permita al usuario introducir números de manera continua hasta que se ingrese el número 999. Después, se le preguntará si desea ver los números que ha introducido. Si la respuesta es afirmativa, se le permitirá seleccionar un orden para mostrar los números (orden establecido, ascendente o descendente).
# Requisitos:
# 1. El script debe permitir al usuario ingresar números uno por uno, hasta que el número 999 sea introducido. El número 999 no debe ser registrado.
# 2. Después de que el usuario termine de ingresar los números, el script debe preguntarle si desea ver los números introducidos. La respuesta debe ser sí (s/S) o no (n/N). Si elige no, el script terminará.
# 3. Si el usuario elige sí (s/S), el script debe preguntarle el orden en el que quiere ver los números:
# o O (Orden de ingreso): Los números se mostrarán en el orden en que fueron introducidos.
# o A (Ascendente): Los números se mostrarán de menor a mayor.
# o D (Descendente): Los números se mostrarán de mayor a menor.
# 4. El script debe manejar las entradas correctamente, asegurándose de que el número 999 no se incluya en la lista de números y de que el usuario pueda elegir el tipo de orden de los números.
# 5. El archivo donde se almacenan temporalmente los números introducidos debe eliminarse al final del script.
# Mensajes:
# • Después de ingresar todos los números, se debe mostrar el siguiente mensaje: "¿Quieres ver los números introducidos?(s/n)"
# • Si el usuario elige sí, debe preguntarse: "¿ Orden de ingreso, ascendente o descendente?(o/a/d)"
# • Si el usuario elige una opción válida de orden, se mostrarán los números según esa opción. En caso de que elija una opción no válida, se debe mostrar: "Opción no válida"
# • El script terminará con el mensaje: "Hasta la vista"


# ---------------------------

#!/bin/bash

# Creamos un array para almacenar los números que irá sumando el usuario
numeros=()

# Leemos el primer número que ingresa el usuario fuera del bucle
read -p "Introduce un número (999 para terminar): " numero

# Establecemos una estructura condicional para evaluar si `numero` no es 999.
if [ "$numero" -ne 999 ]; then
  numeros+=("$numero")
fi

# Establecemos un bucle while para ingresar números
# -ne es el operador de comparación "no igual" en bash, dentro de la familia de -eq, como utilicé en ejercicios anteriores.
while [ "$numero" -ne 999 ]; do
  read -p "Introduce otro número (999 para terminar): " numero
  if [ "$numero" -ne 999 ]; then
    numeros+=("$numero")
  fi
done

# Leemos en una variable si el usuario desea ver los números que introdujo anteriormente
read -p "¿Quieres ver los números introducidos?(s/n) " ver

# Establecemos una estructura condicional para el caso en que sí (s/S) y dentro de ella, otra estructura condicional case para el orden en que quiera ver los números

if [[ "$ver" =~ ^[sS]$ ]]; then
  read -p "¿ Orden de ingreso, ascendente o descendente?(o/a/d) " orden

  case "$orden" in
    # **ACLARACIÓN**: printf se usa para imprimir texto con formato y evitar errores, en este caso, con el formato %s que indica que se imprimirá una cadena de texto, y el \n indica un salto de línea.
    # En cada case, se contempla la entrada de minúsculas y mayúsculas, por eso [oO], [aA],etc. 
    [oO])
      printf "%s\n" "${numeros[@]}"
      ;;
    [aA])
      printf "%s\n" "${numeros[@]}" | sort -n
      ;;
    [dD])
      printf "%s\n" "${numeros[@]}" | sort -nr
      ;;
    *)
      echo "Opción no válida"
      ;;
  esac
fi

# Imprimimos el mensaje de despedida
echo "Hasta la vista"

# ---------------------------


# Ejercicio 2.4: Crear un script que realice la misma pregunta tres veces: "¿Cuánto es 2 + 2?". Si el usuario responde correctamente, el script debe mostrar un mensaje de "Correcto" y finalizar. Si el usuario responde incorrectamente, el script debe indicarle cuántos intentos le quedan y permitirle intentar nuevamente. Después de tres intentos fallidos, el script debe mostrar un mensaje de "Game Over" y finalizar.
# Requisitos:
# 1. El script debe hacer la pregunta "¿Cuánto es 2 + 2?" al usuario hasta tres veces.
# 2. Si el usuario responde correctamente (es decir, si su respuesta es 4), el script debe mostrar el mensaje "CORRECTO, acertado en el intento X", donde X es el número de intentos que el usuario ha hecho. Luego, el script debe finalizar inmediatamente.
# 3. Si el usuario responde incorrectamente, el script debe indicar cuántos intentos le quedan con el mensaje "Te quedan X intentos", donde X es el número de intentos restantes.
# 4. El script debe permitir un máximo de tres intentos. Si el usuario no acierta en tres intentos, el script debe mostrar el mensaje "Game Over" y finalizar.


# ---------------------------

#!/bin/bash

# Establecemos un bucle for para contener la mayoría de las acciones del programa 
# porque ya sabemos que serán 3 veces máximo la cantidad de veces que se le deberá consultar al usuario la misma pregunta.

# Dentro de la misma condición para for, establecemos como contador `i` en 1, condición de corte en 3 y incremento en 1.

for ((i=1; i<=3; i++)); do
  read -p "¿Cuánto es 2 + 2? " respuesta

  if [ "$respuesta" -eq 4 ]; then
    echo "CORRECTO, acertado en el intento $i"
    # Agregamos sleep aquí para que el usuario tenga tiempo de leer el mensaje antes de que el programa termine con `exit`
    sleep 2
    exit 1
  else
    # En el caso de fallo, se le indica al usuario cuántos intentos le quedan, sumando la variable intentos_restantes y restando el total de intentos con la variable i.
    if [ $i -lt 3 ]; then
      intentos_restantes=$((3 - i))
      echo "Te quedan $intentos_restantes intentos"
    fi
  fi

done


# Imprimimos "Game Over" ya que si llega aquí, el usuario falló los 3 intentos
echo "Game Over"

# ---------------------------


# Ejercicio 2.5: Crear un script que lea un archivo llamado pregyresp.txt, que contiene preguntas matemáticas junto con las respuestas correctas. El script debe presentar cada pregunta al usuario, permitirle introducir una respuesta y luego comparar su respuesta con la correcta. Al final, debe mostrar el número total de aciertos.
# Descripción del archivo pregyresp.txt:
# El archivo pregyresp.txt contiene una serie de preguntas matemáticas y sus respuestas correctas, con el siguiente formato en cada línea:
# pregunta;respuesta_correcta
# Donde:
# • pregunta es una operación matemática.
# • respuesta_correcta es la solución correcta a la operación matemática.
# Formato del archivo (ejemplo):
# 2+2;4
# 3+3;6
# 4×4;16
# 3-1;2
# Requisitos:
# 1. El script debe leer el archivo pregyresp.txt línea por línea.
# 2. Para cada línea, el script debe separar la pregunta y la respuesta correcta (utilizando el delimitador ;).
# 3. El script debe mostrar la pregunta al usuario y permitirle ingresar una respuesta.
# 4. El script debe comparar la respuesta del usuario con la respuesta correcta.
# 5. El script debe contar cuántas respuestas son correctas y, al finalizar, mostrar el número total de aciertos.
# Mensajes esperados:
# • El script debe mostrar la pregunta al usuario y esperar su respuesta. Ejemplo: 2+2?
# • Si la respuesta es correcta, el script incrementará el contador de aciertos.
# • Al final, el script debe mostrar el número total de aciertos, por ejemplo: Tienes 3 aciertos


# ---------------------------

#!/bin/bash

# Inicializar contador de aciertos
aciertos=0

# Verificar si el archivo existe
if [ ! -f pregyresp.txt ]; then
  echo "El archivo pregyresp.txt no se encuentra."
  exit 1
fi

# Con la herramienta `tr` eliminamos posibles caractéres de retornos de carro, que en algunos casos no se pueden ejecutar bien en entornos Unix/Linux
tr -d '\r' < pregyresp.txt > pregyresp_tmp.txt
mv pregyresp_tmp.txt pregyresp.txt

# Leemos el archivo y guardamos las preguntas y respuestas en arrays
# `declare` es una palabra reservada de bash para declarar variables, con la flag `-a` indicamos que es un array.
declare -a preguntas
declare -a respuestas

# Leemos el archivo línea por línea
# IFS es una variable de shell que contiene los delimitadores de campo para separar entrada de texto (recordemos que en el .txt, la pregunta y la respuesta están separadas por `;` )
while IFS=';' read -r pregunta respuesta_correcta || [ -n "$pregunta" ]; do
  
  # Eliminamos espacios alrededor de la pregunta, ya que sino en muchos casos nos dará error.
  # sed es un argumento que conocía, pero su uso es complejo y tuve que consultar con otras fuentes al respecto.
  pregunta=$(echo "$pregunta" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
  respuesta_correcta=$(echo "$respuesta_correcta" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
  
  # Agregamos los resultados a los arrays para luego evaluar los aciertos
  preguntas+=("$pregunta")
  respuestas+=("$respuesta_correcta")
done < pregyresp.txt

# Procesamos cada pregunta/respuesta con un bucle `for`
for ((i=0; i<${#preguntas[@]}; i++)); do
  
  # Mostramos la pregunta al usuario
  echo -n "${preguntas[i]}? "
  read respuesta_usuario
  
  # Comparamos la respuesta del usuario con la respuesta correcta (eliminamos con sed y tr espacios del usuario y covertimos a minúsculas)
  # Luego acumulamos en `aciertos` si la respuesta es correcta
  respuesta_usuario=$(echo "$respuesta_usuario" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | tr '[:upper:]' '[:lower:]')
  respuesta_correcta=$(echo "${respuestas[i]}" | tr '[:upper:]' '[:lower:]')
  if [ "$respuesta_usuario" = "$respuesta_correcta" ]; then
    ((aciertos++))
  fi
done

# Mostramos el número total de aciertos al finalizar el juego
echo "Tienes $aciertos aciertos"


# ---------------------------


# Ejercicio 3.1: Crear un script que, dado el nombre de un archivo, determine y muestre el tipo de archivo y sus permisos. El script debe verificar si el archivo existe, identificar si es un archivo regular, directorio, archivo especial, entre otros, y además, verificar los permisos de lectura, escritura y ejecución.
# Requisitos:
# 1. El script debe pedir al usuario que ingrese la ruta de un archivo.
# 2. Si el archivo existe, el script debe:
# o Mostrar el tipo de archivo (por ejemplo, archivo de bloques, archivo de caracteres, directorio, archivo ordinario, archivo simbólico).
# o Verificar y mostrar los permisos del archivo: lectura, escritura y ejecución.
# 3. Si el archivo no existe, el script debe indicar que el archivo no existe.
# Mensajes esperados:
# 1. Si el archivo existe:
# o Indicar el tipo de archivo.
# o Indicar los permisos de lectura, escritura y ejecución si están habilitados.
# 2. Si el archivo no existe:
# o Indicar que el archivo no existe.
# Ejemplo de ejecución:
# $ ./script3.1_tipoarchivo
# Archivo: /dev/sda
# El archivo /dev/sda existe
# Es un archivo especial de bloques
# Tiene permiso de escritura
# Tiene permiso de ejecución
# Detalles del ejercicio:
# • El script debe identificar correctamente el tipo de archivo utilizando los operadores de prueba de Bash, como -e (para verificar si el archivo existe), -b (para archivos especiales de bloques), -c (para archivos de caracteres), -d (para directorios), -f (para archivos ordinarios), y -h (para archivos simbólicos).
# • El script debe verificar los permisos utilizando los operadores de prueba como -r (lectura), -w (escritura), y -x (ejecución).
# • En caso de que el archivo no exista, debe mostrar un mensaje adecuado.
# Notas adicionales:
# • El archivo puede ser un archivo regular, un directorio o un archivo especial como un archivo de bloques o caracteres.
# • Los permisos se pueden verificar en archivos regulares o directorios, pero no en todos los tipos de archivos especiales.


# ---------------------------

#!/bin/bash

# Solicitamos al usuario que ingrese la ruta del archivo
read -p "Ingresá la ruta de tu archivo: " ruta

# Verificamos si el archivo existe con una estructura condicional general y usando el operador `-e`

if [ -e "$ruta" ]; then
    echo "El archivo existe."
    
    # Verificamos el tipo de archivo con una estructura condicional específica
    if [ -f "$ruta" ]; then
        echo "El archivo es un archivo ordinario."
    elif [ -d "$ruta" ]; then
        echo "El archivo es un directorio."
    elif [ -b "$ruta" ]; then
        echo "El archivo es un archivo especial de bloques."
    elif [ -c "$ruta" ]; then
        echo "El archivo es un archivo especial de caracteres."
    elif [ -h "$ruta" ]; then
        echo "El archivo es un archivo simbólico."
    else
        echo "El archivo es de otro tipo."
    fi

    # Utilizamos una estructura condicional para verificar los permisos del archivo
    
    # Verificamos si el archivo tiene permisos de lectura
    if [ -r "$ruta" ]; then
        echo "El archivo tiene permisos de lectura."
    else
        echo "El archivo no tiene permisos de lectura."
    fi

    # Verificamos si el archivo tiene permisos de escritura
    if [ -w "$ruta" ]; then
        echo "El archivo tiene permisos de escritura."
    else
        echo "El archivo no tiene permisos de escritura."
    fi

    # Verificamos si el archivo tiene permisos de ejecución
    if [ -x "$ruta" ]; then
        echo "El archivo tiene permisos de ejecución."
    else
        echo "El archivo no tiene permisos de ejecución."
    fi
    
else
    # Si el archivo no existe, mostramos un mensaje de error
    echo "El archivo no existe."
fi


# ---------------------------

# Ejercicio 3.2: Crear un script que, dada una extensión de archivo, busque todos los archivos que coincidan con dicha extensión en el directorio actual. Para cada archivo encontrado, el script debe mostrar su nombre, el contenido del archivo y un separador de líneas.
# Requisitos:
# 1. El script debe solicitar al usuario que ingrese una extensión de archivo (por ejemplo, .txt, .log, .sh).
# 2. El script debe buscar todos los archivos en el directorio actual que tengan la extensión proporcionada.
# 3. Para cada archivo encontrado, el script debe:
# o Mostrar el nombre del archivo.
# o Mostrar el contenido del archivo.
# o Imprimir un separador de líneas consistente (por ejemplo, ====== o ==================================).
# Mensajes esperados:
# 1. Para cada archivo que coincida con la extensión:
# o El nombre del archivo.
# o El contenido del archivo.
# o Un separador de líneas.
# Ejemplo de ejecución:
# $ ./script3.2
# Extension del archivo: txt
# Nombre del archivo: archivo1.txt
# Contenido del archivo 1
# ==================================
# Nombre del archivo: archivo2.txt
# Contenido del archivo 2
# ==================================
# Detalles del ejercicio:
# • El script debe utilizar un bucle for para recorrer los archivos que coinciden con la extensión proporcionada por el usuario.
# • Para mostrar el contenido de cada archivo, se utilizará el comando cat.
# • El separador debe ser una línea de caracteres (por ejemplo, ==================================) para diferenciar claramente los contenidos de los archivos.

# ---------------------------

#!/bin/bash

# Solicitamos al usuario que ingrese una extensión de archivo
read -p "Escribí la extension del archivo que estás buscando: " extension

# Usamos un bucle `for` para buscar todos los archivos en el directorio actual que tengan la extensión proporcionada

for archivo in *.$extension; do
    # Verificamos si el archivo existe con `-f` y una estructura condicional, ya que es más preciso para archivos ordinarios (no directorios u otros)
    if [ -f "$archivo" ]; then
        # Mostramos la extensión del archivo
        echo "Extensión del archivo: $extension"
        # Mostramos el nombre del archivo
        echo "Nombre del archivo: $archivo"
        
        # Mostramos el contenido del archivo entre ===
        echo
        echo "Contenido del archivo entre ===:"
        echo "=================================="
        cat "$archivo"

        # Imprimimos un separador de líneas luego de un espacio en blanco (tuve problemas con \n en estos casos)
        echo
        echo "=================================="
    fi
done

# ---------------------------


# Ejercicio 4.1: Crear un script que combine la información de dos archivos de texto (arch1.txt y arch2.txt) para generar un archivo de salida (union.txt) con el siguiente formato:
# - En arch1.txt, cada línea contiene el nombre de un equipo de fútbol y el nombre de su estadio, separados por una coma.
# - En arch2.txt, cada línea contiene los colores del equipo y el nombre del estadio, separados por un punto y coma.
# - El script debe combinar la información de ambos archivos para generar un nuevo archivo, union.txt, donde cada línea tiene la siguiente estructura:
# [Nombre del equipo];[Colores del equipo];[Estadio]
# Requisitos:
# 1. El script debe leer ambos archivos arch1.txt y arch2.txt.
# 2. Debe combinar la información de los archivos de tal manera que:
# o Para cada línea en arch1.txt, se obtenga el nombre del equipo y el estadio.
# o Para cada equipo de arch1.txt, debe buscarse el color correspondiente de camiseta en arch2.txt, utilizando el nombre del equipo.
# o El archivo union.txt debe contener, por cada línea, el nombre del equipo, los colores del equipo y el nombre del estadio en el formato indicado.
# Ejemplo de entrada:
# arch1.txt:
# BOCA,BOMBONERA
# TALLERES,BOUTIQUE
# arch2.txt:
# AZUL Y BLANCO;TALLERES
# AZUL Y AMARILLO;BOCA
# Ejemplo de salida en union.txt:
# BOCA;AZUL Y AMARILLO;BOMBONERA
# TALLERES;AZUL Y BLANCO; BOUTIQUE
# Detalles del ejercicio:
# 1. El script debe usar un bucle para recorrer todas las líneas de arch1.txt.
# 2. Para cada equipo de arch1.txt, debe buscar su nombre en arch2.txt y extraer los colores correspondientes.
# 3. El formato de la salida debe ser el siguiente: [Equipo];[Colores];[Estadio].
# 4. El archivo union.txt debe generarse y guardarse con la información combinada.
# Notas adicionales:
# • Si un equipo de arch1.txt no tiene una coincidencia en arch2.txt, no se debe escribir nada para ese equipo.
# • El archivo union.txt debe ser creado desde cero al inicio del script (usando rm union.txt para eliminar cualquier archivo previo).
# Comportamiento esperado:
# 1. El script procesará ambos archivos.
# 2. El archivo union.txt se generará correctamente con la información combinada en el formato adecuado.
# 3. El script debe ser capaz de manejar archivos con múltiples líneas y combinar la información correctamente.

# ---------------------------

#!/bin/bash

# **Aclaración:**Este es un caso similar a 2.5 en cuanto a la "lectura" de archivos

# Eliminamos el archivo de salida si ya existe
rm -f union.txt

# Verificamos que los archivos de entrada existan
if [ ! -f "arch1.txt" ] || [ ! -f "arch2.txt" ]; then
    echo "Error: Uno o ambos archivos de entrada no existen."
    exit 1
fi

# Procesamos cada línea del archivo arch1.txt, traido desde la linea `done < arch1.txt`
while IFS=',' read -r equipo estadio; do

    # Eliminamos los espacios en blanco al principio y final
    equipo=$(echo "$equipo" | tr -d ' ')
    estadio=$(echo "$estadio" | tr -d ' ')
    
    # Buscamos la línea en arch2.txt (traido con `done < arch2.txt`) que contiene el equipo
    # `colores` termina almacenando los colores luego de la ejecución del while, por eso creamos la variable antes
    colores=""
    while IFS=';' read -r color equipo_arch2; do
        # Eliminar espacios en blanco al principio y final
        equipo_arch2=$(echo "$equipo_arch2" | tr -d ' ')
        
        if [ "$equipo" = "$equipo_arch2" ]; then
            colores=$color
            break # break evita lectura de líneas innecesarias del archivo arch2.txt
        fi
    done < arch2.txt
    
    # Si se encontraron los colores, se escribe la línea en el archivo de salida
    if [ -n "$colores" ]; then
        echo "$equipo;$colores;$estadio" >> union.txt
    fi
done < arch1.txt



# Mensaje final en donde le indicamos al usuario que el proceso fue completado
# Mostramos con `cat` el contenido del archivo `union.txt` así el usuario no lo tiene que abrir por fuera

echo "Procesamiento completado. Contenido del archivo union.txt:"

echo "-------------------------------------------------------"
echo ""

cat union.txt

# ---------------------------


# Ejercicio 4.2: Crear un script de gestión de una agenda de clubes, donde se puedan realizar diversas acciones sobre un archivo llamado agenda.txt. Este archivo contiene los siguientes datos de cada club: nombreclub, provincia, localidad, codigoclub.
# El script debe ofrecer un menú interactivo con las siguientes opciones:
# 1. Ver club: Permite buscar y ver los datos de un club existente.
# 2. Gestionar: Permite realizar acciones de gestión sobre los clubes, que incluyen:
# o Insertar un nuevo club.
# o Eliminar un club existente.
# o Modificar los datos de un club existente.
# 3. Salir: Termina la ejecución del script.
# Detalles del ejercicio:
# 1. Menú principal:
# o El script debe mostrar el siguiente menú:
# 1. Ver club
# 2. Gestionar
# 3. Salir
# o El usuario selecciona una opción ingresando un número.
# 1. Opción 1: Ver club
# o El usuario debe poder buscar un club por su nombre. Si el club existe en el archivo agenda.txt, se mostrarán los datos del club.
# - Si el club no existe, se debe mostrar un mensaje indicando que no se encontró el club.
# 3. Opción 2: Gestionar
# o Al seleccionar esta opción, se debe mostrar un submenú con las siguientes opciones:
# 1. Insertar club
# 2. Eliminar club
# 3. Modificar
# 4. Salir
# o El usuario puede elegir una opción para:
# ▪ Insertar un club: El script debe comprobar que el club no exista ya en la agenda. Si no existe, se le pedirá al usuario los datos del nuevo club (nombre, provincia, localidad, código) y se añadirá al archivo agenda.txt.
# ▪ Eliminar un club: El script debe comprobar si el club existe. Si existe, el club será eliminado del archivo agenda.txt.
# ▪ Modificar un club: El script debe permitir modificar los datos de un club existente. Si el club existe, se eliminarán sus datos actuales y se actualizarán con la nueva información proporcionada por el usuario.
# 4. Validación de existencia:
# o El script debe comprobar la existencia de los clubes antes de realizar cualquier operación (ya sea ver, insertar, eliminar o modificar). Para ello, el nombre del club se utilizará como clave primaria, ya que se supone que no puede haber dos clubes con el mismo nombre.
# Formato de entrada en el archivo agenda.txt: nombreclub,provincia,localidad,codigoclub
# Ejemplo de archivo agenda.txt:
# TALLERES,CORDOBA,CORDOBA,123
# UNION,SANTA FE,SANTA FE,456
# Ejemplo de ejecución:
# 1. Ver club
# 2. Gestionar
# 3. Salir
# Elige una opción: 1
# Ingrese el club: TALLERES
# TALLERES,CORDOBA,CORDOBA,123
# 1. Insertar club
# 2. Eliminar club
# 3. Modificar
# 4. Salir
# Elige una opción: 1
# Ingrese el club: REAL MADRID
# Ingrese el nombre de su provincia: Madrid
# Ingrese su localidad: Madrid
# Ingrese su código: 789
# Requisitos adicionales:
# • Si un club ya existe, no se podrá insertar de nuevo y se debe informar al usuario.
# • Si el club no existe, no podrá ser eliminado ni modificado, y se debe informar al usuario de la ausencia del club.

# ---------------------------

#!/bin/bash


# Para que este script funcione, es necesario que agenda.txt esté creado previamente
# Formato: nombreclub,provincia,localidad,codigoclub

# Usamos un bucle while que contenga todo el programa. 
# `while true;` hace que el programa se esté ejecutando constantemente en la terminal hasta que el usuario cambie la condición 
while true; do

    # Limpiamos la terminal al empezar el bucle
    clear

    # Imprimimos el primer menú de opciones
    echo "===== Agenda de Clubes ====="
    echo "1. Ver club"
    echo "2. Gestionar"
    echo "3. Salir"
    echo "======================"

    # Le solicitamos al usuario que elija una opción
    read -p "Elige una opción: " opcion_principal
    
    # Creamos una estructura condicional `case` que tome todos los casos del menú
    case $opcion_principal in
        1)  
            # En el caso de la opción 1 `Ver club`:
            clear
            echo "===== Ver Club ====="
            read -p "Ingrese el club: " nombre_club
            
            # Verificamos si el club existe
            if grep -i "^${nombre_club}," agenda.txt > /dev/null; then
                grep -i "^${nombre_club}," agenda.txt
            else
                echo "El club $nombre_club no existe en la agenda."
            fi
            
            read -p "Presione Enter para continuar..."
            ;;
            
        2)  
            # Caso de opción 2 `Menú de gestión`
            # Estructura similar al `while` que contiene todo el programa
            while true; do
                clear
                echo "===== Gestión de Clubes ====="
                echo "1. Insertar club"
                echo "2. Eliminar club"
                echo "3. Modificar"
                echo "4. Salir"
                echo "======================"
                read -p "Elige una opción: " opcion_gestion
                
                # Dentro de la opción 2 del `Menú de gestión`, insertamos casos anidados o subopciones para `Menú de gestión` con `case`
                case $opcion_gestion in
                    1)  
                        #  Subopción 1 `Insertar club`
                        clear
                        echo "===== Insertar Club ====="
                        read -p "Ingrese el club: " nombre_club
                        
                        # Verificamos si el club ya existe
                        if grep -i "^${nombre_club}," agenda.txt > /dev/null; then
                            echo "El club $nombre_club ya existe en la agenda."
                        else
                            read -p "Ingrese el nombre de su provincia: " provincia
                            read -p "Ingrese su localidad: " localidad
                            read -p "Ingrese su código: " codigo
                            
                            echo "$nombre_club,$provincia,$localidad,$codigo" >> agenda.txt
                            echo "Club $nombre_club añadido correctamente."
                        fi
                        
                        read -p "Presione Enter para continuar..."
                        ;;
                        
                    2)  
                        # Subopción 2 `Eliminar club`
                        clear
                        echo "===== Eliminar Club ====="
                        read -p "Ingrese el club a eliminar: " nombre_club
                        
                        # Verificamos si el club existe
                        if grep -i "^${nombre_club}," agenda.txt > /dev/null; then
                            # Creamos un archivo temporal sin el club a eliminar
                            grep -iv "^${nombre_club}," agenda.txt > agenda_temp.txt
                            mv agenda_temp.txt agenda.txt
                            echo "Club $nombre_club eliminado correctamente."
                        else
                            echo "El club $nombre_club no existe en la agenda."
                        fi
                        
                        read -p "Presione Enter para continuar..."
                        ;;
                        
                    3)  
                        # Subopción 3 `Modificar club`
                        clear
                        echo "===== Modificar Club ====="
                        read -p "Ingrese el club a modificar: " nombre_club
                        
                        # Verificamos si el club existe
                        if grep -i "^${nombre_club}," agenda.txt > /dev/null; then
                            # Eliminamos el club
                            grep -iv "^${nombre_club}," agenda.txt > agenda_temp.txt
                            
                            # Pedimos los datos para el nuevo club
                            read -p "Ingrese el nombre de su provincia: " provincia
                            read -p "Ingrese su localidad: " localidad
                            read -p "Ingrese su código: " codigo
                            
                            # Añadimos el club con los datos actualizados
                            echo "$nombre_club,$provincia,$localidad,$codigo" >> agenda_temp.txt
                            mv agenda_temp.txt agenda.txt
                            echo "Club $nombre_club modificado correctamente."
                        else
                            echo "El club $nombre_club no existe en la agenda."
                        fi
                        
                        read -p "Presione Enter para continuar..."
                        ;;
                        
                    4)  
                        # Subopción 4 `Salir al menú principal`
                        break
                        ;;
                        
                    *)  
                        echo "Opción inválida"
                        sleep 1
                        ;;
                esac
            done
            ;;
            
        3)  
            # Opción 3 del menu principal - `Salir del programa`
            echo "Saliendo del programa..."
            exit 0
            ;;
            
        *)  
            echo "Opción inválida"
            sleep 1
            ;;
    esac
done

# ---------------------------

# Ejercicio 4.3: A partir de un archivo llamado puntuaciones.txt, que contiene el nombre de varios jugadores y sus puntuaciones actuales, el script debe permitir al usuario introducir las nuevas puntuaciones obtenidas por cada jugador en una carrera. Posteriormente, debe actualizar el archivo con las nuevas puntuaciones y mostrar la lista de jugadores ordenada de mayor a menor según sus puntuaciones totales.
# Detalles del ejercicio:
# 1. Archivo de entrada: El archivo puntuaciones.txt tiene el siguiente formato, con cada línea representando el nombre del jugador y su puntuación actual separada por una coma:
# ALONSO,12
# COLAPINTO,10
# HAMILTON,3
# 2. Proceso:
# o El script debe leer cada línea del archivo puntuaciones.txt, mostrar al usuario el nombre de cada jugador y pedirle que introduzca los puntos obtenidos por ese jugador en la carrera.
# o Luego, el script debe sumar los puntos obtenidos por el jugador a los puntos anteriores y actualizar la puntuación total de cada jugador.
# o Finalmente, el script debe reescribir el archivo puntuaciones.txt con las puntuaciones actualizadas y mostrar la lista de jugadores ordenada de mayor a menor puntuación.
# 3. Interacción con el usuario: El script debe solicitar la puntuación de cada jugador de la siguiente manera:
# Puntos de ALONSO: ___
# Puntos de COLAPINTO: ___
# Puntos de HAMILTON: ___
# 4. Salida esperada: Al finalizar la actualización de las puntuaciones, el script debe mostrar la lista de jugadores ordenada de mayor a menor puntuación, como en el siguiente ejemplo:
# HAMILTON,15
# COLAPINTO,14
# ALONSO,13
# Requisitos adicionales:
# • El archivo puntuaciones.txt debe ser actualizado con las nuevas puntuaciones.
# • La lista de jugadores debe ser mostrada ordenada de mayor a menor puntuación al final del script.

# ---------------------------

# Ejercicio 5.1: Repetir el ejercicio 4.3, pero utilizando funciones para organizar y modularizar el código. El objetivo es leer las puntuaciones de los jugadores, permitir que el usuario ingrese nuevas puntuaciones para cada uno y actualizar el archivo puntuaciones.txt con los resultados. Posteriormente, se debe mostrar el archivo de puntuaciones ordenado de mayor a menor.
# Detalles del ejercicio:
# 1. Archivo de entrada: El archivo puntuaciones.txt contiene el nombre de varios jugadores y sus puntuaciones actuales, separadas por una coma, de la siguiente forma:
# ALONSO,12
# COLAPINTO,10
# HAMILTON,3
# 2. Funciones del script:
# o lee_jugador_y_puntos(linea): Esta función recibe un número de línea como parámetro, lee esa línea del archivo puntuaciones.txt, y extrae el nombre del jugador y sus puntos actuales. Retorna el nombre del jugador y su puntuación actual.
# o actualizar_puntos(jugador, puntosantiguos, puntos): Esta función recibe el nombre del jugador, sus puntos anteriores y los nuevos puntos obtenidos. Calcula los nuevos puntos sumando los anteriores con los nuevos, y los guarda en un archivo temporal puntuaciones.temp.
# o ordenar_y_mostrar(): Esta función ordena el archivo puntuaciones.txt de mayor a menor puntuación y muestra la lista resultante.
# o procesar_puntuaciones(): Función principal que coordina todo el proceso. Recorre el archivo puntuaciones.txt, llama a las funciones correspondientes para obtener los datos de cada jugador, solicitar las nuevas puntuaciones y actualizar los registros. Finalmente, reemplaza el archivo original con los datos actualizados y llama a la función que ordena y muestra los resultados.
# 3. Interacción con el usuario: El script solicita al usuario que introduzca las nuevas puntuaciones para cada jugador. La interacción para cada jugador será similar a:
# Puntos de ALONSO: ___
# Puntos de COLAPINTO: ___
# Puntos de HAMILTON: ___
# 4. Salida esperada: Al finalizar la actualización de las puntuaciones, el script debe mostrar la lista de jugadores ordenada de mayor a menor puntuación, como en el siguiente ejemplo:
# HAMILTON,15
# COLAPINTO,14
# ALONSO,13
# Requisitos adicionales:
# • El archivo puntuaciones.txt debe ser actualizado con las nuevas puntuaciones.
# • El código debe estar modularizado utilizando funciones para mejorar la legibilidad y reutilización.
# • La lista de jugadores debe ser mostrada ordenada de mayor a menor puntuación al final del script.

# ---------------------------

# Ejercicio 6.1: Crear un script que permita gestionar usuarios en el sistema. El script debe permitir añadir nuevos usuarios y eliminar usuarios existentes, siempre y cuando el usuario que ejecute el script tenga privilegios de administrador (root). Además, se debe verificar si el usuario que se quiere añadir ya existe en el sistema antes de proceder con su creación.
# Detalles del ejercicio:
# 1. Menú principal:
# o El script debe mostrar un menú con tres opciones principales:
# ▪ 1. Información de usuario: Solicitar el nombre de un usuario y mostrar su información usando el comando finger.
# ▪ 2. Gestión de usuario: Redirigir a otro script (script20_gestion.sh) para gestionar los usuarios (añadir, eliminar, etc.).
# ▪ 3. Salir: Finalizar el programa.
# 2. Gestión de usuarios (en script20_gestion.sh):
# o El script debe mostrar un menú con tres opciones:
# ▪ A. Añadir usuario: Verificar que el usuario que ejecuta el script es root antes de permitir añadir un nuevo usuario. Además, comprobar si el usuario a añadir ya existe en el sistema antes de crearlo.
# ▪ E. Eliminar usuario: Comprobar que el usuario que ejecuta el script es root y verificar si el usuario a eliminar existe antes de proceder con su eliminación.
# ▪ V. Volver: Volver al menú principal.
# 3. Comprobaciones y validaciones:
# o Comprobación de existencia de usuario: Antes de añadir un nuevo usuario, el script debe verificar que el nombre del usuario no esté ya en el sistema (usando /etc/passwd). Si el usuario ya existe, debe mostrar un mensaje indicándolo.
# o Permisos de administrador (root): Solo los usuarios con privilegios de root deben poder añadir o eliminar usuarios. Si un usuario sin privilegios de administrador intenta realizar estas acciones, el script debe mostrar un mensaje indicando que no tiene permisos suficientes.
# 4. Interacción con el usuario:
# o Cuando se selecciona la opción de añadir un usuario, el script debe pedir el nombre del nuevo usuario y verificar si ya existe. Si no existe, se debe crear el usuario.
# o Al seleccionar la opción de eliminar un usuario, el script debe pedir el nombre del usuario a eliminar y verificar si existe en el sistema antes de proceder con la eliminación.
# o El script debe permitir al usuario volver al menú principal en cualquier momento.
# Requisitos adicionales:
# • El script debe ser sencillo de usar e interactivo.
# • Los usuarios sin privilegios de root no deben poder añadir ni eliminar usuarios.
# Ejemplo de salida:
# Menú de gestión de usuarios
# A. Añadir
# E. Eliminar
# V. Volver
# Elige una opción: A
# No tiene permiso de administrador.
# Menú de gestión de usuarios
# A. Añadir
# E. Eliminar
# V. Volver
# Elige una opción: A
# Nombre del usuario: nuevo_usuario
# Usuario nuevo_usuario añadido con éxito.
# Nota: Para poder utilizar el comando finger en el script, se puede necesitar instalarlo primero en el sistema con el siguiente comando:
# sudo apt-get install finger

# ---------------------------