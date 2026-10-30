"""Cliente: el dueño de un vehículo.

Llega ya creado al vehículo (asociación "conoce a" del diagrama): el
Vehiculo no construye a su Cliente, solo guarda el que le entregan.
"""


class Cliente:

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def describir(self):
        return f"{self.nombre} ({self.telefono})"
