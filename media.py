import webbrowser


class Movie(object):
    """Class defines movie structure"""

    def __init__(self, movie_title, movie_storyline, rating, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
