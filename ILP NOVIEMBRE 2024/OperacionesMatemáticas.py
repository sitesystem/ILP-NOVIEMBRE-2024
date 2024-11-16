# Operaciones Matemáticas: Suma, Resta, Mult, Div, Potencia, Raíz cuadrada, Raíz cúbica, Módulo

# IMPORTAR LAS LIBRERIAS O BIBLIOTECAS QUE CONTIENEN FUNCIONES
import math

# DECLARAR O CREAR LAS VARIABLES O CONSTANTES
número_1 = 0 # valor inicial
número_2 = 0 # valor inicial

# ENTRADAS DE DATOS
número_1 = float(input("Ingresa un número: "))
número_2 = float(input("Ingresa otro número: "))

# PROCESO (realizan las operaciones o cálculos matemáticos y/o lógicos)
suma = número_1 + número_2 # SUMA
resta = número_1 - número_2	# RESTA
multiplicación = número_1 * número_2 # MULTIPLICACIÓN
división = número_1 / número_2 # DIVISIÓN

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2) # Las funciones tienen paréntesis donde se colocan Parámetros o Argumentos
cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = math.sqrt(16)
raíz_cuadrada_2 = pow(16, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo_1 = 10 % 2
módulo_residuo_2 = número_1 % número_2

# SALIDAS DE DATOS (IMPRIMIR O MOSTRAR EN PANATALLA)
print("LA SUMA ES =", suma) # CONCATENACIÓN (unión) CON LA COMA (,)
print('LA RESTA ES = ' + str(resta)) # CONCATENACIÓN (unión) CON (+) POR CASTEO (Convertir un tipo de dato a otro tipo de dato)
print(f"LA MULTIPLICACIÓN ES = {multiplicación}") # INTERPOLACIÓN DE TEXTO
print("LA DIVISIÓN ES =", división)
print("LA POTENCIA1 DE n1 ELEVADO A n2 =", potencia_1)
print("LA POTENCIA2 DE n1 ELEVADO A n2 =", potencia_2)
print("LA RAÍZ CUADRADA DE 16 ES =", raíz_cuadrada_1)
print("MÓDULO 1 O RESIDUO ES =", módulo_residuo_1)
print("MÓDULO 2 O RESIDUO ES =", módulo_residuo_2)
