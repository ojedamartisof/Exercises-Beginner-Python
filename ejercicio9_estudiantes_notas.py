"""
Crear un diccionario con 10 estudiantes y sus respectivas notas.
Luego crear una función que nos informe
los estudiantes aprobados (nota >= 7),
los estudiantes desaprobados (4 <= nota < 7) y los estudiantes aplazados (0 <= nota < 4).

"""

notas = {}
print("Ingrese el nombre de cada estudiante y su nota correspondiente")
for i in range(10):
    nombre = input("Nombre: ")
    nota = int(input("Nota: "))
    notas[nombre] = nota

def informe_notas():
    aprobados = {}
    desaprobados = {}
    aplazados = {}
    for nombre_clave, nota_valor in notas.items():
        if nota_valor >= 7:
            aprobados[nombre_clave] = nota_valor
        elif 4 <= nota_valor < 7:
            desaprobados[nombre_clave] = nota_valor
        elif 0 <= nota_valor < 4:
            aplazados[nombre_clave] = nota_valor
        else:
            print("La nota debe estar entre 0 y 10, revisar.")
    if len(aprobados) != 0:
        print(f"Los aprobados son: {aprobados}")
    if len(desaprobados) != 0:
        print(f"Los desaprobados son: {desaprobados}")
    if len(aplazados) != 0:
        print(f"Los aplazados son: {aplazados}")

informe_notas()


