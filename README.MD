# Proyecto Python: Microservice Python Authenticacion

Guía de instalación y ejecución del proyecto:

## Configuración con Docker

### Requisitos previos
- Docker version 24 o superior instalado en tu sistema.

### Pasos detallados para configurar con Docker

1. **Navega al directorio del proyecto:** 
    ```bash
    cd auth_login_service
    ```

2. **Ejecuta el contenedor Docker:** 
    - En Windows (ejecutar como administrador): 
        ```bash
        docker compose -f docker-compose.yml up -d
        ```
    - En Linux (ejecutar con sudo): 
        ```bash
        sudo docker compose -f docker-compose.yml up -d
        ```

3. **¡Listo! Ahora puedes acceder a la aplicación desde `http://localhost:4300`.**

4. **Ver el log del contenedor docker:** 
    - En Windows (ejecutar como administrador): 
        ```bash
        docker logs -f auth_service_jockey .
        ```
    - En Linux (ejecutar con sudo): 
        ```bash
        sudo docker logs -f auth_service_jockey .
        ```

### Nota
- Asegúrate de que los puertos utilizados no estén ocupados por otros servicios en tu sistema.

### Configuración de entornos

- Para entornos de producción, descomenta la siguiente línea en el archivo especificado (`auth_service/domain/services/EncryptService.py`):

```python
# Ruta al archivo de configuración en entorno de producción
# config_path = 'auth_service/domain/services/EncryptService.py'

==>Descomentar para entorno de Producción
    # Credenciales de Producción
    self.key = b"1wOS377woe39ksf/"
    self.iv = b"qawsedploeSD(234"

    # Credenciales de Desarrollo
    # self.key = b"oW1mY2vHAXbiBQtL"
    # self.iv = b"CmYUOq8cIpyr1H6p"
```

### Configuración del archivo .env

Para especificar el host y el puerto, crea un archivo `.env` en el directorio raíz del proyecto utilizando el archivo `.env.example` como ejemplo. Copia el contenido del archivo `.env.example` y pégalo en el archivo `.env`, luego modifica los valores según tus necesidades.

Aquí está un ejemplo del contenido del archivo `.env`:

```dotenv
HOST_PY=0.0.0.0
PORT_PY=4300
```
