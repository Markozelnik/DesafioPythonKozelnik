def login(db):
    def login_nombre(nombre):
        for usuario in Usuario.lista:
            if nombre == usuario.nombre:
                return usuario.nombre
        return False

    def login_contraseña(contraseña):
        for usuario in Usuario.lista:
            if contraseña == usuario.contraseña:
                return True
        return False

    print("LOGIN")
    try:                            # se agrega bloque
        nombre = input("Usuario: ")
    except KeyboardInterrupt:
        print("\nSalió del programa")
        quit()
    if not login_nombre(nombre):
        print("Usuario no existe.")
        return False
    contraseña = input("Contraseña: ")
    if not login_contraseña(contraseña):
        print("Contraseña incorrecta.")
        return False
    return nombre

