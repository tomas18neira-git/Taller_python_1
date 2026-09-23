# TRABAJO EJECICIO # 5

# Datos del empleado

nombre = input("Ingrese el nombre del empleado: ")
horas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de cada hora: "))

# Validar

if horas <= 0 or valor_hora <= 0:
     print("Los valores deben ser positivos")

if horas <= 160:
     horas_normales = horas
     horas_extra = 0
else:
     horas_normales = 160
     horas_extra = horas - 160

# Pago de horas

pago_normal = horas_normales * valor_hora
pago_extra = horas_extra * valor_hora * 1.25

# Salario bruto

salario_bruto = pago_normal + pago_extra

# Descuento

descuento = salario_bruto * 0.08

# Salario neto

salario_neto = salario_bruto - descuento

# Mostrar resultados

print(f"""
-Empleado:......................{nombre}
-Horas normales:................{horas_normales}
-Horas extra:...................{horas_extra}
-Pago hora normal:..............{valor_hora}
-Pago hora extra:...............{valor_hora * 1.25}
-Salario bruto:.................{salario_bruto}
-Descuento:.....................{descuento}
-Salario neto:..................{salario_neto}

""")