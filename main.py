# Importing the dependencies
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Data Collection and Pre-Processing

# loading the data from the csv file to a pandas dataframe
movies_data = pd.read_csv('movies.csv')

# selecting the relevant features for recommendation
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

# replacing the null values with empty strings
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# combining all the selected features into a single string
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']

# converting the text data to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)


# Cosine Similarity

# getting the similarity scores using cosine similarity
similarity = cosine_similarity(feature_vectors)


# Reccomending Movies

# getting the movie name from the user
movie_name = input('Enter your favourite movie name: ')

# creating a list with all the movie names given in the dataset
list_of_all_titles = movies_data['title'].tolist()

# finding the close match for the movie name given by the user
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

# selecting the closest match
close_match = find_close_match[0]

# finding the index of the movie with title
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

# getting a list of similar movies
similarity_score = list(enumerate(similarity[index_of_the_movie]))

# sorting the movies based on their similarity score
sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

# print the name of similar movies based on the index
print('Movies suggested for you: \n')
i = 1
for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index == index]['title'].values[0]
    if i < 30:
        print(i, '.', title_from_index)
        i += 1