appBiblioteca
Requisitos
-	Python 3.8 o superior
-	Django 4.0 o superior
-	Django REST Framework

 Configuración del proyecto
Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:
Clona el repositorio
git clone https://github.com/JoseBF22/PruebaDevJr.git
cd appBiblioteca

 Crear un entorno virtual
python -m venv venv

 Activar el entorno virtual
# En Windows
.\venv\Scripts\activate
# En MacOS/Linux
source venv/bin/activate

Instala las dependencias
pip install -r requirements.txt

Ejecuta las migrate
python manage.py migrate

Ejecuta el servidor
python manage.py runserver
Prueba Tecnica 
Las rutas para probar los ejercicios en postman son: 
**Escribe una función en Python que reciba una lista de números y devuelva una nueva lista con los números ordenados de menor a mayor.**
Método HTTP: POST
URL: http://127.0.0.1:8000/api/ordenar/
Cuerpo de la solicitud (Body): Selecciona el formato JSON en el cuerpo de la solicitud y envía una lista de números. se anexa el ejemplo: 

{
  "numeros": [5, 3, 8, 1, 9]
}

**Respuesta**
{
  "numeros_ordenados": [1, 3, 5, 8, 9]
}

**Escribe un script en Python que lea un archivo de texto y cuente la cantidad de palabras que contiene.**
Método HTTP: POST
URL: http://127.0.0.1:8000/api/contar-palabras/
Cuerpo de la solicitud (Body):
  Key: archivo
  Tipo: File
  Valor: selecciona un archivo tipo .txt de tu sistema 



**Respuesta**
{
  "cantidad_palabras": 16
}

**Diseña una API simple en Django que permita realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un recurso llamado "Tareas". Proporciona los endpoints necesarios.**
URL: http://127.0.0.1:8000/api/tareas/
Métodos: GET (listar todas), POST (crear nueva)
EJEMPLO DE POST (json):

{
  "titulo": "Leer un libro",
  "descripcion": "Leer el libro de Django",
  "completada": false
}

Leer, actualizar o eliminar una tarea específica:
URL: http://127.0.0.1:8000/api/tareas/<id>/
Métodos: GET (obtener una tarea), PUT (actualizar una tarea), DELETE (eliminar una tarea)

**Nota: El ejericio de los modelos esta en el archivo models.py de tareas. 
La consulta Mysql esta en el:  “archivo 3_MySQLConsulta_Insert”


Parte 1: Preguntas Teóricas

1. Django
<!-- ¿Qué es Django y por qué se usa?  -->
Django es un framework web de alto nivel, lo que significa que te proporciona una estructura sólida y herramientas preconstruidas para desarrollar aplicaciones web de manera rápida y eficiente. Está escrito en Python, un lenguaje de programación conocido por su legibilidad y versatilidad.
Se usa debido a diferentes características como por ejemplo la velocidad de desarrollo para construir aplicaciones web complejas en menos tiempo,  otra de sus características es de seguridad, escalabilidad y su versatilidad, resumidamente tiene muchas ventajas como las ya mencionadas anteriormente además de contar con buena documentación y una gran comunidad de desarrolladores

<!-- Explica brevemente el patrón MVC (Modelo-Vista-Controlador) y cómo se implementa en Django. -->
Se refiere a un patrón arquitectónico de software que se utiliza para separar responsabilidad redes de aplicación. En el modelo se representan los datos de aplicación y la lógica, en la vista se encuentra la parte de la aplicación que el usuario ve y que se encarga de presentar datos del modelo en forma visual como una página web y finalmente en el controlador recibe las solicitudes de usuario, actualiza el modelo y selecciona la vista adecuada para mostrar la información actualizada. 

<!-- ¿Qué es un modelo en Django y cómo se define? -->
Un modelo es de representación de datos que tiene aplicación para almacenarlos y gestionarlos estos se guardarán en la base de datos. 
Para definirlo se ocupa la clase model del módulo models y dentro de esta clase se especifican los campos que tendrá cada instancia del modelo cada objeto va a representar un registro en la base de datos. 

