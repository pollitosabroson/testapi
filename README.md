# testapi
Create rest api Manual


Para la funcionalidad del sistema, primero se tienen que instalas lo requrimientos con el siguiente comando:

 ```bash
    $ pip install -r requirements.txt
    ```
    
Despues de instalar los requerimientos del sistema se corre el siguiente comando:

 ```bash
    $ python manage.py migrate
    ```
Con este comando corremos las migraciones que se requieren para que el sistema este funcionando.

Ahora agregamos datos falsos a nuestra base de datos

```bash
    python manage.py loaddata fixtures.json
    ```


Y por ultimo corremos el servidor con el siguiente comando:

```bash
    python manage.py runserver
    ```
 
