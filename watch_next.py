import spacy
nlp = spacy.load('en_core_web_md')

# reads in movie file 
def read_movies(file_name):
    movies = []

    file = open(file_name, "r")
    # reads each line
    for line in file:
        split_line = line.split(" :")
        title = split_line[0]
        description = split_line[1].strip()

        # stores movie in dictionary object
        movie = {'title': title, 'description': description}
        movies.append(movie)
    # returns them
    return movies

# returns most similar movie
def get_most_similar_movie(movies, movie_to_compare):
    # defines model sentence
    model_sentence = nlp(movie_to_compare)

    # defines sets these to default values 
    highest_similarity_so_far = 0.0
    most_similar_movie = movies[0]

    for movie in movies:
        
        # gets the movie description and checks its similarity
        sentence = movie['description']
        similarity = nlp(sentence).similarity(model_sentence)

        # if we have a higher similarity then reassign variables to track
        if similarity > highest_similarity_so_far:
            highest_similarity_so_far = similarity
            most_similar_movie = movie
    
    # returns the most similar movie
    return most_similar_movie



# reads data, sets the movie to compare, and returns most similar
movies = read_movies("movies.txt")
movie_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
most_similar_movie = get_most_similar_movie(movies, movie_to_compare)

print()
print(f"Most similar movie: {most_similar_movie['title']}")
print()
