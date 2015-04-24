import webbrowser
#create a class with movie parameters:title,director,writer,starring,storyline,poster,youtube trailer.
class Movie():
    def __init__(self, movie_title, movie_director, movie_writer, movie_starring, movie_storyline, poster_image,
               trailer_youtube):
        self.title = movie_title
        self.director = movie_director
        self.writer = movie_writer
        self.starring = movie_starring
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #function to show trailer of the movie object
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
