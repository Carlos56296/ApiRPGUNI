RPG Daily Quests API

API REST de misiones estilo RPG para estudiantes universitarios.

Instalacion Local

1. Clonar repositorio:
git clone <tu-repo>
cd apimisiones

2. Crear entorno virtual:
python -m venv venv
venv\Scripts\activate

3. Instalar dependencias:
pip install -r requirements.txt

4. Ejecutar:
python -m uvicorn APIMisiones:app --reload

5. Acceder a:
API: http://localhost:8000
Docs: http://localhost:8000/docs

Gestion de la Base de Datos Local

El proyecto incluye un script interactivo para administrar el estado de las misiones localmente antes de desplegar. 
Para ejecutarlo, usa el comando:

python gestionar_bd.py

Opciones disponibles en el menu:
1. Borrar todo: Vacia por completo las tablas de misiones e historial, reiniciando los IDs a 1.
2. Llenar datos: Inserta las 15 misiones universitarias iniciales por defecto.
3. Reiniciar (Borrar y llenar): Limpia la base de datos y vuelve a cargar las misiones desde cero.

Desplegar en Render

Base URL del despliegue: https://apirpguni.onrender.com (Reemplazar con tu URL final)

Pasos para el despliegue automatizado:
1. Crear cuenta en https://render.com
2. Conectar el repositorio de GitHub de la API.
3. Crear un nuevo Web Service.
4. Seleccionar la opcion de Docker.
5. Render detectara y utilizara el archivo render.yaml de forma automatica para configurar el entorno.

Estructura del Proyecto

apimisiones/
  APIMisiones.py          - Archivo principal de la API (FastAPI)
  gestionar_bd.py         - Script interactivo para limpiar o llenar la base de datos
  requirements.txt        - Dependencias de Python
  Dockerfile              - Configuracion del contenedor para produccion
  docker-compose.yml      - Orquestacion de contenedores local
  render.yaml             - Configuracion de infraestructura para Render
  .gitignore              - Archivos excluidos de Git (rpg.db esta incluido para mantener datos iniciales)
  runtime.txt             - Version de Python especificada para el servidor
  readme_api.md           - Documentacion tecnica de endpoints
  test_endpoints.py       - Script de pruebas integradas de endpoints
  rpg.db                  - Archivo de base de datos SQLite pre-cargada

Variables de Entorno

Actualmente la API no requiere variables de entorno adicionales.

Testing

Para validar que todos los endpoints responden correctamente de manera local, ejecuta:
python test_endpoints.py

Nota: Requiere que la API este corriendo previamente en http://localhost:8000

Prueba