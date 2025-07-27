import csv
import os
import uuid

FILENAME = "favoritos.csv"

def save_favorite(data):
    id_fav = str(uuid.uuid4())
    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id_fav, data["nombre"], data["pokemon"]])
    return {"success": True, "id": id_fav}

def delete_favorite(data):
    id_fav = data.get("id")
    nombre = data.get("nombre")
    found = False
    rows = []

    if not os.path.exists(FILENAME):
        return {"success": False}

    with open(FILENAME, newline="") as f:
        for row in csv.reader(f):
            if row[0] == id_fav and row[1] == nombre:
                found = True
            else:
                rows.append(row)

    with open(FILENAME, "w", newline="") as f:
        csv.writer(f).writerows(rows)
    return {"success": found}

def list_favorites(nombre):
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, newline="") as f:
        return [{"id": r[0], "pokemon": r[2]} for r in csv.reader(f) if r[1] == nombre]

def get_favorite_by_id(id_fav, nombre):
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, newline="") as f:
        for r in csv.reader(f):
            if r[0] == id_fav and r[1] == nombre:
                return {"id": r[0], "pokemon": r[2]}
    return {}
