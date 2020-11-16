"""
Crear una función que calcule cuántos litros de nafta gasta un auto que consume 2 litros x 100km,
en un viaje ida y vuelta MdP-Bue si la distancia es de 400km.
Luego crear una función que, a partir de esos datos,
devuelva cuánto significa eso en pesos si el litro de nafta está 60$.
"""

# Solución

def litros():
    litros_por_100km = 2
    km = 100
    distancia = 400
    litros_gastados = litros_por_100km * distancia / km
    return litros_gastados


def monto(consumo):
    precio_por_litro = 60
    monto_gastado = precio_por_litro * consumo
    print(monto_gastado)

print(litros())
monto(litros())