
# Ejercicio en clase #1

print("====Tienda Merca + ====\n")

#Solicitar las variables
producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad a comprar: "))
precio = float(input("Ingrese el precio unitario del producto : "))

#Crear variables para calcular
subtotal = cantidad * precio
iva = subtotal * 0.19
total = subtotal + iva

print("\n === RESUMEN DE COMPRA === \n")
print(f"""
      -Producto...................{producto}
      -Cantidad...................{cantidad}
      -Precio Unitario............{precio}
      -Subtotal...................{subtotal}
      -IVA (19%)..................{iva}
      -Total Pagar................{total}
      
""")

# Preguntar si quiere incluir propina
propina = input("Desea incluir propina ?: ")
if propina == "si" or propina == "SI"  or propina == "Si" :
    valor_propina = subtotal * 0.10
    total_final = total + valor_propina
    
    print("\n === RESUMEN DE COMPRA === \n")

    print(f"""
      
      -Subtotal...................{subtotal}
      -Valor Propina..............{valor_propina}
      -IVA (19%)..................{iva}
      -Total Pagar................{total}
      
""")

elif propina == "no" or propina == "NO" or propina == "No" :
    print("Gracias por su compra TACAÑO: ")

else:
    print("Opcion no valida, por favor ingrese 'si' o 'no'")
        
 
