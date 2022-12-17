# Crear un programa que calcule  el iva de una compra, siendo el iva del 19% total de la compra


compra = float(input('Precio de la compra: '))

# El IVA - Es el impuesto sobre el valor añadido
def IVA(impuesto):
    return f'IVA: {impuesto * 0.19}'

print(IVA(compra))