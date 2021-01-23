# Invera ToDo-List Challenge (Python/Django Jr-SSr)

El propósito de esta prueba es conocer tu capacidad para crear una pequeña aplicación funcional en un límite de tiempo. A continuación, encontrarás las funciones, los requisitos y los puntos clave que debés tener en cuenta durante el desarrollo.

## Qué queremos que hagas:

- El Challenge consiste en crear una aplicación web sencilla que permita a los usuarios crear y mantener una lista de tareas.
- La entrega del resultado será en un nuevo fork de este repo y deberás hacer una pequeña demo del funcionamiento y desarrollo del proyecto ante un super comité de las más grandes mentes maestras de Invera, o a un par de devs, lo que sea más fácil de conseguir.
- Podes contactarnos en caso que tengas alguna consulta.

## Objetivos:

El usuario de la aplicación tiene que ser capaz de:

- Crear una tarea
- Eliminar una tarea
- Marcar tareas como completadas
- Poder ver una lista de todas las tareas existentes
- Filtrar/buscar tareas por fecha de creación y/o por el contenido de la misma

## Qué evaluamos:

- Desarrollo utilizando Python, Django. No es necesario crear un Front-End, pero sí es necesario tener una API que permita cumplir con los objetivos de arriba.
- Calidad y arquitectura de código. Facilidad de lectura y mantenimiento del código. Estándares seguidos.
- [Bonus] Manejo de logs.
- [Bonus] Creación de tests (unitarias y de integración)
- [Bonus] Unificar la solución propuesta en una imagen de Docker por repositorio para poder ser ejecutada en cualquier ambiente (si aplica para full stack).

## Requerimientos de entrega:

- Hacer un fork del proyecto y pushearlo en github. Puede ser privado.
- La solución debe correr correctamente.
- El Readme debe contener todas las instrucciones para poder levantar la aplicación, en caso de ser necesario, y explicar cómo se usa.
- Disponibilidad para realizar una pequeña demo del proyecto al finalizar el challenge.
- Tiempo para la entrega: Aproximadamente 7 días.

## Installation to Python 3.6.X version

### Check if pyvenv is installed.

```bash
$ whereis pyvenv-3
```

If nothing appears, execute the next command. Otherwise procede next step.

```bash
$ sudo apt-get install python3-venv
```

### Create your virtual enviroment 'venvToDo' 

```bash
$ python3 -m venv venvToDo
```

### Download repository, activate your virtual enviroment

```bash
$ git clone https://github.com/Knd9/todo-challenge.git
$ source venvToDo/bin/activate
$ cd todo-challenge
```

### Install resources in your venv

```bash
$ pip install -r requirements.txt
```

Then you have to modify a single line in the file `swagger_base.html`

```bash
$ sed -i 's/staticfiles/static/g' ../venvToDo/lib/python3.6/site-packages/swagger_ui/templates/swagger_base.html
```

And you have to add the next `.css` and `.png` files

```bash
$ wget https://raw.githubusercontent.com/swagger-api/swagger-ui/master/dist/swagger-ui.css -P ../venvToDo/lib/python3.6/site-packages/swagger_ui/static/swagger-ui/dist/
$ wget https://raw.githubusercontent.com/swagger-api/swagger-ui/master/dist/favicon-16x16.png -P ../venvToDo/lib/python3.6/site-packages/swagger_ui/static/swagger-ui/dist/
```

To desable warning of YAML, you have to modify a single line in the file `swagger_ui/views.py` of the venv

```bash
$ sed -i 's/read()/read(), Loader=yaml.FullLoader/1' ../venvToDo/lib/python3.6/site-packages/swagger_ui/views.py
```

To desable Werkzeug warning, modify a single line in the file `flask_restplus/fields.py`

```bash
$ sed -i 's/from werkzeug import/from werkzeug.utils import/1' ../venvToDo/lib/python3.6/site-packages/flask_restplus/fields.py
```

### Migrate

```bash
$ python manage.py migrate
```

### Run your django server 

```bash
$ python manage.py runserver
```
Something like this will appear:

(...)
```
Django version 3.1.5, using settings 'toDoProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Run tests

```bash
$ pytest --create-db
```

### To deploy

```bash
$ python manage.py collectstatic
```

### To deactivate your 'venvToDo' venv

```bash
$ deactivate
```

## Use instructions

This is an app that provides create, filter, list and delete To Do's methods. 
Once you run the server, you must enter to [api](http://localhost:8000/api-doc/) in your web browser. Then you have the use the basic swagger browseable api.
