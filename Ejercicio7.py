# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:35:29 2020

@author: Marti
"""


tarjeta_monto = float(input("Ingrese el monto disponible en su tarjeta de credito:"))
compra = 2500
if tarjeta_monto >= compra:
    print("Tiene dinero suficiente para realizar la compra")
    print(f"Su saldo actual es de {tarjeta_monto - 2500}")
else:
    print(f"No posee dinero suficiente para realizar la compra, le faltan {compra - tarjeta_monto}")