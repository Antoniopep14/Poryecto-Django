#ahora sigamos la convencion que python espera que tengamos
#recordar que la usar la funcion de urlpatterns nosotros la estamoss creando a traves de la convencion de include
#y ella espera un listado de urls que queremos seguir y mapear con nuestras funciones
from django.urls import path
from . import views

##cuando trabajamos con rutas es bueno que nosotros usemos el nombre de la app
##al comienzo porque asi nos aseguramos que las platillas no se repitan en las apps
## para no tener que agregar producto_detalle, producto_index, etc
##usamos la siguiente variable la cual es una convencion que sigue django
##en caso de existir una variable app name la va a concadenar
#con el nombre de la ruta
app_name = 'productos'

urlpatterns = [
    #path('lala') #esto va a crear una ruta /productos/lala
    #pero como yo quiero que lo ejecute dentro de la funcion de productos lo haremos ed la siguiente manera
    #donde le indicaremos cual es la funcion dentro el archivo de views que queremos ejecutar
    #pero a la vez debemos de crearla
    #from . import views
    #usamos el punto pues si solo lo hacemos con import views
    #podria haber un modulo general que interfiera con nuestro modulo
    #el . indica que es desde la carpeta donde yo me encuentro
    #entonces ya le pasamos views. mas el nombre de la funcion que voy a crear(index)
    #ademas es buena practica pasarle un tercer argmento indicando el nombre de esta funcion con esta ruta
    path('', views.index, name='index'),
    ##aqui agregamos la ruta para los formularios
    path('formulario', views.formulario, name='formulario'),
    # ahora crearemos otra ruta que este enlazada a nuestro producto
    path('<int:producto_id>', 
         views.detalle, 
         name='detalle'
        #  cuando hacemos una referencia a una url cuando estamos en nuestro codigo
        #  nosotros tenemos 2 alternativas, usar una etiqueta <a> </a> dentro de una
        #  propiedad llamada href, pero al cambiar una ruta
        #  nosotros tendriamos que ir a todos lo archivos a cambiar esa ruta
        #  por eso la mejor manera es que utilicemos el nombre de la ruta en lugar
        #  de la ruta misma, por ultimo hacemos la referencia en el archivo de views
         ),
    #ahora seguimos en views para crear la funcion
]
