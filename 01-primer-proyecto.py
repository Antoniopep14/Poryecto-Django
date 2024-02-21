#intalamos djando con pipenv install django==4.1.7
#ahora usaremos una herramienta administrativa que viene instalada con django:
    #django-admin startproject DJANGO .
#el punto al final es para que cree la carpeta en donde estamos trabajando
#tambien crea el archivo manage.py que nos va a funcionar para administrar nuestros proyectos escritos con django
#ahora ejecutamos: python manage.py runserver
#que nos va a decir lo de que tenemos que migrar 18 apps
#la fecha, version de django y server at http://127.0.0.1:8000/
#que es la ruta de donde se va a montar nuestra aplicacion 

#para crear una aplicacion con django tenemos que entender que es un proyecto
#y que ese proyecto esta compueesto de varias app por ejemplo, crearemos una blog
#para lo cual vamos a necesitar varias app:
#app1 = app de administracion desde donde escribiremos los blogs
#app2 = encargada del frontend
# app3 = checkout suponiendo que nosotros vendemos algo dentro de nuestro blog
#la evntaja de esto es que estas aplicaciones son pequeñas y reutilizables
 
#para  crear una app: python manage.py startapp productos
#nos crea la carpeta de productos y nos ayudara a mantener todos los cambios que se le realizaran a nua db
#en admin.py podremos registrar nuestros modelos en el administrador de django
#apps.py para registrar nuestra aplicacion
#models.py nos permite definir clases las cuales van a hacer referencia en la db
#   para trabajar directamente con python y no con sql u otros administradores de db
#test.py para escribir nuestros test automatizados
# views.py