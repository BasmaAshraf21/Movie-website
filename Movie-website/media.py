import webbrowser

#create class Movie
class Movie():
    """This class provides a way to store movie related information"""

    
    VALID_RATINGS = ["G" , "PG" , "PG-13" , "R"]
    #create instructor to the class
    def __init__(self,movie_title,movie_storyline,postoer_image,trailer_youtbe):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = postoer_image
        self.trailer_youtube_url =trailer_youtbe
        
#create function show trailer to open trailer of movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
