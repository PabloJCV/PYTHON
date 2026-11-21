# calculadora de salario
nombre_empleado = input("Ingrese el nombre del empleado: ")
horas_laboradas = float(input("Ingrese cantidad de horas laboradas: "))
hora_laboral = float(input("ingrese monto de su hora laboral: "))
impuesto = 10.83 / 100  # Convertir porcentaje a decimal

# Calculo del salario

salario_bruto = horas_laboradas * hora_laboral

rebajo = salario_bruto * impuesto

salario_neto = salario_bruto - rebajo

print("\n----- Detalle del salario -----")
print(f"Empleado: {nombre_empleado}")
print(f"Salario bruto: ₡{salario_bruto:.2f}")
print(f"Rebajo CCSS (10.83%): ₡{rebajo:.2f}")
print(f"Salario neto: ₡{salario_neto:.2f}")