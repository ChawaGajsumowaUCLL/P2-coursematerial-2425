def movie_count(movies, director):
    return len([movie for movie in movies if movie.director == director]) 

def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])

def has_director_made_genre(movies, director, genre):
    return any([movie.director == director and genre in movie.genres for movie in movies])

def is_prime(n):
    return n> 1 and all([n%i!=0 for i in range(2,n)])

def is_increasing(ns):
    return all([ns[i] >= ns[i-1] for i in range(1, len(ns))])

def count_matching(xs, ys):
    return len([1 for x,y in zip(xs, ys) if x == y])

def weighted_sum(ns, weights):
    return sum([n*weight for n, weight in zip(ns, weights)])

def alternating_caps(string):
    return ''.join([string[i].upper() if i%2 == 0 else string[i].lower() for i in range(len(string)) ])

def find_repeated_words(sentence):
    words = [letter.strip(".,?! ").lower() for letter in sentence.split()]
    return {words[i] for i in range(1, len(words)) if words[i] == words[i-1]}

