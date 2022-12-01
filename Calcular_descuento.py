# En una tienda se ofrecen descuentos a los clientes por navidad.

# Si la compra es menor de 1000 peso no habra descuento.

# Si la compra es mayor de 1000 y menor de 2500 tendra un descuento del 5%.

# Si la compra es mayor de 2500 y menor de 4000 tendra un descuento del 8%.

# Si la compra es mayor de 4000 y menor de 8000 tendra un descuento del 12%.

# Si la compra es mayor de 8000 tendra un descuento del 15%.

compra = int(input('Monto de la compra: '))
print(f'CALCULAR DESCUENTO'.center(50, '*'))
# Manejo de excepciones.
try:
    if compra < 1000:
        print('No se aplica ningun descuento.')

    elif compra >1000 and compra <= 2500:
        descuento = compra * 0.05
        r = (compra - descuento)
        print(f'Su compra fue de {compra} y obtuvo un descuento de {descuento}. \nSu total a pagar es: {r}')

    elif compra >2500 and compra <= 4000:
        descuento = compra * 0.08
        r = (compra - descuento)
        print(f'Su compra fue de {compra} y obtuvo un descuento de {descuento}. \nSu total a pagar es: {r}')

    elif compra >4000 and compra <= 8000:
        descuento = compra * 0.12
        r = (compra - descuento)
        print(f'Su compra fue de {compra} y obtuvo un descuento de {descuento}. \nSu total a pagar es: {r}')

    elif compra >= 8000:
        descuento = compra * 0.15
        r = (compra - descuento)
        print(f'Su compra fue de {compra} y obtuvo un descuento de {descuento}. \nSu total a pagar es: {r}')

except Exception as ex:
    print(f'ERROR: {ex}')


