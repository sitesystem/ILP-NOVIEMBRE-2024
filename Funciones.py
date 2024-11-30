# FUNCIONES: Tarea o acción a ejecutar específica
# SINTAXIS
'''
  def Nombre_de_la_Función(Parámetro o Argumentos):
    contenido de la función
'''
# ENTRADA Y PROCESO DE DATOS
def Operación_Sumar(num1, num2):  # La función recibe/obtiene 2 parámetros o argumentos
  # Contenido de la función
  return num1 + num2              # Retorna, regresa o devuelve un valor(es)

def Operación_Restar(num1, num2): # La función recibe/obtiene 2 parámetros o argumentos
  # Contenido de la función
  resta = num1 - num2
  print(resta)                    # Retorna, regresa o devuelve un valor(es)

# MULTIPLICAR Y DIVIDIR

# SALIDA DE DATOS
''' Invocar o mandar a llamar la función '''
fn1 = Operación_Sumar(10, 15.5)   # Se le pasan o envían 2 parámetros a la función
fn2 = Operación_Sumar("Dana", " Paola")
Operación_Restar(20, 15)

print(fn1)
print(fn2)
