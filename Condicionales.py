# Importar una librería
from decimal import Decimal, ROUND_HALF_UP

# MAYORÍA DE EDAD
edad = Decimal(input("Escribe tu edad: "))
edad = edad.quantize(Decimal('0.0'), rounding=ROUND_HALF_UP) # round(edad, 1) # Función para redondear (Parámetros o Argumentos)
print(edad)

if (edad >= 18 and edad <= 120):    # RANGO VÁLIDO 18 HASTA 120
  print("MAYOR DE EDAD")
elif (edad >= 0 and edad < 18):    # RANGO VÁLIDO 0 A 17
  print("MENOR DE EDAD")
elif (edad < 0 or edad > 120):      # VALORES NO VÁLIDOS MENOR QUE 0 O MAYOR QUE 120
  print("EDAD NO VÁLIDA")
else:
  print("OTRA COSA")

# Comentar Ctrl. + K  Ctrl. + C
# Descomentar Ctrl. + K Ctrl. + U

'''
EJERCICIO 1.
APROBADO            MAYOR A 6 Y MENOR O IGUAL A 10
APENAS APROBADO     CALIFICACIÓN DE 6
REPROBADO           MENOR QUE 6 Y MAYOR O IGUAL QUE CERO
PROMEDIO INVÁLIDO   MENOR QUE 0 O MAYOR QUE 10
'''
