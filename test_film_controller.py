# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.film import Film  # noqa: E501
from swagger_server.models.films import Films  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFilmController(BaseTestCase):
    """FilmController integration test stubs"""

    def test_create_film(self):
        """Test case for create_film

        Метод создания фильма
        """
        body = Film()
        response = self.client.open(
            '/api/v1//films',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_detele_film_by_id(self):
        """Test case for detele_film_by_id

        Метод удаления фильма
        """
        response = self.client.open(
            '/api/v1//films/{film_id}'.format(film_id='film_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_films(self):
        """Test case for get_all_films

        Метод получения списка фильмов
        """
        response = self.client.open(
            '/api/v1//films',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_film_by_id(self):
        """Test case for get_film_by_id

        Метод получения фильма по id
        """
        response = self.client.open(
            '/api/v1//films/{film_id}'.format(film_id='film_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_film(self):
        """Test case for update_film

        Метод обновления списка фильмов
        """
        body = Film()
        response = self.client.open(
            '/api/v1//films/{film_id}'.format(film_id='film_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
