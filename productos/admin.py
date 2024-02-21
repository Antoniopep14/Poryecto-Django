from django.contrib import admin
#aqui importamos los modelos que queremos registrar
from .models import Categoria, Producto

#creando clase para personalizar el administrador

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

#ahora crearemos una para productos
class ProductoAdmin(admin.ModelAdmin):
    #como al crear un producto desde la web nos muestra opciones para personaliazr la fecha
    #y no queremos que eso se muestre, vamos aocultarlo
    #para ello podemos usar fields = *y seleccionar los campos visibles
    #u ocultar los que no queremos que se vean
    exclude = ('creado_en', )
    #RECORDAR que debemos pasarle una tupla por lo que le agregamos , para que no lo reconosca como str
    
    list_display = ('id', 'nombre', 'stock', 'creado_en')
# Register your models here.
#y para registrar los modelos
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)