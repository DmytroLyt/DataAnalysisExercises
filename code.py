# Importing pandas and matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Subset column of interest : "title", "country", "genre", "release_year", "duration"
netflix_movies = netflix_subset[
    ["title", "country", "genre", "release_year", "duration"]
]

# Filter and find the movies that shorter than 60 minutes
short_movies = netflix_movies[netflix_movies["duration"] < 60]

# Define an empty list
colors = []

# Iterate over rows of netflix_movies
for lab, row in netflix_movies.iterrows():
    if row["genre"] == "Documentaries":
        colors.append("green")
    elif row["genre"] == "Children":
        colors.append("yellow")
    elif row["genre"] == "Stand-Up":
        colors.append("blue")
    else:
        colors.append("red")

# Inspect first 10 values in the list
colors[:10]

# Create a matplotlib figure
fig = plt.figure(figsize=(15, 10))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies.duration, netflix_movies.release_year, c=colors)

# Create labels and title

plt.title("Movie Duration by Year of Release")
plt.ylabel("Release year")
plt.xlabel("Duration (min)")

# Show scatter plot
plt.show()
