
Consumo = int(input('Consumo: '))

if Consumo == 100:
    print(''.center(25, '='))
    print('Factura de Consumo'.center(25, '-'))

    descuento = 0.10
    impuesto = 0.19

    descuento_aplicado = Consumo * descuento
    monto_descuento = Consumo - descuento_aplicado
    impuesto_aplicado = monto_descuento * impuesto

    total = (Consumo - descuento_aplicado) + impuesto_aplicado
    print(f'''
    Consumo: {Consumo}
    Descuento: {descuento_aplicado}
    Impuesto: {impuesto_aplicado}
    Total a pagar: {total}
    ''')
    print(''.center(25, '='))


elif Consumo > 100 and Consumo < 200:
    print(''.center(25, '='))
    print('Factura de Consumo'.center(25, '-'))

    descuento = 0.20
    impuesto = 0.19

    descuento_aplicado = Consumo * descuento
    monto_descuento = Consumo - descuento_aplicado
    impuesto_aplicado = monto_descuento * impuesto

    total = Consumo - descuento_aplicado + impuesto_aplicado
    print(f'''
    Consumo: {Consumo}
    Descuento: {descuento_aplicado}
    Impuesto: {impuesto_aplicado}
    Total a pagar: {total}
    ''')

    print(''.center(25, '='))

elif Consumo > 200:
    print(''.center(25, '='))
    print('Factura de Consumo'.center(25, '-'))

    descuento = 0.30
    impuesto = 0.19

    descuento_aplicado = Consumo * descuento
    monto_descuento = Consumo - descuento_aplicado
    impuesto_aplicado = monto_descuento * impuesto

    total = Consumo - descuento_aplicado + impuesto_aplicado
    print(f'''
    Consumo: {Consumo}
    Descuento: {descuento_aplicado}
    Impuesto: {impuesto_aplicado}
    Total a pagar: {total}
    ''')

    print(''.center(25, '='))