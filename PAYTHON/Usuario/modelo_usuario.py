import json
from pathlib import Path


class UsuarioModel:
    id = 0
    lista = []

    def __init__(self, nombre, contraseña, id=0):
        Usuario.id += 1
        self.id = Usuario.id
        self.nombre = nombre
        self.contraseña = contraseña
        Usuario.lista.append(self)


class UsuarioController:

    @staticmethod
    def listar():
        if Usuario.lista:
            print( f"\n{'ID':>5} {'NOMBRE':<10} {'CONTRASEÑA':<10}")
            for usuario in Usuario.lista:
                print(
                    f"{usuario.id:>5} {usuario.nombre:<10} {usuario.contraseña:<10}")
        else:
            print("No hay registros.")

    @staticmethod
    def crear(db):
        nombre = input("Nombre de usuario: ")
        for usuario in Usuario.lista:
            if nombre == usuario.nombre:
                print("El usuario ya existe, pruebe con otro nombre.")
                return
        contraseña = input("Contraseña: ")
        Usuario(nombre, contraseña)
        db.guardar_datos()
        print("Usuario creado.")

    @staticmethod
    def actualizar(db):
        nombre = input("Nombre de usuario a modificar: ")
        for usuario in Usuario.lista:
            if nombre == usuario.nombre:
                nuevo_nombre = input("Introduzca nuevo nombre: ")
                for usuario in Usuario.lista:
                    if nuevo_nombre == usuario.nombre:
                        print("El usuario ya existe, pruebe con otro nombre.")
                        return

                contraseña = input("Introzca nueva contraseña: ")
                usuario.nombre = nuevo_nombre
                usuario.contraseña = contraseña
                db.guardar_datos()
                print("Usuario modificado.")

    @staticmethod
    def eliminar(db):
        nombre = input("Nombre de usuario a eliminar: ")
        for usuario in Usuario.lista:
            if nombre == usuario.nombre:
                Usuario.lista.remove(usuario)
                print("Usuario eliminado.")
                db.guardar_datos()


class Usuario(UsuarioModel, UsuarioController):
    pass