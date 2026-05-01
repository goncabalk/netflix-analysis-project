import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DATA LOAD
df = pd.read_csv("data/netflix_titles.csv")

# TITLE
st.title("Netflix Content Analysis Dashboard")
st.write("This dashboard explores Netflix movies and TV shows.")

# -------------------
# FILTERS
# -------------------

# TYPE FILTER
content_type = st.selectbox(
    "Choose content type",
    ["All"] + list(df["type"].dropna().unique())
)

if content_type != "All":
    filtered_df = df[df["type"] == content_type]
else:
    filtered_df = df

# COUNTRY FILTER
all_countries = (
    df["country"]
    .dropna()
    .str.split(", ")
    .explode()
    .str.strip()
)

all_countries = sorted(all_countries[all_countries != ""].unique())

country = st.selectbox(
    "Choose country",
    ["All"] + all_countries
)

if country != "All":
    filtered_df = filtered_df[
        filtered_df["country"].str.contains(country, na=False)
    ]

# -------------------
# DATA PREVIEW
# -------------------

st.subheader("Dataset Preview")
st.dataframe(filtered_df.head())

# -------------------
# CONTENT TYPE GRAPH
# -------------------

st.subheader("Content Type Distribution")

type_counts = filtered_df["type"].value_counts()

fig, ax = plt.subplots()
sns.barplot(x=type_counts.index, y=type_counts.values, ax=ax)

ax.set_xlabel("Content Type")
ax.set_ylabel("Count")
ax.set_title("Movies vs TV Shows")

st.pyplot(fig)

# -------------------
# GENRE GRAPH
# -------------------

st.subheader("Top Genres")

genres = filtered_df["listed_in"].str.split(", ").explode()
top_genres = genres.value_counts().head(10)

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_genres.values, y=top_genres.index, ax=ax2)

ax2.set_xlabel("Count")
ax2.set_ylabel("Genre")
ax2.set_title("Top Genres")

st.pyplot(fig2)
st.write("This dashboard explores Netflix movies and TV shows.")
st.subheader("Total Content")

st.metric(label="Total Titles", value=len(filtered_df))
col1, col2 = st.columns(2)

col1.metric("Movies", len(filtered_df[filtered_df["type"] == "Movie"]))
col2.metric("TV Shows", len(filtered_df[filtered_df["type"] == "TV Show"]))
