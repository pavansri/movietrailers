#!/usr/bin/env python
import media
import fresh_tomatoes
'''We are importing things from fresh_tomatoes.py file.
The import fresh_tomatoes can do this.
'''


Ironman2 = media.Movie("Ironman-2", "Action packed movie",
                       "https://bit.ly/2KGr1EB",
                       "https://www.youtube.com/watch?v=BoohRoVA9WQ")
Avengers = media.Movie("Avengers", "Super heros together saving the world",
                       "https://bit.ly/2kb1UOJ",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
Civilwar = media.Movie("Civil war", "Friendship turned to war",
                       "https://bit.ly/2GB4vKH",
                       "https://www.youtube.com/watch?v=dKrVegVI0Us")
Thor = media.Movie("Thor", "Fantasy", "https://bit.ly/2wVfGys",
                   "https://www.youtube.com/watch?v=ue80QwXMRHg")

movies = [Ironman2, Avengers, Civilwar, Thor]
fresh_tomatoes.open_movies_page(movies)
