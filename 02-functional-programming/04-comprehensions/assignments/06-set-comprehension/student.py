#collects all directors in a set
def directors(movies):
    return {movie.director for movie in movies}

#should return the set of values that occur both in xs and ys
def common_elements(xs, ys):
    return {value for value in xs if value in ys}