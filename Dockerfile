# Usa una imagen base de Python
FROM python:3.12

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación al contenedor
COPY . .

# Expone el puerto en el que se ejecutará la aplicación Flask
EXPOSE 4300

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
