"""Carro: clase hija de Vehiculo."""

from vehiculo import Vehiculo


class Carro(Vehiculo):

    TOPE = 60      # Articulo 5: maximo Q60 por visita

    def __init__(self, placa, color, dueno, puertas):
        super().__init__(placa, color, dueno)   # el padre arma lo comun
        self.puertas = puertas                  # dato propio del carro

    def calcular_tarifa(self, horas):
        # Articulo 5: Q10 por hora, pero nunca mas de Q60 por visita.
        monto = 10 * horas
        if monto > Carro.TOPE:
            monto = Carro.TOPE
        return monto

    def describir(self):
        # Sobrescribe reutilizando al padre en vez de repetir sus datos.
        return f"Carro | {super().describir()} | {self.puertas} puertas"
