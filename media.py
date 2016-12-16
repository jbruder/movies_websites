import webbrowser

# Import imdbpy module (see README and http://imdbpy.sourceforge.net/)
import imdb


class Movie():

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            imdb_id):
        # Create imdbpy object to query imdb for movie rating
        imdb_access = imdb.IMDb(accessSystem='http')
        # Pull basic info for movie with identifier in imdb_id
        imdb_movie = imdb_access.get_movie(imdb_id)
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        # Get imdb rating
        self.rating = imdb_movie['rating']

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
