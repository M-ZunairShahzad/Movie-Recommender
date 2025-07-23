# 🎬 Movie Recommender System

A content-based movie recommender system using **tmdb dataset** that suggests similar movies based on a selected title. Built using **Python**, **Streamlit**, and **machine learning** techniques.

---

## 🚀 Features

- Select any movie and get top 5 similar movie recommendations
- Displays official movie posters using **TMDB API**
- Clean, simple, and interactive user interface
- Fast, real-time recommendation system

---

## 🧠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Machine Learning:** CountVectorizer, Cosine Similarity
- **Data:** TMDB dataset (CSV files), Pickle files for performance
- **API:** [TMDB API](https://www.themoviedb.org/documentation/api)

---


## 🔄 Project Workflow

1. **Dataset Loading**

   - Used a TMDB-based dataset with 500 movies and metadata.
2. **EDA & Preprocessing**

   - Selected key columns: `title`, `overview`, `genres`, etc.
   - Combined features into a single `tags` column and cleaned the text.
   - [tmdb_movies.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) + [tmdb_credits.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

   | budget | genres | homepage | id | keywords | orignal_language | orignal_title | overview | popularity | production_companies | production_countries | release_date | revenue | runtime | spoken_languages | status | tagline | title | vote_average | vote_count | movie_id | cast | crew |
   | ------ | ------ | -------- | -- | -------- | ---------------- | ------------- | -------- | ---------- | -------------------- | -------------------- | ------------ | ------- | ------- | ---------------- | ------ | ------- | ----- | ------------ | ---------- | -------- | ---- | ---- |


   * Useful columns

   | movie_id | title | genres | keywords | overview | cast | crew |
   | -------- | ----- | ------ | -------- | -------- | ---- | ---- |

   * Final datatset

   | movie_id | title | tags |
   | -------- | ----- | ---- |
3. **Text Normalization (NLP)**

- Applied stemming using NLTK's `PorterStemmer` to reduce words to root forms.

4. **Text Vectorization**

   - Used **CountVectorizer** (` Bag of Words model`) to convert text into vectors.
   - Computed `cosine similarity` to find similar movies.
5. **Model Saving**

   - Saved processed data (`movies.pkl`) and similarity matrix (`similarity.pkl`) using `pickle`.
6. **App Development**

   - Built UI with **Streamlit**: dropdown for movie selection, real-time poster display.
7. **Poster Integration (TMDB API)**

   - Fetched poster images using `GET` requests with movie IDs.
8. **Deployment**

   - Deployed on **Streamlit Cloud** and shared link in LinkedIn.

---

## 🔑 Some files are very large, so i paste their link below:

**Simlarity.pkl**: https://drive.google.com/file/d/1jfskohammBG12aYsWTToY7uxmL6EOKiz/view?usp=sharing
**tmdb_movies.csv**: https://drive.google.com/file/d/1KJMrvS_sO1wl3zeIEK9gCGcHiBeQDNHw/view?usp=sharing
**tmdb_credits.csv**: https://drive.google.com/file/d/1GEC_JopZc2mlYs7IPDREmxcgVPZDn1eE/view?usp=sharing

---

## 🔑 TMDB API Key

This project uses the following TMDB API key to fetch movie posters:

**API Key:** [8265bd1679663a7ea12ac168da84d2e8]()

**Get request** using movie id to detch posters

https://api.themoviedb.org/3/movie/{movie_id}?api_key=Api Key
