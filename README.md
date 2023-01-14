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
# Acceder a la API
## URL
### https://crud-apirest-django.onrender.com/

## headers:

```Authorization: Token ${token}```

* GET      http://crud-apirest-django.onrender.com/api/v1/projects/

* POST     http://crud-apirest-django.onrender.com/api/v1/projects/

* PATCH    http://crud-apirest-django.onrender.com/api/v1/projects/${id}/

* DELETE   http://crud-apirest-django.onrender.com/api/v1/projects/${id}/


# Crear un usuario
### http://crud-apirest-django.onrender.com/api/v1/user/create_user/
post > body: {
  "username": "...",
  "first_name": "...",
  "last_name": "...",
  "email": "...",
  "password": "..."
}

# Obtener token via login
### http://crud-apirest-django.onrender.com/api/v1/user/token/
post > body: {
  "username": "...",
  "password": "..."
}
