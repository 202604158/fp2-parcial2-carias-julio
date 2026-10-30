"""Pickup: clase hija de Vehiculo."""

from vehiculo import Vehiculo


class Pickup(Vehiculo):

    MANEJO = 10    # Articulo 5: Q10 fijos de manejo por visita

    def __init__(self, placa, color, dueno, carga_ton):
        super().__init__(placa, color, dueno)   # el padre arma lo comun
        self.carga_ton = carga_ton              # dato propio del pickup

    def calcular_tarifa(self, horas):
        # Articulo 5: Q15 por hora mas Q10 de manejo.
        return 15 * horas + Pickup.MANEJO

    def describir(self):
        # Sobrescribe reutilizando al padre en vez de repetir sus datos.
        return f"Pickup | {super().describir()} | {self.carga_ton} toneladas"
