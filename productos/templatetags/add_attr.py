from django import template
#creamos un decorador para poder registrar el filtro
register = template.Library()

@register.filter(name="add_attr")
#definimos la funcion add_attr
#la cual recibe 2 atributos field y la clase que de¿¿necesitamos pasarle
#en este claso class is_invalid
def add_attr(field, css):
    attrs = {}
    #el parametro de css necesita una clase, la cual sera class:is_invalid
    #por lo que vamos a tomar el str y dividirlo con los : split
    clase, valor = css.split(':')
    attrs[clase] = valor

    return field.as_widget(attrs=attrs)