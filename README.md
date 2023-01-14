# API REST con django para guardar datos de proyectos


## Instalación 
#

### Clonar el repositorio
```
https://github.com/josuema2002/crud-apirest-django_Projects.git
```
### Crear un entorno virtual
```
python -m venv venv
```
```
.\venv\Scripts\activate
```
### Instalar las dependencias
```
pip install -r requirements.txt
```
### Crear la base de datos
```
python manage.py makemigrations
```
```
python manage.py migrate
```
### Crear un superusuario
```
python manage.py createsuperuser
```
### Ejecutar el servidor
```
python manage.py runserver
```
### Acceder a la API desarrollo
* GET      http://127.0.0.1:8000/api/projects/

* POST     http://127.0.0.1:8000/api/projects/

* PATCH    http://127.0.0.1:8000/api/projects/${id}/

* DELETE   http://127.0.0.1:8000/api/projects/${id}/


### Acceder al panel de administración
http://127.0.0.1:8000/admin/

### Acceder a la documentación de django-rest-framework
https://www.django-rest-framework.org/

# Acceder a la API producción

### https://crud-apirest-django.onrender.com/api/projects/
