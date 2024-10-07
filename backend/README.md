# Backend con FLASK API RESTFUL

### Comandos
    Creación de entorno virutal
    python -m venv .venv

    Activar entorno virtual
    .env/Scripts/activate

    Desactivar Entorno virtual
    deactivate

    Instalación inicial: 
    pip install -r requirements.txt

    Asignar variable de la aplicación
    Windows PowerShell
    $env:FLASK_APP = "manage.py"
    Windows cmd
    set FLASK_APP=manage.py
    Linux
    export FLASK_APP=manage.py

    Activar DEBUG
    Windows PowerShell
    $env:FLASK_DEBUG = "1"
    Windows cmd
    set FLASK_DEBUG=1
    Linux
    export FLASK_DEBUG=1

    Ejecutar test:
    flask test
    
    Ejecutar la aplicación: 
    flask run

### Acceder a la aplicación ###

    Abrir la siguiente URL en su navegador para ver la documentación de swagger
    http://127.0.0.1:5000/

### Usando Postman ####

    El encabezado de autorización tiene el siguiente formato:
    
    Key: Authorization
    Valor: <token generado durante el inicio de sesión>