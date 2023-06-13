def calcular_propina(cantidad_factura, porcentaje_propina):
    propina = cantidad_factura * (porcentaje_propina / 100)
    total = cantidad_factura + propina
    return propina, total

def main():
    cantidad_factura = float(input("Ingrese la cantidad de la factura: $"))
    porcentaje_propina = float(input("Ingrese el porcentaje de propina a calcular: "))
    propina, total = calcular_propina(cantidad_factura, porcentaje_propina)
    print("Propina: $", propina)
    print("Total a pagar (incluyendo propina): $", total)

if __name__ == "__main__":
    main()
