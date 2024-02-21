from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
from .models import Producto
#este ultimo import es para interactuar con la base de datos

# # Create your views here.
# #todas las vistas reciben el mismo argumento de request
# def index(request):
#     #donde vamos a retornar una respuesta http
#     #y en el quickfix selecccionamos from django.http import HttpResponse
#     return HttpResponse('Hola mundo!')
#     #con esto la ruta ya fnuciona y al ingresar al /productos nos regresa ese str
#     #ejecutamos: python manage.py runserver
#     #y abrimos http://127.0.0.1:8000/productos


# #ahora queremos ver una lista json en lugar el hola mundo
# def index(request):
#     #ahora crearemos una variable que nos muestre los productos
#     productos = Producto.objects.all().values()#values seria lo ultimo para que productos nos devuelva los valores
#     # productos = Producto.objects.filter(puntaje__lte=3)
#     # #lte es less than equal <= pero tambien puede ser
#     # #gte >=, lt <, gt >
#     # productos = Producto.objects.get(id=1)#o podriamos usar pk=1 que seria la primary key
#     print(productos)
#     return JsonResponse(list(productos), safe=False)#solo devuelve datos que sean diccionarios
# #por eso agregamos list para cambiar su tipo por listado y safe=false para que pueda listarlo
# #no da esto en la terminal al ejecutar el serv
# # <QuerySet [<Producto: Surfboard>]>
# #[17/Jan/2024 21:42:56] "GET /productos/ HTTP/1.1" 200 10

# #al ejecutar esto nos mostrara la lista de productos pero solo se debe usar si necesitamos salir de un apuro
# #entregar una version rapida del lista, sino debemos usar una dependencia que nos de un html

#ahora vamos a trabajar con plantillas
def index(request):
    productos = Producto.objects.all()#quitamos los valores porque vamos a pasar la referencia de los productos completa a la plantilla

    return render(
        request, #argumendo de la funcion
        'index.html', #donde se encuentra la plantilla, no existe, despues lo crearemos
        context={'productos' : productos} #son los datos que le vamos a pasar a la plantilla en forma de dicc
    )

#una forma de manejar errorres es la siguiente
# def detalle(request, producto_id):
#     try:
#         producto = Producto.objects.get(id=producto_id)

#         return render(request, 
#                     'detalle.html', 
#                     context={'producto': producto})
#     except Producto.DoesNotExist:
#         raise Http404()
    
#pero django tambien tiene una funcion que nos ayuda a eso

def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    return render(request, 
                'detalle.html', 
                context={'producto': producto})

#ahora tenemos que crear nuestro archivo detalle.html en templates

#aqui estamos agregando la funcion para los formularios
def formulario(request):
#para mostrar un formulario dentro de una platilla html 
#primero debemos de crear un formulario en base a la clase que creamos en forms
  ##ahora vamos a validar si se esta ejecutando el metodo de post
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    #ahora ceraremos una instancia de form en caso de que el metodo no sea POST
    #que seria el mismo del principio sin modificar con el request.POST
    else:
        form = ProductoForm()
    #con quickfix importamos la clase
    #ahora retornaremos el llamado a la funcino de render
    return render(
        request,#el primer argumento es request
        'producto_form.html',#seguido de la platilla que vamos a renderizar
        #esa platilla debemos de crearla en la carpeta de templates
        #despues le pasamos el contexto que queremos que tenga la platilla en forma ed dicc       
        {'form': form}
    )