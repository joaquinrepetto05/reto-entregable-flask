# Horoscopo Pokemon

Este proyecto, desarrollado en Flask, permite:
- Realizar búsquedas de Pokemon usando la PokeAPI.
- Calcular el horóscopo Pokemon en base al signo zodiacal de un usuario.
- Guardar y modificar una lista de Pokemon favoritos en un archivo CSV.

## Requisitos previos
- Python 3.9 o superior.
- Pip (administrador de paquetes de Python).

> [!WARNING]
> Es importante cumplir con los requisitos previos, o no se podrá ejecutar el proyecto.

## Instalación y ejecución
1) Clonar el repositorio.
2) Acceder a la carpeta raíz del proyecto.
3) Crear un entorno virtual con el comando:

   ```bash
   python -m venv venv
   ```

4) Activar el entorno virtual usando uno de los siguientes comandos:
   En Windows:
   ```bash
   venv\Scripts\activate
   ```

   En macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

5) Instalar las dependencias del proyecto con el comando:

   ```bash
   pip install -r requirements.txt
   ```
> [!TIP]
> Una vez finalizado el proceso, ejectuar el proyecto con:
> ```bash
> python run.py
> ```

## Endpoints
A continuación se detalla el listado de endpoints contenidos en esta API:
1) POST /horoscopo: Calcula el horóscopo Pokemon según fecha de nacimiento.
2) GET /pokemon: Busca un Pokemon por nombre o tipo.
3) POST /favoritos: Guarda un Pokemon como favorito.
4) GET /favoritos: Lista los Pokemon favoritos de un usuario.
5) DELETE /favoritos: Elimina un Pokemon favorito.
