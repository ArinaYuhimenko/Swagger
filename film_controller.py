import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.film import Film  # noqa: E501
from swagger_server.models.films import Films  # noqa: E501
from swagger_server import util

films = []

def create_film(body):  # noqa: E501
    if connexion.request.is_json:
        body = Film.from_dict(connexion.request.get_json())  # noqa: E501
    films.append(body)
    return body


def delete_film_by_id(film_id):  # noqa: E501
    for i in range(len(films)):
      if films[i].film_id == film_id:
        films.pop(i)
        return films





def get_all_films():  # noqa: E501

    return films


def get_film_by_id(film_id):  # noqa: E501
    for film in films:
     if film.film_id == film_id:
         return film





def update_film(body, film_id):  # noqa: E501
    if connexion.request.is_json:
        body = Film.from_dict(connexion.request.get_json())  # noqa: E501
        for i in range(len(films)):
            if films[i].film_id == film_id:
                films[i].film_id = body.film_id
                films[i].genre = body.genre
                films[i].name = body.name
                films[i].year_of_creation = body.year_of_creation
                return "Фильм изменен"





