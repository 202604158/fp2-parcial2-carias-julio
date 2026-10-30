"""Moto: clase hija de Vehiculo."""

from vehiculo import Vehiculo


class Moto(Vehiculo):

    def __init__(self, placa, color, dueno, cilindrada):
        super().__init__(placa, color, dueno)   # el padre arma lo comun
        self.cilindrada = cilindrada            # dato propio de la moto

    def calcular_tarifa(self, horas):
        # Articulo 5: Q5 por hora, sin tope.
        return 5 * horas

    def describir(self):
        # Sobrescribe reutilizando al padre en vez de repetir sus datos.
        return f"Moto | {super().describir()} | {self.cilindrada} cc"
