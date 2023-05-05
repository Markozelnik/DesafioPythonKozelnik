from PAYTHON.Usuario.modelo_usuario import Usuario
#login en Eslovenos Fc

def login(database):#usuario
    def login_nombre(nombre):
        for usuario in Usuario.lista:
            if nombre == usuario.nombre:
                return usuario.nombre
        return False

    def login_contraseña(contraseña): #contraseña
        for usuario in Usuario.lista:
            if contraseña == usuario.contraseña:
                return True
        return False
    
    def login_plan(plan): #plan a eleccion-> acordarse de ver como poder poner los planes para seleccionar
        for usuario in Usuario.lista:
            if plan == usuario.plan:
                return True
        return False

    print("Ingreso")
    try:                           
        nombre = input("Usuario: ")
    except KeyboardInterrupt:
        print("\nSalió de la pagina")
        quit()
    if not login_nombre(nombre):
        print("Usuario no existe.")
        return False
    contraseña = input("Contraseña: ")
    if not login_contraseña(contraseña):
        print("Contraseña incorrecta.")
        return False
    return nombre

