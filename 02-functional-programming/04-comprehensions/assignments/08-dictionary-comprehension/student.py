#returns a dict whose keys are movie titles and values are the corresponding director
def title_to_director(movies):
    return {movie.title : movie.director for movie in movies}
#returns a dict where keys are directors and values are lists of movie titles by that director. 
def director_to_titles(movies):
    return {director : [movie.title for movie in movies if movie.director == director] for director in {movie.director for movie in movies}}
