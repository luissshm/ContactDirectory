from os import system
import sqlite3
from sqlite3.dbapi2 import Cursor
import time


def conexion():
    conectar = sqlite3.connect('directorio.db')
    cursor = conectar.cursor()
    return conectar, cursor


def insertar():
    conectar, cursor = conexion()
    nombre, apellido, numero, correo, relacion = str(input('Inserte los datos de su contacto (Nombre Apellido Numero Correo Relacion): ')).split()
    datos = nombre, apellido, numero, correo, relacion
    sql = '''
    INSERT INTO contactos(Nombre, Apellido, Numero, Correo, Relacion) VALUES (?, ?, ?, ?, ?)
    '''
    print('Datos guardados' if cursor.execute(sql, datos) else 'No se pudieron guardar los datos')
    conectar.commit() and conectar.close()


def consultar():
    conectar, cursor = conexion()
    cursor.execute('SELECT id,Nombre,Apellido,Numero,Correo,Relacion from contactos')
    for fila in cursor:
        print(f'''ID = {fila[0]}
        Nombre = {fila[1]}
        Apellido = {fila[2]}
        Numero = {fila[3]}
        Correo = {fila[4]}
        Relacion = {fila[5]}

        ''')
    conectar.close()


def modificar():
    conectar, cursor = conexion()
    id = int(input('Ingresa el ID: '))
    if(id != 0):
        nombre, apellido, numero, correo, relacion = str(input('Ingrese (Nombre Apellido Numero Correo Relacion): ')).split() 
        sql = "UPDATE contactos SET Nombre=?,Apellido=?,Numero=?,Correo=?,Relacion=? WHERE id=?"
        parametros = (nombre,apellido, numero, correo, relacion, id)
        cursor.execute(sql, parametros)
        conectar.commit()
        conectar.close()
        print('Actualizados')


def borrar():
    conectar, cursor = conexion()
    id = int(input('Ingresa el id: '))
    if(id != 0):
        sql = "DELETE FROM contactos WHERE id=?"
        parametros = (id,)
        cursor.execute(sql,parametros)
        conectar.commit()
        conectar.close()
        print("Eliminado!")
    else:
        print("Se require un id")


def buscar():
    conectar, cursor = conexion()
    nombre = str(input('Buscar por nombre: '))
    if(len(nombre) > 0):
        sql = "SELECT * FROM contactos WHERE Nombre LIKE ?"
        parametros = (f'%{nombre}%',)
        result = cursor.execute(sql,parametros)
        for data in result:
            print(f""" 
            +id :    {data[0]}
            +Nombre :    {data[1]}
            +Correo :    {data[4]}
            +Relacion :  {data[5]}""")
        conectar.commit()
        conectar.close()

while True:
    print("================================================")
    print(f"\tBienvenido a su directorio de contactos")
    print("================================================")
    print("\t[1] Insertar registro")
    print("\t[2] Listar registros")
    print("\t[3] Actualizar registros")
    print("\t[4] Eliminar registros")
    print("\t[5] Buscar registros")
    print("\t[6] Salir")
    print("=========================================")

    try:
        opcion = int(input("Selecciona una opcion: "))
        if(opcion == 1):
            insertar()
            time.sleep(1)
            system("cls")
        elif (opcion == 2):
            consultar()
            time.sleep(1)
        elif (opcion == 3):
            modificar()
            time.sleep(1)
            system("cls")
        elif (opcion == 4):
            borrar()
            time.sleep(1)
            system("cls")
        elif (opcion == 5):
            buscar()
            
        elif (opcion == 6):
            break
    except:
        print("Por favor, selecciona las opciones correctas")
        time.sleep(3)
        system("cls")
