# Operaciones Matemáticas: Suma, Resta, Mult, Div, Potencia, Raíz cuadrada, Raíz cúbica, Módulo

# DECLARAR O CREAR LAS VARIABLES O CONSTANTES
número_1 = 0 # valor inicial
número_2 = 0 # valor inicial

# ENTRADAS
número_1 = float(input("Ingresa un número: "))
número_2 = float(input("Ingresa otro número: "))

# PROCESO (realizan las operaciones o cálculos matemáticos y/o lógicos)
suma = número_1 + número_2 # SUMA
resta = número_1 - número_2	# RESTA
multiplicación = número_1 * número_2 # MULT

# SALIDAS (IMPRIMIR O MOSTRAR EN PANATALLA)
print("LA SUMA ES =", suma) # CONCATENACIÓN (unión) CON LA COMA (,)
print('LA RESTA ES = ' + str(resta)) # CONCATENACIÓN (unión) CON (+) POR CASTEO (Convertir un tipo de dato a otro tipo de dato)
print(f"LA MULTIPLICACIÓN ES = {multiplicación}") # INTERPOLACIÓN DE TEXTO
