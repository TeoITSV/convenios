# Usa la imagen base de Python para Django
FROM python:3.7-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala el compilador de C
RUN apt-get update && apt-get install -y build-essential

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY . .

# Expone el puerto 8000 para que Django pueda ser accesible desde el exterior
EXPOSE 8000

# Comando para iniciar el servidor Django
CMD ["python", "convenios/manage.py", "runserver", "0.0.0.0:8000"]
