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