from django.shortcuts import render
#esto es para poder devolver codigo html al usuario

#ahora definimos la funcion de inicio
#a la cual tenemos que pasarle la plantilla que contenga la pagina de inicio
#lo correcto seria crear otra app llamada inicio y crear el archivo inicio
#en una carpeta templates de ahi, pero para el alcance de este ejemplo
#la pondremos dentro de templates principal
def inicio(request):
    return render(
        request,
        'inicio.html'
    )

