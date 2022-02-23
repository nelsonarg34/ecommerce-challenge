# Lista de Tareas

## Configuración inicial

Este proyecto incluye migraciones predeterminadas, también incluye una base de datos SQLITE con datos de ejemplo.

1.- Clonar este repositorio:

    git clone https://github.com/nelsonarg34/lista_tareas.git 

2.- Crear un entorno virtual:

    virtualenv venv

3.- Active el entorno virtual.

4.- Instalar librerias.

    (venv) pip install -r requirements.txt 

5.- Correr servidor:

    venv) python manage.py runserver 
<br>

## Autenticación y registro de usuarios

### Características
- Registrar una cuenta
- Iniciar y cerrar sesión
- Restaurar contraseña

###     End points

http://localhost:8000/api/user/auth/login/

http://localhost:8000/api/user/auth/logout/

http://localhost:8000/api/user/auth/signup/

http://localhost:8000/api/user/auth/reset/

http://localhost:8000/api/user/profile/

<br>

## Listas de tareas de usuarios

Interacción entre los usuarios y listas de tareas

###     End points

Listas (GET, POST): http://127.0.0.1:8000/api/lists/

Listas (GET, PUT, PATCH, DELETE): http://127.0.0.1:8000/api/lists/1/

Tareas (GET, POST): http://127.0.0.1:8000/api/tasks/

Tareas (GET, PUT, PATCH, DELETE): http://127.0.0.1:8000/api/tasks/1/

<br>

## Búsquedas y filtros

- Búsqueda: Usando un texto y buscando coincidencias.
- Ordenación: Ascendente o descendente a partir de varios campos.
- Filtrado: En base a a partir de varios campos.

###     End points

http://127.0.0.1:8000/api/list_filters/

<br>

## Proyecto con Docker

1.- Creación del proyecto:

    docker-compose run web django-admin startproject <nombre-proyecto> 

2.- Construcción del contenedor:

    docker-compose -f docker-compose.yml build

3.- Modificar el archivo settings.py del proyecto:

Realizar las siguientes modificaciones para poder comunicarnos con nuestra base de datos.

    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['POSTGRES_DB'],
            'USER': os.environ['POSTGRES_USER'],
            'PASSWORD': os.environ['POSTGRES_PASSWORD'],
            'HOST': os.environ['POSTGRES_HOST'],
            'PORT': os.environ['POSTGRES_PORT'],
        }
    }

4.- Correr build y up:

    docker-compose -f docker-compose.yml build
    docker-compose up

5.- Correr  makemigrations y migrate:

    docker-compose -f .\docker-compose.yml run --rm web python manage.py makemigrations
    docker-compose -f .\docker-compose.yml run --rm web python manage.py migrate

6.- Crear super usuario:

    docker-compose -f .\docker-compose.yml run --rm web python manage.py createsuperuser

6.- Con el contenedor corriendo:

    Acceder a http://localhost:8000/admin


