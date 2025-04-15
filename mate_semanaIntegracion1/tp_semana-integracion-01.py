# Idea: Contador Binario

# Última revisión: 2025-04-15

# Escriban un programa que, usando un ciclo, cuente desde 0 hasta 15 y muestre cada número en su representación binaria. 
# Extensión: Utilicen un retardo (por ejemplo, con time.sleep) para simular el conteo de un circuito.
import time #se importa la biblioteca time para agregar la funcion time.sleep().
for numero in range(0, 16):
    time.sleep(1) #esta funcion pausa 1 seg la ejecucion del bucle.
    # Creamos una variable para almacenar el binario en tipo cadena
    binario = "" 
    # Hacemos una copia para no modificar 'numero' del for
    n = numero
    # creamos una condicional doble para agregar el 0.
    if numero == 0:
        print("0 en binario es 0")
    else:
        while n > 0:
            residuo = n % 2
            binario = str(residuo) + binario
            n = n // 2
        print(f"{numero} en binario es {binario}")


# NOTAS

# Faltaría incluir el 0 dentro del rango
# Deberíamos usar time.sleep ya que lo señala la consigna misma
# Si van a usar AI, traten de documentar más o menos qué es lo que hacen (y por qué necesitaban preguntar eso) 
# así vemos como lo agregamos a la fundamentación
