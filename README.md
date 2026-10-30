# Parqueo El Obelisco — Segunda Evaluación Parcial

**Nombre completo:** Julio César Carías Vargas
**Carné:** 202604158
**Grupo:** IS24-FP2
**Curso:** Fundamentos de Programación 2 · Segundo semestre 2026
**Docente:** Ing. Brandon Antony Chitay Coutiño

## Cómo se ejecuta

```
python3 main.py
```

No necesita instalar nada: solo la biblioteca estándar de Python 3.

## Archivos

| Archivo | Qué contiene |
|---|---|
| `cliente.py` | `Cliente`: nombre y teléfono del dueño, con `describir()`. |
| `vehiculo.py` | `Vehiculo`: clase abstracta (hereda de `ABC`), con `calcular_tarifa()` marcado `@abstractmethod`. |
| `moto.py` | `Moto`: atributo propio `cilindrada`. Q5 por hora, sin tope. |
| `carro.py` | `Carro`: atributo propio `puertas`. Q10 por hora, máximo Q60 por visita. |
| `pickup.py` | `Pickup`: atributo propio `carga_ton`. Q15 por hora más Q10 de manejo. |
| `parqueo.py` | `Parqueo`: agrupa los vehículos estacionados y aplica el reglamento. |
| `main.py` | El menú de la terminal con `input()`. No es una clase. |

## Relaciones del diagrama

- **Herencia:** `Moto`, `Carro` y `Pickup` son tipos de `Vehiculo`, que es abstracta. Cada hija llama a `super().__init__(...)`, sobrescribe `calcular_tarifa()` con su tarifa del Art. 5 y sobrescribe `describir()` reutilizando el del padre con `super().describir()`.
- **Asociación ("conoce a"):** el `Vehiculo` guarda en `dueno` el `Cliente` que recibe ya creado; no lo construye.
- **Agregación ("agrupa a"):** el `Parqueo` recibe vehículos ya creados y los guarda en `estacionados`; no los construye.

## El reglamento

| Artículo | Regla | Dónde se revisa |
|---|---|---|
| 1 · Capacidad | 6 espacios; si está lleno no entra nadie más. | `Parqueo.registrar_entrada()` |
| 2 · Horario | Horas enteras de 6 a 22, en entrada y en salida. | `registrar_entrada()` y `registrar_salida()` |
| 3 · Placa única | Una placa no se repite adentro; se guarda en mayúsculas. | `Vehiculo.__init__()` y `registrar_entrada()` |
| 4 · Salida | Nadie sale antes de su hora de entrada; se cobra por hora completa, mínimo 1 hora. | `Parqueo.registrar_salida()` |
| 5 · Tarifas | Moto Q5/h, Carro Q10/h con tope Q60, Pickup Q15/h más Q10. | `calcular_tarifa()` de cada hija |

Cada rechazo imprime el artículo que falló y no cambia el estado del parqueo.

## El menú

```
=== Parqueo El Obelisco ===
1. Registrar entrada
2. Registrar salida
3. Ver vehiculos estacionados
4. Buscar vehiculo por placa
5. Ver resumen del dia
6. Salir
```

La opción 1 pide los datos en este orden: tipo (`M`, `C` o `P`), placa, color, dato propio, nombre del dueño, teléfono y hora de entrada.

Los datos inválidos no rompen el programa: una opción que no existe, un tipo distinto de `M`, `C` o `P`, o un texto donde va un número muestran un mensaje y vuelven al menú. Los números se revisan con `texto.isdigit()` antes de convertirlos con `int()`.
