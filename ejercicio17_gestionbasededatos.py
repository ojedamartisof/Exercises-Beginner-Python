"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su ID,
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
donde preferente tendrá el valor True si se trata de un cliente preferente.
El programa debe preguntar al usuario por una opción del siguiente menú:
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
(5) Listar clientes preferentes, (6) Terminar.

En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el ID del cliente y eliminar sus datos de la base de datos.
Preguntar por el ID del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su ID y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su ID y nombre.
Terminar el programa.

"""

clientes = {}
option = ''
while option != '6':
    if option == '1':
        id = input('Introduce ID del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        tel = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ').upper()
        cliente = {'nombre': nombre, 'dirección': direccion, 'teléfono': tel, 'email': email, 'preferente': vip == 'S'}
        clientes[id] = cliente
    if option == '2':
        id = input('Introduce id del cliente: ')
        if id in clientes:
            del clientes[id]
        else:
            print('No existe el cliente con el id', id)
    if option == '3':
        id = input('Introduce id del cliente: ')
        if id in clientes:
            print('ID:', id)
            for key, value in clientes[id].items():
                print(key.title() + ':', value)
        else:
            print('No existe el cliente con el id', id)
    if option == '4':
        print('Lista de clientes')
        for key, value in clientes.items():
            print(key, value['nombre'])
    if option == '5':
        print('Lista de clientes preferentes')
        for key, value in clientes.items():
            if value['preferente']:
                print(key, value['nombre'])
    option = input('''Menú de opciones\n
    1 Añadir cliente\n
    2 Eliminar cliente\n
    3 Mostrar cliente\n
    4 Listar clientes\n
    5 Listar clientes preferentes\n
    6 Terminar\n
    Elige una opción:''')  # vas a responder con un numero


