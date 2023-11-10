import json
import os
from datetime import datetime


class Movie:
    data_folder = 'exercice 4/data'
    json_file = 'movies.json'
    path = os.path.join(data_folder, json_file)

    def __init__(self, title, release_date, description):
        self.title = title.title()
        self.release_date = release_date
        self.description = description
        if not os.path.exists(Movie.path):
            self._create_data_folder()
            self._create_json_file()

        self._add_movie_to_json()

    @classmethod
    def _create_data_folder(cls):
        if not os.path.exists(cls.data_folder):
            os.makedirs(cls.data_folder)

    @classmethod
    def _create_json_file(cls):
        with open(cls.path, 'w') as file:
            json.dump({'movies': []}, file, indent=4)

    def _add_movie_to_json(self):
        movies = self._read_movies_json()
        movies.append({
            'titre': self.title,
            'date_de_sortie': self.release_date,
            'description': self.description
        })
        self._write_movies_json(movies)

    @classmethod
    def movie_exists(cls, title):
        title = title.title()
        movies = cls._read_movies_json()
        return any(movie['titre'] == title for movie in movies)

    @classmethod
    def _read_movies_json(cls):
        with open(cls.path, 'r') as file:
            data = json.load(file)
        return data['movies']

    @classmethod
    def _write_movies_json(cls, movies):
        with open(cls.path, 'w') as file:
            json.dump({'movies': movies}, file, indent=4)

    @classmethod
    def delete_movie(cls, title):
        title = title.title()
        movies = cls._read_movies_json()
        movies = [movie for movie in movies if movie['titre'] != title]
        cls._write_movies_json(movies)
        print("Film supprimé avec succès")

    @classmethod
    def update_movie(cls, title, property_to_update, new_value):
        if not cls.movie_exists(title):
            print("Film non trouvé, entrez un titre valide")
            return False
        title = title.title()
        movies = cls._read_movies_json()
        for movie in movies:
            if movie['titre'] == title:
                movie[property_to_update] = new_value
                cls._write_movies_json(movies)
                print("Le film a été mis à jour avec succès.")
                return True
        return False

    @classmethod
    def print_movie(cls, title):
        title = title.title()
        movies = cls._read_movies_json()
        for movie in movies:
            if movie['titre'] == title:
                print(json.dumps(movie, indent=4))

        else:
            print("Film introuvable")

    @classmethod
    def print_all_movies(cls):
        movies = cls._read_movies_json()
        sorted_movies = sorted(movies, key=lambda x: datetime.strptime(
            x['date_de_sortie'], '%d/%m/%Y'))
        print(json.dumps(sorted_movies, indent=4))
