import sqlite3
import sys

DB_NAME = "rpg.db"

def crear_tablas_si_no_existen(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS misiones (
        id INTEGER PRIMARY KEY,
        descripcion TEXT,
        xp INTEGER,
        estado TEXT,
        fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS historial (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mision_id INTEGER,
        descripcion TEXT,
        xp INTEGER,
        fecha_completada DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (mision_id) REFERENCES misiones(id) ON DELETE CASCADE
    )
    """)

def borrar_todo():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        crear_tablas_si_no_existen(cursor)
        
        cursor.execute("PRAGMA foreign_keys = OFF;")
        cursor.execute("DELETE FROM historial")
        cursor.execute("DELETE FROM misiones")
        
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='historial'")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='misiones'")
        
        conn.commit()
        print("Base de datos borrada por completo.")
    except sqlite3.Error as e:
        print(f"Error al borrar: {e}")
    finally:
        conn.close()

def llenar_datos():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        crear_tablas_si_no_existen(cursor)
        
        misiones = [
            (1, "Estudiar para el examen de algoritmos", 100, "pendiente"),
            (2, "Completar tarea de matematicas", 50, "pendiente"),
            (3, "Hacer proyecto de programacion", 200, "pendiente"),
            (4, "Asistir a clase de base de datos", 20, "completada"),
            (5, "Terminar reporte de practicas", 150, "pendiente"),
            (6, "Instalar Docker en la laptop", 30, "completada"),
            (7, "Resolver serie de ecuaciones diferenciales", 80, "pendiente"),
            (8, "Leer capitulo de sistemas operativos", 40, "pendiente"),
            (9, "Reunirse con el equipo para la API", 75, "en progreso"),
            (10, "Presentar el proyecto final", 500, "pendiente"),
            (11, "Pagar la colegiatura", 40, "completada"),
            (12, "Actualizar repositorio en GitHub", 90, "pendiente"),
            (13, "Depurar codigo en Python", 300, "en progreso"),
            (14, "Configurar servidor en Render", 400, "pendiente"),
            (15, "Sobrevivir a la semana de examenes", 1000, "pendiente")
        ]
        
        cursor.executemany(
            "INSERT OR IGNORE INTO misiones (id, descripcion, xp, estado) VALUES (?, ?, ?, ?)",
            misiones
        )

        historial = [
            (4, "Asistir a clase de base de datos", 20),
            (6, "Instalar Docker en la laptop", 30),
            (11, "Pagar la colegiatura", 40)
        ]

        cursor.executemany(
            "INSERT OR IGNORE INTO historial (mision_id, descripcion, xp) VALUES (?, ?, ?)",
            historial
        )
        
        conn.commit()
        print("Misiones e historial insertados correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar: {e}")
    finally:
        conn.close()

def mostrar_menu():
    while True:
        print("\n--- Gestionar Base de Datos ---")
        print("1. Borrar todo")
        print("2. Llenar datos")
        print("3. Reiniciar (Borrar y llenar)")
        print("4. Salir")
        
        opcion = input("Selecciona una opcion: ").strip()
        
        if opcion == "1":
            confirmar = input("Seguro que quieres borrar todo? (s/n): ").strip().lower()
            if confirmar == 's':
                borrar_todo()
                
        elif opcion == "2":
            llenar_datos()
            
        elif opcion == "3":
            confirmar = input("Seguro que quieres reiniciar todo? (s/n): ").strip().lower()
            if confirmar == 's':
                borrar_todo()
                llenar_datos()
                
        elif opcion == "4":
            print("Saliendo...")
            sys.exit()
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    mostrar_menu()