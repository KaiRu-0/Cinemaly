# Cinemaly
Cinimaly is a movie recommendation system that suggests movies based on the user's favorite movie. It uses a combination of genres, keywords, tagline, cast, and director information to find and recommend similar movies.


Features: 
1) Load and preprocess movie data.
2) Combine relevant features into a single string for each movie.
3) Convert text data into feature vectors using TF-IDF Vectorizer.
4) Calculate similarity scores using cosine similarity.
5) Recommend movies based on user input.


Installation: 
To get started with Cinimaly, you need to have Python and pip installed. Then, install the necessary dependencies:
pip install numpy pandas scikit-learn

KaiRu's Notes:
This is my first "formal" program, and it serves as a trial run. I didn't use a machine learning model because I don't have enough data to train the model. Instead, I used the cosine similarity algorithm.
