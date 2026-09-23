

try:
    numero = int(input("Ingrese un numero"))
    print(f"El numero ingresado: {numero}")
    
except ValueError:
    print("Ingrese un numero valido")
    
    

# Ejercicio #1
   
menu = 0

while menu != 3:   
    try:
        menu = int(input("""
        seleccione una opcion:
        1. Sumar
        2. Restar
        3. Salir
    :                 
    """))
        
        if menu == 1: 
            n1=int(input("Ingrese primer numero: "))
            n2=int(input("Ingrese segundo numero: "))
            print(f"Resultado {n1+n2}")
            
        elif menu == 2: 
            n1=int(input("Ingrese primer numero: "))
            n2=int(input("Ingrese segundo numero: "))
            print(f"Resultado {n1-n2}")
        else:
            print("Opcion invalida")
    except ValueError:
        print("Inserte un numero valido")
                
print("Saliendo Del Sistema")                

# Ejercicio #2:


try:
    dividendo = float(input("Ingrese el dividendo: "))
    divisor = float(input("Ingrese el divisor: "))
    resultado = dividendo / divisor
    print(f"Resaultado: {dividendo} / {divisor} = {resultado}")
except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")
except ValueError:
    print("Error: ingrese unicamente valores numericos.")        
        


# Ejercicio #2:




try:
    dividendo = float(input("Ingrese el dividendo: "))
    divisor = float(input("Ingrese el divisor: "))
    resultado = dividendo / divisor
    print(f"Resaultado: {dividendo} / {divisor} = {resultado}")
except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")
except ValueError:
    print("Error: ingrese unicamente valores numericos.")        
    




# Ejercicio #3:

try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: la edad debe ser un número entero.")
else:
    if edad >= 18:
        print("Acceso permitido.")
    else:
        print("Acceso denegado: debe ser mayor de edad.")
finally:
    print("Verificación finalizada.")
    



# Ejercicio #4:  

while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0: ")
        break
    except ValueError as e:
        print(f"Entrada invalida: {e}. Intente de nuevo.")
         
print(f"NOta registrada: {nota}")         
         
        
# Ejercicio #5:

def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)

try:
    n = int(input("¿Cuántas notas va a ingresar? "))
    notas  = []
    for i in range(n):
        nota = float(input(f"  Nota {i + 1}: "))
        notas.append(nota)
    promedio = calcular_promedio(notas)
    print(f"Promedio: {round(promedio, 2)}")
except ValueError as e:
    print(f"Error: {e}")      

