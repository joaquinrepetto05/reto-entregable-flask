from datetime import datetime
from pokebase import pokemon as get_pokemon
from utils.date_utils import zodiac_sign
from models.zodiac_mapping import ZODIAC_POKEMON

def get_pokemon_horoscope(nombre, fecha_nacimiento):
    try:
        fecha = datetime.fromisoformat(fecha_nacimiento).date()
        signo = zodiac_sign(fecha)
        poke_name = ZODIAC_POKEMON.get(signo, "pikachu")
        p = get_pokemon(poke_name)

        return {
            "nombre_usuario": nombre,
            "signo": signo,
            "pokemon": {
                "nombre": p.name,
                "imagen": p.sprites.front_default,
                "tipo": [t.type.name for t in p.types],
                "altura": p.height,
                "peso": p.weight,
                "habilidades": [a.ability.name for a in p.abilities]
            }
        }
    except Exception as e:
        return {"error": str(e)}
