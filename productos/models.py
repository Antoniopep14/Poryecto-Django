from django.db import models
from django.utils import timezone

# Create your models here.
#MODELOS
#Es cuando se hace una consulta(Query SQL) a una clase continuamente usando ORM
#ORM: Object relational mapping, esto lo que hace es tomar las clases construidas
    #y hace un mapeo contra la db sin necesidad de escribir consultas
#para crear clases que puedan ser mapeadas por el ORL de Django

class Categoria(models.Model):
    #con esto extendemos las funciones de nuestras db usando pythhon y no sql
    #a la variable de abajo tenemos que indicarle el tipo de dato que tendra
    #en las db un tipo es: CharField(max_length=255)*cadena de texto limitada
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    
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
    def __str__(self):
        return self.nombre
#y ya esta, ahora para que estos modelos se vean reflejadpos en la base de datos
#tenemos que usar las migraciones, que es el sig tema
    
#IMPORTANTE, ESTOS MODELOS DEBEN ESTAR EN LA CARPETA DE MODELS DE LA CATEGORIA QUE CREAMOS ANTERIORMENTE
    #ES DECIR LA DE PRODUCTOS
    #ahora agreamos una nueva dependencia y vamos a hacer qwue sea automatica
    #para lo que le agregamos el valor de default en base a la fecha
    #que tenemos que importar timezone para usarla
    creado_en = models.DateTimeField(default=timezone.now)
    #al crear esta dependencia debemos tener cuidado de no ejecutarla, solo pasar la referencia
    #sino todos los registros que se creen quedaran con la fecha del momento en que ejecutamos
