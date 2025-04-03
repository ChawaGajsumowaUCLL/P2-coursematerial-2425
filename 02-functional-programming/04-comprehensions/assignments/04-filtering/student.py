#returns the titles of movies from the given year
def movies_from_year(movies, year):
    return [movie.title for movie in movies if movie.year == year]

#returns the titles of movies that have actor in it
def movies_with_actor(movies, actor):
    return [movie.title for movie in movies if actor in movie.actors]

#returns the divisors of n in increasing order. For example, divisors(12) should return [1, 2, 3, 4, 6, 12]
def divisors(n):
    return [divisor for divisor in range(1,n + 1) if n%divisor == 0]