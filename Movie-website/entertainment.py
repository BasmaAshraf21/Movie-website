import media
import fresh_tomatoes

#Information about toy story
toy_story = media.Movie("Toy Story",
                        "A story of a by and his toys that can",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#Information about avatar
avatar = media.Movie("Avatar",
                        "Avatar is a 2009 American science fiction adventure movie",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY&t=2s")

#Information about hunger games
hunger_games = media.Movie("Hunger Games",
                        "This article is about the book series. ",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=mfmrPu43DF8")
#Information about la la land
la_la_land = media.Movie("La la land",
                        "La La Land is a 2016 American musical romantic comedy-drama film",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_SY1000_SX675_AL_.jpg",
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")
#Information about John wick
john_wick = media.Movie("John Wick",
                        " Chapter 1, is a 2014 American neo-noir action thriller film",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwMTM2MTI4MjE@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")
#Information about John wick
the_best_of_me = media.Movie("The Best Of Me",
                        "The Best of Me is a 2014 American romantic drama film ",
                        "https://upload.wikimedia.org/wikipedia/en/6/68/The_Best_of_Me_poster.jpg",
                        "https://www.youtube.com/watch?v=cQszhfoP_WI")


movies = [toy_story, avatar, hunger_games,la_la_land,john_wick,the_best_of_me]
fresh_tomatoes.open_movies_page(movies)
