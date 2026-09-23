
# TALLER ERRORES 

# EJERCICIO #1

numero1  = 0
numero2  = 0
operador = ""

try:
    numero1 = int(input("Ingre el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    operador = input("Ingrese el operador (+, -, *, /): ")
    
    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2
    else:
        print("Operador no valido")
        resultado = 0
                    
    print("Resultado:", resultado)
            
except ValueError:
    print("Error: debe ingresar numeros validos. ")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero. ")    
    
# EJERCICIO #2

nombre_archivo = ""

nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    archivo = open(nombre_archivo, "r")
    print("El archivo fue encontrado. ")
    archivo.close()
except FileNotFoundError:
    print("Error: el archivo no existe. ")
    
                    
# EJERCICIO #3

from datetime import datetime

fecha = ""

fecha = input("Ingrese una fecha (DD/MM/AAAA): ")

try:
    fecha_convertida = datetime.strptime(fecha, "%d/%m/%Y")
    print("La fecha es valida. ")
    

except ValueError:
    print("Error: la fecha no tiene un formato valido.")
    
    
# EJERCICIO #4

import math

def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("El numero no puede ser negativo")
                                
    resultado = math.sqrt(n)
    return resultado

numero = float(input("Ingrese un numero: "))

try:
    resultado = raiz_cuadrada(numero)
    print ("La raiz cuadrada es:", resultado)
                                
except ValueError:
    print("Error: no se puede calcular la raiz de un numero negativo. ") 
    

    
# EJERCICIO #5

cantidad = 0
suma = 0

while True:
    dato = input("Ingrese un numero o escriba 'fin' para terminar: ")
    
    if dato == "fin":
        break
    try:
        numero = float(dato)
        suma = suma + numero
        cantidad = cantidad + 1
    except ValueError:
        print("Valor invalido. No se tendra en cuenta. ")
                                               
    if cantidad > 0:
        promedio = suma / cantidad
        
        print("Cantidad de valores aceptados:", cantidad)
        print("Promedio:", promedio)
    else:
        print("No se ingresaron valores validos. ")                                               