from django.db import models
# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo


2. Python
<!-- ¿Qué es un diccionario en Python y cómo se diferencia de una lista? -->
Un diccionario en python es una colección desordenada de elementos, donde cada elemento está asociado a una clave única, estos se definen entre llaves y cada elemento se escribe como clave:valor. 
Los diccionarios tienen como características que son mutables, desordenados, tienen claves únicas, y los valores pueden ser de cualquier tipo incluso de otros diccionarios o listas. 
Una lista en python es una colección ordenada de elementos, donde su sintaxis se define utilizando corchetes, tiene como características que es mutable es decir puede modificar elementos agregar nuevos o eliminarlos, es ordenada, tiene elementos duplicados y pueden ser de cualquier tipo de dato. 
Como diferencia clave podemos decir que un diccionario es para almacenar pares de claves y valores y una lista almacena colecciones de elementos ordenados. O dicho de otra forma los diccionarios almacenan datos asociados, mientras que las listas secuencias de elementos

<!-- Explica la diferencia entre append() y extend() en una lista de Python. -->
El append() Agrega solo un elemento al final de la lista, este elemento puede ser de cualquier tipo y modifica la lista original
Extend() agrega todos los elementos de un iterable al final de la lista modificando la lista original (lista, tupla, cadena, etc.)

<!-- ¿Qué es un decorador en Python? Proporciona un ejemplo simple. -->
Se refiere a una función que modifica el comportamiento de otra función. 
Ejemplo: supongamos que queremos crear un decorador que imprima un mensaje antes y después de que se ejecute una función: 
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args, **kwargs)
        print("Después de ejecutar la función")
        return resultado
    return wrapper

@mi_decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")

SALIDA; 
Antes de ejecutar la función 
Hola, Juan!
Después de ejecutar la función

Resumidamente un decorador es una herramienta poderosa que va a permitir modificar el comportamiento de funciones de una forma concisa y elegante. 

3. MySQL

<!-- ¿Qué es una base de datos relacional? -->
Son bases de datos que nos sirven para almacenar y gestionar grandes cantidades de datos de manera estructurada y eficiente. 
Explica la diferencia entre una clave primaria y una clave foránea.
La clave primaria se identifica de forma única dentro de una tabla y la clave foránea crea una relación entre 2 tablas vinculando un registro de una tabla con el registro de otra tabla. 

<!-- ¿Cómo se realiza una consulta SELECT básica en MySQL? -->
Es una herramienta fundamental para recuperar datos de una base de datos ya que permite seleccionar y mostrar los datos requeridos que se necesitan de una o de más tablas. 
SELECT * FROM nombre_de_la_tabla;

4. API

<!-- ¿Qué es una API y para qué se utiliza? -->
Se refiere a un conjunto de reglas y especificaciones que permiten que diferentes programas de software se comuniquen entre sí, se utilizan principalmente para integración de aplicaciones, desarrollo de aplicaciones móviles, servicios web, automatización de tareas, creación de MarketPlaces

<!-- Explica brevemente la diferencia entre una API REST y una API SOAP. -->
Que el API REST se basa en un estilo arquitectónico de los principios HTTP, es más ligero y flexible, utiliza formatos de datos tipo JSON el más común, usa HTTP (GET, POST, PUT, DELETE) para realizar operaciones CRUD (Create, Read, Update, Delete) en los recursos.
API SOAP, se refiere a un protocolo más formal y estructurado que utiliza XML para definir y transportar mensajes, usándolo exclusivamente para intercambio de datos, además requiere un archivo WSDL para describir los servicios web, y emplearla puede resultar más complejo. 

<!-- ¿Qué son los métodos HTTP comunes utilizados en una API REST? -->

GET: se usa para obtener un recurso en específico
POST: se utiliza para crear un nuevo recurso
PUT: actualiza un recurso existente por completo
DELTE: se encarga de eliminar un recurso
PATCH: actualiza parcialmente un recurso

