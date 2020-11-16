# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:34:41 2020

@author: Marti
"""

def mensaje(mensaje):
    lista_numeros = []
    for caracter in mensaje:
        if caracter.isdigit():
            lista_numeros.append(caracter)

    print(lista_numeros)
    
    
mensaje("Quedan 5 meses para que se termine el 2020")