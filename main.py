"""Parqueo El Obelisco - menu en la terminal.

Nombre completo: Julio Cesar Carias Vargas
Carne: 202604158
Grupo: IS24-FP2

main.py no es una clase: crea el Parqueo, arma cada Cliente y cada
vehiculo con lo que se escribe, y repite el menu hasta que se elija 6.
"""

from cliente import Cliente
from moto import Moto
from carro import Carro
from pickup import Pickup
from parqueo import Parqueo


def leer_entero(mensaje):
    """Lee un entero. Devuelve None si lo escrito no es un numero, para
    que un texto como 'abc' no rompa el programa."""
    texto = input(mensaje).strip()
    if not texto.isdigit():
        print(f"  Dato invalido: '{texto}' no es un numero entero. "
              f"Se vuelve al menu.")
        return None
    return int(texto)


def mostrar_menu():
    print()
    print("=== Parqueo El Obelisco ===")
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Ver vehiculos estacionados")
    print("4. Buscar vehiculo por placa")
    print("5. Ver resumen del dia")
    print("6. Salir")


def opcion_entrada(parqueo):
    # El orden de los datos es el que pide el enunciado.
    tipo = input("Tipo (M, C o P): ").strip().upper()
    if tipo != "M" and tipo != "C" and tipo != "P":
        print(f"  Tipo invalido: '{tipo}'. Solo se acepta M, C o P.")
        return

    placa = input("Placa: ").strip()
    color = input("Color: ").strip()

    if tipo == "M":
        propio = leer_entero("Cilindrada (cc): ")
    elif tipo == "C":
        propio = leer_entero("Numero de puertas: ")
    else:
        propio = leer_entero("Carga (toneladas): ")
    if propio is None:
        return

    nombre = input("Nombre del dueno: ").strip()
    telefono = input("Telefono: ").strip()

    hora = leer_entero("Hora de entrada: ")
    if hora is None:
        return

    # El Cliente se arma primero y llega ya creado al vehiculo.
    dueno = Cliente(nombre, telefono)
    if tipo == "M":
        vehiculo = Moto(placa, color, dueno, propio)
    elif tipo == "C":
        vehiculo = Carro(placa, color, dueno, propio)
    else:
        vehiculo = Pickup(placa, color, dueno, propio)

    # El vehiculo llega ya creado al Parqueo.
    parqueo.registrar_entrada(vehiculo, hora)


def opcion_salida(parqueo):
    placa = input("Placa: ").strip()
    hora = leer_entero("Hora de salida: ")
    if hora is None:
        return
    parqueo.registrar_salida(placa, hora)


def opcion_buscar(parqueo):
    placa = input("Placa: ").strip()
    vehiculo = parqueo.buscar(placa)
    if vehiculo is None:
        print(f"  La placa {placa.upper()} no esta en el parqueo.")
    else:
        print(f"  {vehiculo.describir()} | entro a las "
              f"{vehiculo.hora_entrada}")


def opcion_resumen(parqueo):
    print(f"  Espacios libres ..... {parqueo.espacios_libres()} de "
          f"{parqueo.capacidad}")
    print(f"  Total recaudado ..... Q{parqueo.total_recaudado}")


parqueo = Parqueo("El Obelisco", 6)

while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ").strip()

    if opcion == "1":
        opcion_entrada(parqueo)
    elif opcion == "2":
        opcion_salida(parqueo)
    elif opcion == "3":
        parqueo.listar()
    elif opcion == "4":
        opcion_buscar(parqueo)
    elif opcion == "5":
        opcion_resumen(parqueo)
    elif opcion == "6":
        print("  Hasta luego, Don Chepe.")
        break
    else:
        print(f"  Opcion invalida: '{opcion}'. Elige del 1 al 6.")
