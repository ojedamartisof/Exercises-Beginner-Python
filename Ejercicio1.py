# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:23:53 2020

@author: Marti
"""


def min_seg(horas):
    minutos = horas * 60
    seg = horas * 3600
    horas = int(input("Ingrese una hora"))
    print(f"{horas} horas son {minutos} minutos y {seg} segundos.")

min_seg(12)
min_seg(34)