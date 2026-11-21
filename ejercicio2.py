def leer_paquetes():
    paquetes = []

    for dia in range(5):
        while True:
            try:
                cantidad = int(input(f"Ingrese los paquetes del dia {dia + 1}: "))

                if cantidad >= 0:
                    paquetes.append(cantidad)
                    break
                else:
                    print("Error: la cantidad no puede ser negativa.")

            except ValueError:
                print("Error: debe ingresar un numero entero.")

    return paquetes


def calcular_total(paquetes):
    total = 0

    for cantidad in paquetes:
        total += cantidad

    return total


def buscar_mayor(paquetes):
    mayor = paquetes[0]

    for cantidad in paquetes:
        if cantidad > mayor:
            mayor = cantidad

    return mayor


def contar_dias_mayores(paquetes):
    contador = 0

    for cantidad in paquetes:
        if cantidad > 20:
            contador += 1

    return contador


def mostrar_resultados(paquetes, total, mayor, cantidad_dias):
    print("\n--- RESULTADOS ---")
    print("Paquetes registrados:", paquetes)
    print("Total de paquetes:", total)
    print("Mayor cantidad registrada:", mayor)
    print("Dias con mas de 20 paquetes:", cantidad_dias)


def main():
    paquetes = leer_paquetes()

    total = calcular_total(paquetes)
    mayor = buscar_mayor(paquetes)
    cantidad_dias = contar_dias_mayores(paquetes)

    mostrar_resultados(paquetes, total, mayor, cantidad_dias)


main()