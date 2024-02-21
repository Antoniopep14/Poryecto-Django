#ahora veamos como agregar forumlarios a nuestra aplicacion
#para poder capturar datos ren un formulario para la app
#tendremos que hacerlo usando HTML, CSS y ademas validar las entradas
#lo cual llevaria mucho tiempo, pero django tiene una herramienta
#que nos va a ayudar a hacer todo esto
#ademas podremos crear los formularios en  base a los modelos y categorias
#la dependencia se llama ModelForm
from . import models
from django.forms import ModelForm

class ProductoForm(ModelForm):
#cuando creamos un formulario en base a modelform tenemos que crear otra clase dentro
    class Meta:
        model = models.Producto
        #ahora le tenemos que indicar los campos que queremos que use de modelform
        fields = ['nombre', 'stock', 'puntaje', 'categoria']
    
