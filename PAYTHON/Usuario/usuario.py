class Menu:
    def __init__(self) -> None:
        pass

    def principal(self, db, user):  # se agrega parámetro
        while True:
            print(f"\n{user}")
            print('MENU PRINCIPAL')
            print('1. Usuario')
            print('2. Logout')    # **********
            opción = input('Elige una opción: ')
            if opción == '1':
                self.usuario(db, user)
            elif opción == '2':
                user = None
                return user
            else:
                print('\nOpción inválida')

    def usuario(self, db, user):  # se agrega parámetro
        while True:
            print(f"\n{user}")
            print('MENU USUARIO')
            print('1. Crear')
            print('2. Ver')
            print('3. Actualizar')
            print('4. Eliminar')
            print('x. Volver al menú principal')
            opción = input('Elige una opción: ')
            if opción == '1':
                Usuario.crear(db)
            elif opción == '2':
                Usuario.listar()
            elif opción == '3':
                Usuario.actualizar(db)
            elif opción == '4':
                Usuario.eliminar(db)
            elif opción == 'x':
                break
            else:
                print('\nOpción inválida')


def main():
    db = BaseDatos()
    hay_usuarios = db.cargar_datos()
    if hay_usuarios:
        while True:
            user = login(db)
            if user:
                menu = Menu()
                logout = menu.principal(db, user)
                if logout:
                    db = {}
                    continue
    else:
        print("Debe crear un usuario para usar la aplicación")
        Usuario.crear(db)


main()