from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template


def probando_template_render(request):
    """
    Importar: from django.shortcuts import render
    settings.py: "DIRS": [BASE_DIR / "templates"]
    """
    
    return render(request, "index.html",)


"""
nombre = "Louis"
    apellido = "Van Beethoven"
    datos = {"nombre": nombre, "apellido": apellido}
    fecha_hora = datetime.now()
    fecha_hora_f = fecha_hora.strftime(r"%d/%m/%Y a las %H:%M:%Shs.")
    datos["fecha_hora"] = fecha_hora_f
"""