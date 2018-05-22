#!/usr/bin/env python
import webbrowser


class Movie():
    '''class Movie():
attributes:
    movie_title=It describes the title of the movie.
    movie_storyline=It summarises the story of the movie in one line.
    poster_image=This is the poster of the respective movie.
    trailer_youtube=This is the trailer of the repective movie
'''
    VALID_RATINGS = ["EXCELLENT", "GOOD", "BAD", "AVERAGE"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
