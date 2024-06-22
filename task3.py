import pandas as pd
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

# Step 1: Load the data
# For simplicity, we will use the built-in Movielens dataset
data = Dataset.load_builtin('ml-100k')

# Step 2: Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.25, random_state=42)

# Step 3: Use a collaborative filtering algorithm
# We'll use the KNNBasic algorithm for user-based collaborative filtering
algo = KNNBasic(sim_options={'user_based': True})

# Step 4: Train the algorithm on the trainset
algo.fit(trainset)

# Step 5: Make predictions on the testset
predictions = algo.test(testset)

# Step 6: Evaluate the algorithm
accuracy.rmse(predictions)

# Step 7: Generate recommendations for a specific user
# Choose a user ID
user_id = str(196)

# Get a list of all movie IDs
all_movie_ids = set([i for i in range(1, 1683)])  # Movie IDs in the Movielens 100k dataset range from 1 to 1682

# Get the list of movie IDs the user has already rated
rated_movie_ids = set([rating.iid for rating in trainset.ur[trainset.to_inner_uid(user_id)]])

# Get the list of movie IDs the user has not rated
unrated_movie_ids = all_movie_ids - rated_movie_ids

# Predict ratings for the unrated movies
predictions = [algo.predict(user_id, str(movie_id)) for movie_id in unrated_movie_ids]

# Get the top 10 recommendations
top_10_recommendations = sorted(predictions, key=lambda x: x.est, reverse=True)[:10]

# Print the recommended movie IDs
print("Top 10 movie recommendations for user", user_id, ":")
for recommendation in top_10_recommendations:
    print(recommendation.iid, "with predicted rating", recommendation.est)
