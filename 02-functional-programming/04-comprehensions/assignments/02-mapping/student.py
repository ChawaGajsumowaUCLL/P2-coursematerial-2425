
#returns the movie titles.
def titles(movies):
    return [movie.title for movie in movies]

#returns the movie titles and their year, grouped in pairs: [(title1, year1), (title2, year2), ...]
def titles_and_years(movies):
    return [(movie.title, movie.year) for movie in movies]

#returns the movie titles paired up with the number of actors
def titles_and_actor_counts(movies):
    return [(movie.title, len(movie.actors)) for movie in movies]

#must reverse each word in the given string sentence. Words are separated by one space.
def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split(" "))

print(reverse_words("Hello world"))