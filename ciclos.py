
# Mostra un Mensaje 10 veces 

mensaje =input("Quse mensaje quieres mostrar: ")
cantidad = int(input("Cuantas veces quiere repetir el mensaje: "))


for i in range(cantidad):
    print(f" {i}: {mensaje}")
    
 

 
    
# Ejercicio 1: Mostrar la tabla de multiplicar de un número

numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")




# Ejercicio 2: Sumar los primeros n números naturales

n = int(input("Ingrese numero entero positivo: ")) 

suma = 0
for i in range(1, n + 1): 
    suma = suma + i
    
    print(f"La suma de los primeros {n} numeros naturales es: {suma}")
    



import random

numero_secreto = random.randint(1,10)
intentos = 3 

for i in range(intentos):
    numero = int(input("Adivina el numero secreto: "))
    
    if numero == numero_secreto:
        print("!Felicidades! Adivinaste el numero.")
        break
    else:
        intentos_restantes =intentos - (i + 1)        
        print(f"Te quedan {intentos - (i + 1)} intentos.")
        
        if intentos_restantes == 0 :
            print(f"El numero era {numero_secreto}")
        
        if numero > numero_secreto:
            print(f"Muy alto")
            
        if numero < numero_secreto:
            print(f"Muy bajo")                 