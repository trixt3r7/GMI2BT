import textwrap
from gui import movie_info_header, hr_header


class Movie:
    def __init__(self, movie):
        self.title = movie['Title']
        self.year = movie['Year']
        self.rated = movie['Rated']
        self.runtime = movie['Runtime']
        self.genre = movie['Genre']
        self.released = movie['Released']
        self.director = movie['Director']
        self.writer = movie['Writer']
        self.actors = movie['Actors']
        self.plot = movie['Plot']
        self.country = movie['Country']
        self.language = movie['Language']
        self.poster = movie['Poster']
        self.rating_imdb = movie['imdbRating']
        self.rating_metascore = movie['Metascore']
        self.imdbID = movie['imdbID']
        self.type = movie['Type']

    def movie_details(self):
        movie_info_header()
        print(f"TITLE: {self.title}")
        print(f"{self.runtime} | {self.released} | {self.rated}")
        print(f"GENRE: {self.genre}")
        print(f"DIRECTOR: {self.director}")
        writers = textwrap.wrap(f"WRITERS: {self.writer}", 61)
        for line in writers:
            print(line)
        actors = textwrap.wrap(f"ACTORS: {self.actors}", 61)
        for line in actors:
            print(line)

        print(f"\nRATINGS:\nIMDB: {self.rating_imdb}/10\nMetacritics: {self.rating_metascore}/100")

        print("\nSTORYLINE:")
        storyline = textwrap.wrap(f"{self.plot}", 61)
        for line in storyline:
            print(line)
        hr_header()
