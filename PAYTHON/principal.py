import json
from pathlib import Path
from PAYTHON.Usuario.modelo_usuario import Usuario
from PAYTHON.Usuario.login import login
from PAYTHON.Datos.base_de_datos import ManejoArchivos, BaseDatos

#principal del programa segunda entrega
#deberia poner la informacion de cada abono sea Bronce, Plata o Oro en el html principal en el futuro 
class MenuPrincipal:
    def __init__(self) -> None:
        pass

    def principal(self, db, user):  
        while True:
            print(f"\n{user}")
            print('Eslovenos Fc')
            print('1. Usuario')
            print('2. Logout')    
            opción = input('Elige una opción: ')
            if opción == '1':
                self.usuario(db, user)
            elif opción == '2':
                user = None
                return user
            else:
                print('\nOpción inválida')

    def usuario(self, db, user):  # para poder eliminar, crear o actualizar el abono mensual de Eslovenos fc
        while True:
            print(f"\n{user}")
            print('MENU USUARIO ESLOVENOS FC')
            print('1. Crear nuevo usuario')
            print('2. Ver mi abono')
            print('3. Actualizar usuario')
            print('4. Eliminar usuario')
            print('5. Volver al menú principal')
            opción = input('Elige una opción: ')
            if opción == '1':
                Usuario.crear(db)
            elif opción == '2':
                Usuario.listar()
            elif opción == '3':
                Usuario.actualizar(db)
            elif opción == '4':
                Usuario.eliminar(db)
            elif opción == '5':
                break
            else:
                print('\nOpción inválida')

#base de datos de Eslovenos Fc
def main():
    db = BaseDatos()
    hay_usuarios = db.cargar_datos()
    if hay_usuarios:
        while True:
            user = login(db)
            if user:
                menu = MenuPrincipal()
                logout = menu.principal(db, user)
                if logout:
                    db = {}
                    continue
    else:
        print("Bienvenido a Eslovenos Fc") #bienvenida al programa 
        print("Esta listo para unirse a la familia Eslovena?")
        print("Los distintos abonos disponibles son: bronce, oro y plata") 
        Usuario.crear(db)


main()