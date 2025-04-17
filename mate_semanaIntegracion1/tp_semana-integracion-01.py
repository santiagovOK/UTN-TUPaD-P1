# Idea que seleccionamos: Contador Binario / Última revisión: 2025-04-17

# Escriban un programa que, usando un ciclo, cuente desde 0 hasta 15 y muestre cada número en su representación binaria. Extensión: Utilicen un retardo (por ejemplo, con time.sleep) para simular el conteo de un circuito.

# --- 

import time # Importamos la biblioteca time para agregar la funcion `time.sleep()`.

for numero in range(0, 16):
    # Usamos `time.sleep()` para pausar 1 seg. la ejecucion del bucle en cada iteración.
    time.sleep(1)
    # Creamos una variable para almacenar el binario en tipo cadena
    binario = "" 
    # Hacemos una copia para no modificar 'numero' del `for`
    n = numero
    # Creamos una condicional doble para agregar el 0.
    if numero == 0:
        print("0 en binario es 0")
    else:
    # Dentro de la condicional, agregamos el `while` que incluye el pasaje de cada uno de los números del rango a binario.
        while n > 0:
            # Calculamos el residuo de la división por 2
            residuo = n % 2
            # Concatenamos el residuo al inicio de la cadena binaria.
            binario = str(residuo) + binario
            # Actualizamos n dividiendo por 2.
            n = n // 2
        # Imprimimos los resultados en cada iteración.    
        print(f"{numero} en binario es {binario}")

# --- 