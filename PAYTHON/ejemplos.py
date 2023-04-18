import json
from pathlib import Path
from pprint import pprint

 

#ingreso de nuevos usuarios

def crear_usuarios(base_de_datos):

    formulario = {}

    formulario['usuario'] = input('Ingrese un nuevo usuario: ')

    formulario['contraseña'] = input('Ingrese su nueva contraseña: ')

    base_de_datos.append(formulario)

    try:

        with open(ruta_archivo, 'w') as archivo:

            json.dump(base_de_datos, archivo, indent=4)

    except Exception as error:

        print(f"Ocurrió el error: {error}")

    return base_de_datos

 

 
#pregnta una vez termine de registrarce, si desea crear otro usuario 

def preguntar_si_crear_usuarios(base_de_datos):

    while True:

        nuevos_datos = input("¿Desea ingresar un nuevo usuario?: s/n: ")

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

            if password == elemento_de_lista.get("contraseña"):

                print("Contraseña correcta")

                validacion = True

                break

            else:

                print("Contraseña incorrecta")

                break

        else:

            print("Usuario incorrecto")

            break

    return validacion

 

 

def cargar_datos():

    if ruta_archivo.exists():

        try:

            with open(ruta_archivo) as archivo:

                base_de_datos = json.load(archivo)

                return base_de_datos

        except json.decoder.JSONDecodeError:

            print("El archivo existe pero no es un formato JSON")

            return False

    else:

        print("No existe el archivo. Se creará uno nuevo")

    return False

 

 

def mostrar_información(base_de_datos):

    pprint(base_de_datos)

 

 

def main():

    base_de_datos = cargar_datos()

    if not base_de_datos:

        base_de_datos = []

        preguntar_si_crear_usuarios(base_de_datos)

    else:

        es_login = login(base_de_datos)

        if not es_login:

            print("No pude acceder al sistema. Intente nuevamente")

            return

        print("Bienvenido al sistema")

        preguntar_si_crear_usuarios(base_de_datos)

       

 

 

# Variables globales

BASE_DIR = Path(__file__).resolve().parent

ruta_archivo = BASE_DIR / 'archivo.json'

 

main()