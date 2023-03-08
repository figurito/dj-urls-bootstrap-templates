from django.shortcuts import render
from django.http import HttpResponse
import datetime


def calculo(request, fechaNacimiento, fechaFutura):
    agno_actual=datetime.datetime.now().year
    edad_actual=agno_actual-fechaNacimiento
    edad_futura=fechaFutura-fechaNacimiento
    documento=""" <html>
                    <head>
                      <title>Pasar Parametros en Django</title>
                    </head>
                    <body>
                        <h1>El Aprendiz Nacio en el Año %s actualmente tiene la edad de %s años y en el año
                        %s tendra %s años de edad</h1>
                    </body>    
    
                  </html>""" % (fechaNacimiento,edad_actual,fechaFutura, edad_futura )
    return HttpResponse(documento)

def inicio(request):
    agno_actual=datetime.datetime.now().year
    tareas=['Aprender Django', 'Aprender Python','Aprender HTML', 'Aprender GIT']
    context={'listado':tareas,'ahoy':agno_actual}
    return render(request, 'inicio.html', context)

def list_productos(request):
    prod=['Impresora HP', 'Mouse HP','Portatil lenovo Intel core11G   ', 'Cable HDMI 3Mtrs']
    context={'listado':prod}
    return render(request, 'productos.html', context)

