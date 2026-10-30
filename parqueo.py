"""Parqueo: agrupa los vehiculos estacionados y aplica el reglamento.

Agregacion "agrupa a" del diagrama: el Parqueo NO construye vehiculos,
recibe los que ya vienen armados y los guarda en su lista.
"""


class Parqueo:

    HORA_APERTURA = 6      # Articulo 2
    HORA_CIERRE = 22       # Articulo 2

    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.estacionados = []       # empieza vacia
        self.total_recaudado = 0

    def espacios_libres(self):
        return self.capacidad - len(self.estacionados)

    def buscar(self, placa):
        # Articulo 3: se compara en mayusculas, asi que da igual como se
        # escriba la placa al buscarla.
        placa = placa.strip().upper()
        for vehiculo in self.estacionados:
            if vehiculo.placa == placa:
                return vehiculo
        return None

    # ------------------------------------------------------------------
    # Entrada: revisa los articulos 1, 2 y 3 ANTES de tocar nada.
    # ------------------------------------------------------------------
    def registrar_entrada(self, vehiculo, hora):
        if self.espacios_libres() <= 0:
            print(f"  RECHAZADO - Articulo 1: el parqueo esta lleno "
                  f"({self.capacidad} de {self.capacidad} ocupados).")
            return False

        if hora < Parqueo.HORA_APERTURA or hora > Parqueo.HORA_CIERRE:
            print(f"  RECHAZADO - Articulo 2: la hora {hora} esta fuera del "
                  f"horario de atencion ({Parqueo.HORA_APERTURA} a "
                  f"{Parqueo.HORA_CIERRE}).")
            return False

        if self.buscar(vehiculo.placa) is not None:
            print(f"  RECHAZADO - Articulo 3: la placa {vehiculo.placa} ya "
                  f"esta adentro.")
            return False

        vehiculo.hora_entrada = hora
        self.estacionados.append(vehiculo)
        print(f"  OK - entro a las {hora}: {vehiculo.describir()}")
        print(f"       Espacios libres: {self.espacios_libres()}")
        return True

    # ------------------------------------------------------------------
    # Salida: revisa los articulos 2 y 4, cobra y saca el vehiculo.
    # ------------------------------------------------------------------
    def registrar_salida(self, placa, hora):
        vehiculo = self.buscar(placa)
        if vehiculo is None:
            print(f"  RECHAZADO - la placa {placa.strip().upper()} no esta "
                  f"en el parqueo.")
            return 0

        if hora < Parqueo.HORA_APERTURA or hora > Parqueo.HORA_CIERRE:
            print(f"  RECHAZADO - Articulo 2: la hora {hora} esta fuera del "
                  f"horario de atencion ({Parqueo.HORA_APERTURA} a "
                  f"{Parqueo.HORA_CIERRE}).")
            return 0

        if hora < vehiculo.hora_entrada:
            print(f"  RECHAZADO - Articulo 4: no puede salir a las {hora} si "
                  f"entro a las {vehiculo.hora_entrada}.")
            return 0

        # Articulo 4: se cobra por hora completa, con un minimo de 1 hora.
        horas = hora - vehiculo.hora_entrada
        if horas < 1:
            horas = 1

        # Polimorfismo: cada tipo de vehiculo calcula su propia tarifa.
        monto = vehiculo.calcular_tarifa(horas)
        self.total_recaudado = self.total_recaudado + monto
        self.estacionados.remove(vehiculo)

        print(f"  OK - salio a las {hora}: {vehiculo.describir()}")
        print(f"       {horas} hora(s) --> COBRAR Q{monto}")
        print(f"       Espacios libres: {self.espacios_libres()}")
        return monto

    def listar(self):
        if len(self.estacionados) == 0:
            print("  No hay vehiculos estacionados.")
            return
        print(f"  Vehiculos estacionados: {len(self.estacionados)}")
        for vehiculo in self.estacionados:
            print(f"    - {vehiculo.describir()} | entro a las "
                  f"{vehiculo.hora_entrada}")
