
# Ejercicio 1: Suma de dos números

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2   # Se calcula la suma

print(f"La suma es: {suma}")


# Ejercicio 2: Área de un rectángulo

base   = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

area = base * altura   # fórmula: base × altura

print(f"El área del rectángulo es: {area}")

# Ejercicio 3: Conversión de minutos a horas y minutos

minutos_totales = int(input("Ingrese la cantidad de minutos: "))

horas   = minutos_totales // 60   # división entera → horas completas
minutos = minutos_totales % 60    # módulo → minutos restantes

print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")

# Ejercicio 4: Cálculo del precio con descuento

precio    = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento / 100)   # valor que se descuenta
precio_final    = precio - valor_descuento      # precio con descuento

print(f"El precio final a pagar es: {precio_final}") 

# Ejercicio 5: Intercambio de valores entre dos variables

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

auxiliar = a   # guardar temporalmente el valor de a
a = b          # a toma el valor de b
b = auxiliar   # b toma el valor original de a

print(f"Después del intercambio: a = {a} , b = {b}") 

print("=" * 30)


# SOLUCION EJERCICIOS DE CLASE TALLER # 1 

# Ejercicio #1 Perimetro de un terreno 

largo = float(input("Ingrese el largo del terreno: "))
ancho = float(input("Ingrese el ancho del terreno: "))

perimetro = 2 * (largo+ ancho) 

print(f"El perímetro del terreno es: {perimetro}")
  

# Ejercicio #2 Promedio de tres numeros 

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: ")) 
num3 = float(input("Ingrese el tercer numero: ")) 

promedio = (num1 + num2 + num3) /3 

print(f"El promedio de los tres numeros es: {promedio}")
 
# Ejercicio #3 Mensaje Presentación 

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: ")) 

print(f"Hola, mi nombre es {nombre} y tengo {edad} años") 

# Ejercicio #4 Conversión de COP a USD 

pesos = float(input("Ingrese la cantidad en pesos colombianos (COP): ")) 
tasa_usd = 4000 

dolares = pesos / tasa_usd 

print(f"${pesos} COP equivalen a ${dolares} USD")

# Ejercicio #5 Conversión 

segundos_totales = int(input("Ingrese la cantidad total de segundos: "))
horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos_restantes = segundos_totales % 60 

print(f"{segundos_totales} segundos equivalen a: {horas} horas, {minutos} minutos y {segundos_restantes} segundos.") 

