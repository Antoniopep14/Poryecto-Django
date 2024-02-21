#lo que vamos a hacer es comparar nuestra app con la db para que si no estan nuestros modelos en ella
#generar un script que los inserte
#es el paso a paso para actualizar nuestra base de datos
#ahora si vamos  a solucionar lo de las migraciones
#escribimos en terminal: python manage.py makemigrations
#RECORDAR que debemos tener las clases en models de la carpeta que queremos incluir
#y debemos de tener el agregada la carpeta en settings de la carpeta del proyecto
#al ejecutar nos crea: Migrations for 'productos':
  #productos\migrations\0001_initial.py
    #- Create model Categoria
    #- Create model Producto

#eso nos ha creado el archivo encargado de actualizar la db
#NUNCA borrar estos archivos (0001_initial.py) ya que estos indican el paso a paso
#en la historia, de todos los cambios realizados en la db
#ahora ejecutamos: python manage.py migrate
#lo que hace el ejecutar los cambois de 0001_initial
#ahora vamos a intruciar la db que acabamos de crear
#si abrimos db.sqlite3 veremos las tablas creadas en base a las clases que mandamos
#la tabla de django migrations contiene el registro de todos lo cambios efectuados en la db

#para acutalizar los models vamos a agregar una nueva dependencia a la clase de producto
#va a ser llamada creado_en y alla continuamos
#de esta manera pudimos ver que: python manage.py makemigrations
#hace la comparacion y actualiza de ser necesario
#Migrations for 'productos':
  #productos\migrations\0002_producto_creado_en.py
   # - Add field creado_en to producto
#y por ultimo migramos: python manage.py migrate
#ahora ya tenemos el migrations, la 0001 y la 0002 recordar no borrarlas por nada
#ya que cada una contiene los cambios a realizar independiente de la otra

#GESTION DE MODELOS
#ahora veamos como gestionar los modelos con las herramientas de django
#primero ejecutamos nuestro servidor de desarrollo: python manage.py runserver
#e ingresamos a la ruta 127.0.0.1:8000/admin
#y vemos que pide usuario y pass
#asi que crearemos usuarios que sean admins: python manage.py createsuperuser
#admin, antonio.142103@gmail.com, pp142103
#ahora para poder ver los modelos creados en la interfaz de admin
#tenemos que agregarlos al archivo de admin importandolos
#continuamos alla
#despues de eso, lo que icimos fue correr la pagina de nuevo, entrar como admin
#y agregamos una categoria alla, llamada deportes, pero no la muestra como astrid
#asi que vamos a personalizar nuestro administrador definiendo el str en categoria y producto
#para lo cual añadimos
#def __str__(self):
        # return self.nombre
#pero tambien podemos agregar mas cosas como la camtidad de columnas que queremos que nos muestre:
#para ello vamos a agregar una nueva clase a admin que indique lo que queremos ver
#pasandola como segundo argumento a al metodo de registeer en el archivo admin
#continuamos alla

#despues de crear la interaccion con la base de datos vamos a
#corregir los errores que marca vscode en el codigo, para ello ejecutamos
# pipenv install pylint-django
# para que la dependencia se encargue de que django interactue bien con vscode
# y creamos el archivo .pylintrc en la carpeta DJANGO
