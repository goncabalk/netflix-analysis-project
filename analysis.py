# NOTE:
# - Missing country values dropped for country analysis
# - 'listed_in' and 'country' fields exploded for accurate counts
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/netflix_titles.csv")

print(df.head())

print(df["type"].value_counts())

sns.countplot(data=df, x="type")

plt.title("Netflix Content Types")

plt.savefig("images/content_types.png")

plt.show()

year_counts = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(12,5))

sns.lineplot(
    x=year_counts.index,
    y=year_counts.values
)

plt.title("Netflix Content by Release Year")

plt.xlabel("Year")
plt.ylabel("Content Count")

plt.show()
country_counts = df["country"].value_counts().head(10)

print(country_counts)
plt.figure(figsize=(12,6))

sns.barplot(
    x=country_counts.values,
    y=country_counts.index
)

plt.title("Top 10 Countries by Netflix Content")

plt.xlabel("Content Count")
plt.ylabel("Country")

plt.show()
print(df.isnull().sum())
clean_df = df.dropna(subset=["country"])

print(clean_df["country"].isnull().sum()) 
clean_df = df.dropna(subset=["country"])
top_countries = clean_df["country"].value_counts().head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top 10 Countries (Clean Data)")
plt.xlabel("Content Count")
plt.ylabel("Country")

plt.show()
# GENRE ANALYSIS

genres = df["listed_in"].str.split(", ").explode()

top_genres = genres.value_counts().head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_genres.values,
    y=top_genres.index
)

plt.title("Top Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")

plt.savefig("images/top_genres.png")

plt.show()# COUNTRY FIX

countries = df["country"].str.split(", ").explode()

top_countries = countries.value_counts().head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top Countries on Netflix (Fixed)")
plt.xlabel("Count")
plt.ylabel("Country")

plt.savefig("images/top_countries.png")

plt.show()# MOVIE DURATION ANALYSIS

movies = df[df["type"] == "Movie"].copy()

movies["duration"] = movies["duration"].str.replace(" min", "")
movies["duration"] = movies["duration"].astype(float)

plt.figure(figsize=(10,5))

sns.histplot(movies["duration"], bins=30)

plt.title("Movie Duration Distribution")
plt.xlabel("Minutes")
plt.ylabel("Count")

plt.savefig("images/movie_duration.png")

plt.show()
# YEARLY TYPE TREND (Movie vs TV)

year_type = (
    df.groupby(["release_year", "type"])
      .size()
      .reset_index(name="count")
)

plt.figure(figsize=(12,6))
sns.lineplot(data=year_type, x="release_year", y="count", hue="type")

plt.title("Movies vs TV Shows by Year")
plt.xlabel("Year")
plt.ylabel("Count")

plt.savefig("images/year_type_trend.png")
plt.show()# RATING DISTRIBUTION

rating_counts = df["rating"].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=rating_counts.values, y=rating_counts.index)

plt.title("Top Content Ratings")
plt.xlabel("Count")
plt.ylabel("Rating")

plt.savefig("images/ratings.png")
plt.show()
# HEATMAP: TOP COUNTRIES OVER YEARS

countries = df["country"].str.split(", ").explode()
df_exp = df.copy()
df_exp["country"] = countries

top5 = countries.value_counts().head(5).index

heat = (
    df_exp[df_exp["country"].isin(top5)]
    .groupby(["country", "release_year"])
    .size()
    .unstack(fill_value=0)
)

plt.figure(figsize=(12,6))
sns.heatmap(heat, cmap="Blues")

plt.title("Top Countries Content Over Time")

plt.savefig("images/country_heatmap.png")
plt.show()