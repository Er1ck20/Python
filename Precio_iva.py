# Mostrar el precio del IVA de un producto

producto = input('Nombre del producto: ')
precio = int(input('Precio del producto: '))
IVA = precio * 0.10
print(f'PRODUCTO: {producto} | PRECIO: {precio} | IVA DEL PRODUCTO: {IVA}')