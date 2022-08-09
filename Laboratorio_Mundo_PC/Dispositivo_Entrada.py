class DispotivoEntrada:
    def __init__(self, marca, tipo_entrada):
        # Atributos Protegidos llevan un solo _ y encapsulados llevan __
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    # Metodo STR
    def __str__(self):
        return f'MARCA: {self._marca} | TIPO DE ENTRADA: {self._tipo_entrada}'
