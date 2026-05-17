# RPG Daily Quests API - Documentacion de Endpoints

Base URL: https://tu-api-rpg.onrender.com
Documentacion interactiva: https://tu-api-rpg.onrender.com/docs

---

## Health Check

**GET /** o **HEAD /**
Obtiene el estado general de la API.

**Respuesta (200 OK):**
```json
{
  "titulo": "RPG Daily Quests API",
  "version": "1.0",
  "descripcion": "API de misiones estilo RPG para estudiantes universitarios",
  "documentacion": "/docs",
  "status": "online"
}
```

---

## Misiones

**GET /misiones**
Obtiene la lista de todas las misiones registradas.
**Respuesta (200 OK):** Lista de objetos de misiones.

**GET /misiones/{mision_id}**
Obtiene los detalles de una mision especifica por su ID.
**Respuesta (200 OK):** Objeto de la mision seleccionada.
**Error (404 Not Found):** `{"detail": "Mision no encontrada"}`

**POST /misiones/auto** (Recomendado)
Crea una nueva mision con ID autoincremental.

**Cuerpo de la solicitud:**
```json
{
  "descripcion": "Estudiar para el examen de algoritmos",
  "xp": 100
}
```

**Respuesta (200 OK):**
```json
{
  "mensaje": "Mision creada automaticamente",
  "id": 1,
  "mision": {
    "id": 1,
    "descripcion": "Estudiar para el examen de algoritmos",
    "xp": 100,
    "estado": "pendiente"
  }
}
```
**Error (400 Bad Request):** `{"detail": "Maximo 10 misiones activas"}`

**POST /misiones**
Crea una nueva mision especificando un ID manual.

**Cuerpo de la solicitud:**
```json
{
  "id": 5,
  "descripcion": "Completar tarea de matematicas",
  "xp": 50,
  "estado": "pendiente"
}
```
**Respuesta (200 OK):** `{"mensaje": "Mision creada", "mision": {...}}`
**Error (400 Bad Request):** `{"detail": "Maximo 10 misiones activas"}`

**PUT /misiones/{mision_id}**
Modifica la descripcion, los puntos de experiencia o el estado de una mision existente.

**Cuerpo de la solicitud:**
```json
{
  "descripcion": "Estudiar para el examen de algoritmos y estructuras de datos",
  "xp": 150,
  "estado": "pendiente"
}
```
**Respuesta (200 OK):** `{"mensaje": "Mision actualizada", "mision": {...}}`
**Error (404 Not Found):** `{"detail": "Mision no encontrada"}`

**DELETE /misiones/{mision_id}**
Elimina una mision del sistema y su registro del historial en cascada.
**Respuesta (200 OK):** `{"mensaje": "Mision eliminada"}`
**Error (404 Not Found):** `{"detail": "Mision no encontrada"}`

---

## Historial de Completados

**PUT /misiones/{mision_id}/completar**
Marca una mision como completada y genera un registro en la tabla de historial.

**Respuesta (200 OK):**
```json
{
  "mensaje": "Mision completada",
  "xp_ganada": 100
}
```
**Error (400 Bad Request):** `{"detail": "La mision ya fue completada"}`
**Error (404 Not Found):** `{"detail": "Mision no encontrada"}`

**GET /misiones/completadas**
Obtiene el historial de todas las misiones marcadas como completadas.

**Respuesta (200 OK):**
```json
[
  {
    "id": 1,
    "mision_id": 4,
    "descripcion": "Asistir a clase de base de datos",
    "xp": 20,
    "fecha_completada": "2026-05-16 12:00:00"
  }
]
```

---

## Estadisticas Generales

**GET /estadisticas**
Obtiene el conteo de misiones pendientes, completadas y la experiencia total acumulada.

**Respuesta (200 OK):**
```json
{
  "misiones_pendientes": 12,
  "misiones_completadas": 3,
  "xp_total_ganada": 90
}
```

---

## ESTRUCTURA DE DATOS

**Modelo Mision:**
* **id** (integer): Identificador unico
* **descripcion** (string): Descripcion de la mision
* **xp** (integer): Puntos de experiencia al completar
* **estado** (string): "pendiente" o "completada"
* **fecha_creacion** (timestamp): Se genera automaticamente

**Modelo MisionCrear:**
* **descripcion** (string): Descripcion de la mision
* **xp** (integer): Puntos de experiencia al completar
* **estado** (string): "pendiente" o "completada" (opcional, por defecto "pendiente")

---

## LIMITES Y RESTRICCIONES

* Maximo 10 misiones activas simultaneamente
* Las misiones completadas se guardan en el historial
* No se pueden completar misiones que ya fueron completadas
* Al eliminar una mision, se elimina automaticamente su historial asociado
* El ID se genera automaticamente cuando usas `POST /misiones/auto`

---

## CODIGOS DE ESTADO HTTP

* **200:** Solicitud exitosa
* **404:** Recurso no encontrado
* **400:** Solicitud invalida o limite excedido
* **500:** Error interno del servidor