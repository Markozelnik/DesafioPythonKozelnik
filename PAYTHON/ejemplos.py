import json
from pathlib import Path
from pprint import pprint

#esta fue mi primer entrega, y la dejo aca para ir cobiando lo que hice pero nada mas















#la idea en un futuro seria registrarse y tener un nivel de abono con distintos beneficios dependiendo tu abono
# en un futuro hacer algun apartado en html con los distinos abonos para que el usuario pueda ver
#
print("Buenos dias, bienvenido a Eslovenos Fc")
print("Los distintos abonos disponibles son: bronce, oro y plata") 
print("")
#ver para poner mas informacion para que los usuarios sepan mas de los niveles 
#ingreso de nuevos usuarios

def crear_usuarios(base_de_datos):
    inscripcion = {}
    inscripcion['usuario'] = input('Ingrese un nuevo usuario: ')
    inscripcion['contraseña'] = input('Ingrese su nueva contraseña: ')
    inscripcion['abono'] = input('Ingrese nuevo nivel de abono: ')#revisar para que sea mejor en un futuro
    base_de_datos.append(inscripcion)
    try:
        with open(ruta_archivo, 'w') as archivo:
            json.dump(base_de_datos, archivo, indent=4)
    except Exception as error:
        print(f"Ocurrió el error: {error}")
    return base_de_datos

 
#pregnta una vez termine de registrarce, si desea crear otro usuario 
def preguntar_crear_usuarios(base_de_datos):
    while True:
        nuevos_datos = input("¿Desea ingresar un nuevo usuario?: si/no: ")
        if nuevos_datos.lower().strip()[0] == 's':
            crear_usuarios(base_de_datos)
            continue
        else:
            break
    return base_de_datos


#cuando vuelve a empezar el proceso, verifica el usuario y una vez encontrado pregunta si desea ingresar otro 
def login(base_de_datos):
    validacion = False
    print('INGRESO AL SISTEMA')
    usuario = input('Ingrese nombre de usuario: ')
    for elemento_de_lista in base_de_datos:
        if usuario == elemento_de_lista.get("usuario"):           
            print("Usuario encontrado")
            password = input('Ingrese contraseña: ')
            abono = input("Ingrese su abono: ")
            if password == elemento_de_lista.get("contraseña"):
                #en futuro mejorar para que quede todo en orden y no al final
                print("Contraseña correcta")
                validacion = True
                if abono == elemento_de_lista.get("abono"):
                    print("El abono coincide")
                    #revisar para poder preguntar si desea cambiar su abono y que cambie en json
                break
            else:
                print("Contraseña incorrecta")
                break
        else:
            print("Usuario incorrecto")
            break
    return validacion

 
#posibles erroes
def cargar_datos():
    if ruta_archivo.exists():
        try:
            with open(ruta_archivo) as archivo:
                base_de_datos = json.load(archivo)
                return base_de_datos
        except json.decoder.JSONDecodeError:
            print("El archivo existe pero no es valido")
            return False
    else:
        print("No existe el archivo. Se creará uno nuevo")
    return False

 
#mostrare la info
def mostrar_información(base_de_datos):
    pprint(base_de_datos)
  
def main():
    base_de_datos = cargar_datos()
    if not base_de_datos:
        base_de_datos = []
        preguntar_crear_usuarios(base_de_datos)
    else:
        es_login = login(base_de_datos)
        if not es_login:
            print("No pude acceder al sistema. Intente nuevamente")
            return
        print("Bienvenido al sistema")
        preguntar_crear_usuarios(base_de_datos)

# Variables generales
BASE_DIR = Path(__file__).resolve().parent
ruta_archivo = BASE_DIR / 'archivo.json'
#revisar error de contraseña en json (aparece mal el nombre contraseña en json)
main()