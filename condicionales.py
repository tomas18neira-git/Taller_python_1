
# Repaso Clase Pasada 
 
var_nombre = input("Por favor ingrese su nombre: ")

#Variable numerica (int = numero entero float =decimales)

var_edad =int(input(f"{var_nombre} Por favor ingresa tu edad: "))

# Validar si la edad es > = 18. y mostrar un mensaje que diga que es mayor 

if var_edad >= 18 :
    print(f"{var_nombre} usted es mayor de edad")

else: 
    print(f"{var_nombre} usted es menor de edad")
    





# Ejercicio 1: Determinar si un número es positivo, negativo o cero

numero = float(input("Ingrese un número: "))

if numero > 0:
   print(f"El numero : {numero} es Positivo")
    
elif numero < 0 : 
    print(f"El numero : {numero} es Negativo")
    
else:
    print(f"El numero : {numero} es Cero") 
    
    

   
 # Ejercicio 3: Determinar si un número es par o impar

numero = int(input("Por favor ingrese un numero: "))

if numero % 2 !=0:
    print(f"El numero {numero} es Impar ")
else:
    print(f"El numero {numero} es Par ")
   
   

# Ejercicio 4: Clasificar una nota académica

nota = float(input("Ingrese la nota obtenida (0.0 a 5.0) : "))

if nota > 5.0:
    print("Nota Inavlida")
elif nota > 4.5:
    print("Desempeño superior")
elif nota > 3.5:
    print("Desemepeño alto")
elif nota > 3.0:
    print("Desempeño basico")
elif nota <0:
    print("Nota invalida")
else:
    print("Desempeño bajo")
    
# Ejercicio 5: Determinar el mayor de tres números

n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))

if n1 > n2 and n1 > n3:
    mayor = n1
elif n2 > n1 and n2 > n3:
    mayor = n2
    

