# Usa la imagen base de Python para Django
FROM python:3.7-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala el compilador de C
RUN apt-get update

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# crea los directorios
RUN mkdir -p convenios/crearConvenios/media/resultado/ConveniosIndividuales 
RUN mkdir -p convenios/crearConvenios/media/resultado/ConveniosMarco 
RUN mkdir -p convenios/crearConvenios/media/resultado/Diplomas 

# Copia el código de la aplicación al contenedor
COPY . .

# Expone el puerto 8000 para que Django pueda ser accesible desde el exterior
EXPOSE 8000

# Genera las migraciones y migra la base de datos
RUN python convenios/manage.py makemigrations
RUN python convenios/manage.py migrate
RUN python convenios/manage.py collectstatic --noinput
# Comando para iniciar el servidor Django
CMD ["python", "convenios/manage.py", "runserver", "0.0.0.0:8000"]
