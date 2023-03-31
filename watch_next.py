watched = """ Planet Hulk: Will he save their world or destroy it? 
When the hulk becomes too dangerous for the Earth, the illuminati trick 
Hulk into a shuttle and launch him into space to a planet where the hulk 
can live in peace. Unfortunately, Hulk land on the planet Sakaar where he 
is sold into slavery and trained as a gladiator “"""

def suggest(mov_description):
    import spacy
    nlp = spacy.load('en_core_web_sm') # en_core_web_md doesn't work on my device
    
    interest = nlp(mov_description)      # Recent movie watched
    movies = []                          # Upload movie txt
    with open("movies.txt", 'r+') as f: 
        for line in f: 
         movies += line.splitlines()

    similar1ty = [] # stored: similarities between interest and other movies
    movie1 = [] # stored: title of movies for index purposes

    for movie in movies: 
        similarity = nlp(movie).similarity(interest)
        similar1ty.append(similarity)
        movie1.append(movie)

    dex = similar1ty.index(max(similar1ty))
    best = movie1[dex]
    print(f"Based on the last movie you watched, we recommend {best[:7]} next!")

suggest(watched)