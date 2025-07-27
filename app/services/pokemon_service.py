from pokebase import pokemon as get_pokemon, type_ as get_type

def search_pokemon(nombre=None, tipo=None):
    try:
        if nombre:
            p = get_pokemon(nombre.lower())
            return [{
                "nombre": p.name,
                "imagen": p.sprites.front_default,
                "tipo": [t.type.name for t in p.types],
                "altura": p.height,
                "peso": p.weight,
                "habilidades": [a.ability.name for a in p.abilities]
            }]
        elif tipo:
            t = get_type(tipo.lower())
            return [{"nombre": p.pokemon.name} for p in t.pokemon]
    except:
        return []
