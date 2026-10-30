"""Vehiculo: clase padre ABSTRACTA de los tres tipos del parqueo.

Nadie estaciona un "vehículo a secas": todo lo que entra es una moto, un
carro o un pickup. Por eso hereda de ABC y calcular_tarifa es abstracto:
Python se niega a construir un Vehiculo directo.
"""

from abc import ABC, abstractmethod


class Vehiculo(ABC):

    def __init__(self, placa, color, dueno):
        # Articulo 3: la placa se guarda en mayusculas, para que
        # p-222bbb y P-222BBB sean la misma.
        self.placa = placa.upper()
        self.color = color
        self.dueno = dueno          # el Cliente llega ya creado
        self.hora_entrada = None    # la pone el Parqueo al registrar la entrada

    # ------------------------------------------------------------------
    # Metodo abstracto: cada tipo cobra distinto (Articulo 5), asi que el
    # padre no puede saber la tarifa. Obliga a que cada hija la defina.
    # ------------------------------------------------------------------
    @abstractmethod
    def calcular_tarifa(self, horas):
        pass

    def describir(self):
        # Usa el describir() del Cliente en lugar de armar el nombre aqui.
        return f"{self.placa}, color {self.color}, dueño: {self.dueno.describir()}"
