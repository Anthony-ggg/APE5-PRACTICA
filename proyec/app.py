from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

USERS_FILE = "users.json"


# ---------------------------
# Cargar usuarios desde JSON
# ---------------------------
def cargar_usuarios():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------
# Guardar usuarios en JSON
# ---------------------------
def guardar_usuarios(usuarios):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)


# ---------------------------
# RUTA PRINCIPAL: Ver usuarios
# ---------------------------
@app.route("/")
def inicio():
    usuarios = cargar_usuarios()
    return render_template("index.html", usuarios=usuarios)


# ---------------------------
# RUTA: Formulario para agregar usuario
# ---------------------------
@app.route("/agregar")
def agregar_usuario():
    return render_template("agregar_usuario.html")


# ---------------------------
# RUTA: Procesar formulario
# ---------------------------
@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    nombre = request.form["nombre"]
    correo = request.form["correo"]

    usuarios = cargar_usuarios()

    # Crear ID secuencial
    nuevo_id = max([u["id"] for u in usuarios], default=0) + 1

    nuevo_usuario = {
        "id": nuevo_id,
        "nombre": nombre,
        "correo": correo
    }

    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
