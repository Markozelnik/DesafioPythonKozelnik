import json
from pathlib import Path
from PAYTHON.Usuario.modelo_usuario import Usuario


#json
#base de datos del "programa"

class ManejoArchivos:
    nombre_archivo = "mi_clase_14.json"
    BASE_DIR = Path(__file__).resolve().parent
    ruta_archivo = BASE_DIR / nombre_archivo

    def __init__(self):
        pass

    def leer_archivo(self):
        if ManejoArchivos.ruta_archivo.exists():
            try:
                archivo = open(ManejoArchivos.ruta_archivo)
                datos = json.load(archivo)
                return datos
            except json.JSONDecodeError:
                print("El archivo existe pero tiene errores. No se cargarán datos.")
        else:
            print("El archivo de la base de datos no existe.")
            print("Se crea el archivo", ManejoArchivos.ruta_archivo)

    def guardar_archivo(self, datos):
        with open(ManejoArchivos.ruta_archivo, "w") as file:
            json.dump(datos, file, indent=4)
            print("Base de datos guardada.")


class BaseDatos(ManejoArchivos):
    def __init__(self):
        pass

    def cargar_datos(self):
        datos = self.leer_archivo()
        if datos:
            # Usuarios
            if datos.get("usuarios"):
                for usuario in datos.get("usuarios"):
                    Usuario(**usuario)
            return datos  

    def guardar_datos(self):
        datos = {}
        # Usuarios
        if Usuario.lista:
            datos["usuarios"] = []
            for usuario in Usuario.lista:
                datos["usuarios"].append(usuario.__dict__)

        self.guardar_archivo(datos)
