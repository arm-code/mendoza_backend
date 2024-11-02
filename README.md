# TO CREATE THE FILE requeriments.txt
pip freeze > requirements.txt

# TO INSTALL ALL LIBRARYS FROM requeriments.txt file
pip install -r requirements.txt

# Para crear un superusuario en Django desde la consola, sigue estos pasos:

1. Abre tu terminal y asegúrate de estar en el directorio principal de tu proyecto Django.
2. Activa tu entorno virtual, si es necesario.
3. Ejecuta el siguiente comando:   
   python manage.py createsuperuser  
4. Django te pedirá que ingreses un nombre de usuario, correo electrónico y contraseña para el superusuario. Completa estos datos.
