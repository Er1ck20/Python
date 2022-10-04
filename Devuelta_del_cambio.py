# Programa para calcular cuando se le debe devolver al cliente al comprar un articulo.

# DATOS:
# 1. El cambio se debe entregar al cliente, si el paga efectuado es mayor que el precio del producto.
# 2. Que pasa si el cliente paga exactamente lo mismo que vale el producto?
# 3. La cantidad del pago que falta por pagar, si el paga es menor a lo que vale el producto.

ARTICULO = float(input('Precio del Articulo: ')) 
DINERO = float(input('Pago: '))

# Devolver el cambio si el pago es mayor a lo que vale el producto.
if DINERO > ARTICULO:
    R = ARTICULO - DINERO
    print(f'Usted ha recibido un cambio de: {R} al momento de comprar el articulo')

# Pago exacto
elif ARTICULO == DINERO:
    print(f'Pago exacto.')

# Pago menos
elif DINERO < ARTICULO:
    R = DINERO - ARTICULO
    print(f'Le falta {R}')
else:
    print('ERROR')