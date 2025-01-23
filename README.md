# Catálogo de Vehículos en Django

Este proyecto es una aplicación web desarrollada con el framework Django que permite gestionar un catálogo de vehículos. Los usuarios pueden ver una lista de vehículos, agregar nuevos vehículos (con permisos adecuados) y gestionar sus perfiles.

## Funcionalidades

*   Listado de vehículos con filtros por precio (bajo, medio, alto).
*   Formulario para agregar nuevos vehículos.
*   Autenticación de usuarios (registro, inicio de sesión, cierre de sesión).
*   Página de perfil de usuario.
*   Interfaz de administración de Django para gestionar los datos.

## Tecnologías Utilizadas

*   Python
*   Django
*   Bootstrap 5 (integrado con `django-bootstrap-v5`)
*   django-crispy-forms
*   crispy-bootstrap5

## Instalación

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/Zprit3/proyecto_vehiculos_django.git
    ```

2.  **Crear un entorno virtual (recomendado):**

    ```bash
    python -m venv .venv       # Crea el entorno virtual (Python 3.3+)
    .venv\Scripts\activate   # Activa el entorno virtual (Windows)
    source .venv/bin/activate # Activa el entorno virtual (macOS/Linux)
    ```

3.  **Instalar las dependencias:**

    Este proyecto utiliza un archivo `requirements.txt` para gestionar las dependencias. Para instalarlas, ejecuta el siguiente comando:

    ```bash
    pip install -r requirements.txt
    ```

    Este comando instalará todas las bibliotecas necesarias, incluyendo Django, Bootstrap y otras dependencias.

4.  **Migraciones:**

    Aplica las migraciones de Django para crear las tablas en la base de datos:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Crear un superusuario:**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Ejecutar el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

    Accede a la aplicación en tu navegador en `http://127.0.0.1:8000/`.

## Uso de `requirements.txt`

El archivo `requirements.txt` es crucial para la gestión de dependencias en este proyecto. Contiene una lista de todas las bibliotecas de Python necesarias para que la aplicación funcione correctamente.

*   **Para generar `requirements.txt`:**

    Después de instalar nuevas bibliotecas con `pip install <nombre_paquete>`, ejecuta el siguiente comando para actualizar el archivo:

    ```bash
    pip freeze > requirements.txt
    ```

*   **Para instalar dependencias desde `requirements.txt`:**

    En un nuevo entorno o después de clonar el repositorio, ejecuta:

    ```bash
    pip install -r requirements.txt
    ```

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o tienes una sugerencia de mejora, por favor abre un issue o envía un pull request.
