#django tiene muchas herramientas http response para responder a un http request
#pero para ello se deben de cumplir ciertos pasos:
#primero terminar de instalar la aplicacion de productos
#configurar las URLs
#configurar las rutas hijas
#despues trabajar con las views que va a ejecutra lo qeu se van a hacer con las rutas

#para instalar la app de productoas vamos al arhivo apps de productos y copiamos la clase de ahi
# y copiarla en settings de DJANGO para crear la app de productos en instaled_apps
#despues vamos a configurar la ruta, a urls de DJANGO y en urlpatterns agregar:
#path('productos/', include('productos.urls')) donde productos es la app y lo que sigue es un archivo de urls con las rutas que podria contener
#pero para referenciarlo en las django.urls debemos poner: ,include que es una funcion que recibe un str de donde se encuentran las urls
#entonces le agregamos include + el parametro de nuestra app y el archivo donde estaran las urls
#ahora creamos el archivo urls en productos y continuamos ahi

#MODELOS
#Es cuando se hace una consulta(Query SQL) a una clase continuamente usando ORM
#ORM: Object relational mapping, esto lo que hace es tomar las clases construidas
    #y hace un mapeo contra la db sin necesidad de escribir consultas
#para crear clases que puedan ser mapeadas por el ORL de Django
from django.db import models

class Categoria(models.Model):
    #con esto extendemos las funciones de nuestras db usando pythhon y no sql
    #a la variable de abajo tenemos que indicarle el tipo de dato que tendra
    #en las db un tipo es: CharField(max_length=255)*cadena de texto limitada
    nombre = models.CharField(max_length=255)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    #integerfield nos ayuda a llevar un conteo de productos en stock
    stock = models.IntegerField()
    #  nos ayudar a llevar un puntaje asignado al producto por los usuairos
    puntaje = models.FloatField()
#para ver todos los tipos de campos que podemos usar escribioms models.field y aparece todos como sugerencia
#como notas no usar autofield porque es mejor designar el tipo de dato
#ni tampodo textfield porque un hacker podria insertar una gran cantidad de datos a tu db y tirarla   
#ahora lo que queremos es establecer una relacion entre los productos y las categorias
#on delete se usa apra que la clase de Producto sepa que hacer en caso de eliminar nua categoria de la otra clase
#aqui podemos usar: cascade: elimina el producto si se elimina la categoria
    #protect: lanza un error, restrict: no te deja eliminar la categoria a menos que elimines todos los productos de esa categoria
    #set_null: actualiza a valor nulo si se elimina la categoria
    #set_default: asigna el valor por defecto asignado como un argumento nombrado (Categoria, default=x)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE
        )

#y ya esta, ahora para que estos modelos se vean reflejadpos en la base de datos
#tenemos que usar las migraciones, que es el sig tema
    
#IMPORTANTE, ESTOS MODELOS DEBEN ESTAR EN LA CARPETA DE MODELS DE LA CATEGORIA QUE CREAMOS ANTERIORMENTE
    #ES DECIR LA DE PRODUCTOS



