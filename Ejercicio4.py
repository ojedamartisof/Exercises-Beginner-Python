# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:43:36 2020

@author: Marti
"""


def mayor_prod():
    lista_numeros = []
    for i in range(4):
        num = int(input("Ingrese un número: "))
        lista_numeros.append(num)
    lista_numeros.sort()
    for numero in lista_numeros:
        if numero == 0:
            lista_numeros.pop(numero)
            mayor_prod = lista_numeros[-2] * lista_numeros[-1]
        else:
            mayor_prod = lista_numeros[-2] * lista_numeros[-1]
    print(mayor_prod)
