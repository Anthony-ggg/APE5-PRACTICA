📘 Proyecto de Gestión de Usuarios con Flask y JSON

Este proyecto implementa una aplicación web completa usando Flask, que permite:

Visualizar usuarios almacenados en un archivo JSON

Agregar nuevos usuarios

Todo mediante rutas HTML renderizadas con plantillas Jinja, más un archivo usuarios.json usado como base de datos mock.

📁 Estructura del Proyecto
/api
  ├── app.py                # API + Rutas web con Flask
  ├── usuarios.json         # Base de datos mock JSON
  ├── /templates
  │     ├── layout.html     # Plantilla base
  │     ├── index.html      # Página: Ver usuarios
  │     ├── agregar_usuario.html  # Página: Agregar usuario
  └── README.md             # Esta documentación

🛠️ Tecnologías Utilizadas
Backend

Python 3

Flask

JSON como base de datos mock

Jinja2 templates (integrado en Flask)

Frontend

HTML5

CSS3

Bootstrap (opcional si deseas agregar estilo después)

Herramientas

VS Code

Browser DevTools

Git/GitHub

▶️ Ejecución del Proyecto
1️⃣ Instalar dependencias
cd api
pip install flask

2️⃣ Ejecutar Flask
python app.py


Tu aplicación se ejecutará en:

👉 http://127.0.0.1:5000/

🌐 Rutas disponibles
Página principal — Ver usuarios
GET /


Muestra todos los usuarios almacenados en usuarios.json.

Página para agregar usuarios
GET /agregar_usuario


Despliega un formulario HTML.

POST /guardar_usuario


Guarda un usuario nuevo en usuarios.json.

API interna para obtener usuarios (opcional)
GET /api/usuarios


Retorna el JSON completo de usuarios.

📦 Estructura del JSON (usuarios.json)

Ejemplo utilizado actualmente:

[
  {
    "id": 1,
    "nombre": "Anthony",
    "email": "anthony@example.com"
  },
  {
    "id": 2,
    "nombre": "Daniela",
    "email": "daniela@example.com"
  },
  {
    "id": 3,
    "nombre": "Carlos",
    "email": "carlos@example.com"
  }
]

📊 Tabla de Pruebas HTTP

Método	URL	Código	Descripción
GET	/	200	Visualiza usuarios
GET	/agregar_usuario	200	Muestra formulario
POST	/guardar_usuario	302 → 200	Guarda usuario y redirige
GET	/api/usuarios	200	Devuelve JSON de usuarios
🔐 CORS

No es necesario CORS en este proyecto porque todas las vistas y la API están en el mismo dominio (localhost:5000).

📝 Códigos de Estado Relevantes

200 OK → Petición correcta

302 Found → Redirección luego de un POST

404 Not Found → Ruta no encontrada

500 Internal Server Error → Error del backend

📸 Capturas sugeridas para tu documentación

Vista de “Ver usuarios”

Vista de “Agregar usuario”

usuarios.json actualizado después de agregar

Terminal mostrando peticiones

DevTools → Network verificando redirecciones (POST → 302 → GET)

🎯 Ejemplos de Uso
✔ Agregar un usuario

Ir a:
http://127.0.0.1:5000/agregar_usuario

Llenar formulario:

Nombre

Email

Guardar → Regresa a “Ver usuarios”

El usuario aparece ahora en la lista

📌 Notas del Proyecto

El ID se genera automáticamente usando int(time.time())

usuarios.json se sobrescribe con cada actualización

No requiere base de datos real

Fácil de expandir para CRUD completo