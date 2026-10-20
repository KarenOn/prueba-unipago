from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AnimeBody(BaseModel):
        Nombre: str
        Año: int
        Genero: str
        Estado: str

animes = [
    {
        "AnimeID": 1,
        "Nombre": "Dragon Ball",
        "Año": 1986,
        "Genero": "Shonen",
        "Estado": "Activo"
    },
    {
        "AnimeID": 2,
        "Nombre": "Naruto",
        "Año": 2002,
        "Genero": "Shonen",
        "Estado": "Activo"
    }
]

@app.get("/")
def read():
    return animes

@app.get("/{animeid}")
def find(animeid: int):
    anime = [a for a in animes if a["AnimeID"] == animeid]
    return anime

@app.post("/anime/")
def add(item: AnimeBody):
    lastAnime = animes[len(animes) - 1]

    animes.append({
        "AnimeID": lastAnime['AnimeID'] + 1,
        "Nombre": item.Nombre,
        "Año": item.Año,
        "Genero": item.Genero,
        "Estado": item.Estado
    })
    return animes

@app.put('/anime/{animeid}')
def update(animeid: int, anime: AnimeBody):
    for a in animes:
        if a["AnimeID"] == animeid:
            a['Nombre'] = anime.Nombre
            a['Año'] = anime.Año
            a['Genero'] = anime.Genero
            a['Estado'] = anime.Estado

            return a

    return "Anime no encontrado"

@app.delete('/anime/{animeid}')
def delete(animeid: int):
    for i,a in enumerate(animes):
        if a["AnimeID"] == animeid:
            animes.pop(i)
            return "Anime eliminado correctamente"

    return "Anime no encontrado"