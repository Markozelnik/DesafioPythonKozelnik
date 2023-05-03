import json
from pathlib import Path

#modelos de usuario 
#muy basicos
#tratar de hacerlo mejor para entrega 3 o final ( buscar ejemplos parecidos al profesor)
class UsuarioModel:
    id = 0
    lista = []

    def __init__(self, nombre, contraseña,plan, id=0):
        Usuario.id += 1
        self.id = Usuario.id
        self.nombre = nombre
        self.contraseña = contraseña
        self.plan = plan
        Usuario.lista.append(self)


class UsuarioController:
#crear usuario
    @staticmethod
    def listar():
        if Usuario.lista:
            print( f"\n{'ID':>5} {'NOMBRE':<10} {'CONTRASEÑA':<10} {'CONTRASEÑA':<10}")
            for usuario in Usuario.lista:
                print(
                    f"{usuario.id:>5} {usuario.nombre:<10} {usuario.contraseña:<10} {usuario.plan:<10}")
        else:
            print("No hay registros.")

    @staticmethod
    def crear(db): #crear usuario
        nombre = input("Nombre de usuario: ")
        for usuario in Usuario.lista:
            if nombre == usuario.nombre:
                print("El usuario ya existe, pruebe con otro nombre.")
                return
        contraseña = input("Contraseña: ")
        plan = input("Ingrese su plan (bornce, plata o oro):")
        Usuario(nombre, contraseña,plan)
        db.guardar_datos()
        print("Usuario creado.")

    @staticmethod
    def actualizar(db): #actualizacion del usuario
        nombre = input("Nombre de usuario a modificar: ")
        for usuario in Usuario.lista:
            if nombre == usuario.nombre:
                nuevo_nombre = input("Introduzca nuevo nombre: ")
                for usuario in Usuario.lista:
                    if nuevo_nombre == usuario.nombre:
                        print("El usuario ya existe, pruebe con otro nombre.")
                        return

                contraseña = input("Introzca nueva contraseña: ")
                plan = input("Introduzca su nuevo plan(bronce, plata o oro):")
                usuario.nombre = nuevo_nombre
                usuario.contraseña = contraseña
                usuario.plan = plan
                db.guardar_datos()
                print("Usuario modificado.")

    @staticmethod
    def eliminar(db):#eliminar usuario
        nombre = input("Nombre de usuario a eliminar: ")
        for usuario in Usuario.lista:
            if nombre == usuario.nombre:
                Usuario.lista.remove(usuario)
                print("Usuario eliminado.")
                db.guardar_datos()


class Usuario(UsuarioModel, UsuarioController):
    pass