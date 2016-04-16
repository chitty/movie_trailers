# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     7.9,
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

blow = media.Movie("Blow",
                   "A biographical crime film about  George Jung, a drug lord"
                   " responsible for bringing most of the cocaine to the "
                   "United States in the 80s.",
                   7.6,
                   "https://upload.wikimedia.org/wikipedia/en/b/bf/Blow_poster.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=q8lGHQn_n9Y")

city_of_god = media.Movie("Cidade de Deus",
                          "Organized crime rises in a Rio de Janeiro's slum.",
                          8.7,
                          "https://upload.wikimedia.org/wikipedia/pt/1/10/CidadedeDeus.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=ioUE_5wpg_E")

frozen = media.Movie("Frozen",
                     "A story about love between sisters.",
                     7.6,
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_(2013_film)_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

life_is_beautiful = media.Movie("La vita è bella",
                                "A father turns the harsh reality of war into "
                                "a simple game for his son.",
                                8.6,
                                "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=3Y_p7KmAiLM")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors.",
                                7.7,
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

motorcycle_diaries = media.Movie("Diarios de Motocicleta",
                                 "A motorcycle journey in South America made "
                                 "by Che Guevara.",
                                 7.8,
                                 "https://upload.wikimedia.org/wikipedia/en/9/9b/The_Motorcycle_Diaries.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=u6jz_b80V5g")

nine_queens = media.Movie("Nueve Reinas",
                          "Two guys join forces to do a huge scam.",
                          7.9,
                          "https://upload.wikimedia.org/wikipedia/en/d/db/9reinasposter.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=M9Les56e22c")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        8.3,
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

movies = [avatar, blow, city_of_god, motorcycle_diaries, frozen,
          life_is_beautiful, midnight_in_paris, nine_queens, toy_story]

fresh_tomatoes.open_movies_page(movies)
