# manejo de version python... ver en comando, componentes minimos para ejecutar app python..
# Imagen Base
FROM python:3.12.3-slim-bullseye 

# Setear variables de entorno... DESACTIVAR LA COMPROBACION DE VERSIONES DE PIP... SE EVITA QUE PIP VEA VERSIONES...
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# EVITAR GENERACION DE ARCHIVOS PYC... REDUCIR ESPACIO DE ALMACENAMIENTO Y MEJOR RENDIMIENTO DE LA APP
ENV PYTHONDONTWRITEBYTECODE 1
# DESACTIVAR EL ALMACENAMIENTO EN BUFFER.. SALIDA SE MUESTRA DE FORMA INMEDIATA..
ENV PYTHONUNBUFFERED 1


# Setear directorio de trabajo... si no existe docker lo crea... la ejecucion se realiza en este directorio...
WORKDIR /code 

# # Actualizar el sistema e instalar las dependencias necesarias para OpenCV
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     cmake \
#     libglib2.0-0 \
#     libgl1-mesa-glx \
#     libgl1 \
#     libsm6 \
#     libxext6 \
#     libxrender1 \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*



# Instalar Rust y Cargo
#RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
#ENV PATH=/root/.cargo/bin:$PATH

# EL CONTENEDOR DOCKER SE EJECUTA CON LINUX OJOOOO!!! NADA DE WINDOWS EN REQUIREMENTS... DARA ERROR...
# borrar todos los arhivos que tengan win... el tensorflow de intel y python 3.12.3... 
# en requirements.txt ir borrando sino no carga y da error... para borrar ir en usuarios y borrar el vhdx...
# sino ocupa espacio al pedo...

# instalar dependencias requirements.txt ... cuando se pone . se refiere al directorio de trabajo osea app en este caso..
COPY ./requirements.txt . 

# # instalar dependencias del archivo de requerimientos...
# RUN pip install --default-timeout=2000 -r requirements.txt

# Aumentar el tiempo de espera para pip install
RUN pip install --default-timeout=3000 -r requirements.txt

# copiar proyecto inicio y destino . . copiar dentro del directorio de trabajo..
COPY . . 

