from flask import Flask, request, jsonify
from services.horoscope_service import get_pokemon_horoscope
from services.pokemon_service import search_pokemon
from services.favorites_service import (
    save_favorite,
    delete_favorite,
    list_favorites,
    get_favorite_by_id
)

app = Flask(__name__)

@app.post("/horoscopo")
def horoscopo():
    data = request.get_json()
    nombre = data.get("nombre")
    fecha = data.get("fecha_nacimiento")
    if not nombre or not fecha:
        return jsonify({"error": "Faltan datos"}), 400
    return jsonify(get_pokemon_horoscope(nombre, fecha))

@app.get("/pokemon")
def buscar_pokemon():
    nombre = request.args.get("nombre")
    tipo = request.args.get("tipo")
    if not nombre and not tipo:
        return jsonify({"error": "Debe enviar nombre o tipo"}), 400
    return jsonify(search_pokemon(nombre, tipo))

@app.post("/favoritos")
def guardar_favorito():
    data = request.get_json()
    return jsonify(save_favorite(data))

@app.delete("/favoritos")
def eliminar_favorito():
    data = request.get_json()
    return jsonify(delete_favorite(data))

@app.get("/favoritos")
def listar_favoritos():
    usuario = request.args.get("usuario")
    if not usuario:
        return jsonify({"error": "Debe indicar usuario"}), 400
    return jsonify(list_favorites(usuario))

@app.get("/favoritos/<id>")
def favorito_por_id(id):
    usuario = request.args.get("usuario")
    if not usuario:
        return jsonify({"error": "Debe indicar usuario"}), 400
    return jsonify(get_favorite_by_id(id, usuario))

if __name__ == "__main__":
    app.run(debug=True)
