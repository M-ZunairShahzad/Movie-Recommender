import pickle
import streamlit as st
import requests

def poster_fetch(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8'.format(movie_id)) # json string
    data = response.json() # json dictionary
    return "http://image.tmdb.org/t/p/w500" + data['poster_path']
    

# load back
file_name1 = 'movies.pkl'
file_mode = 'rb'
pkl_file1 = open(file_name1, file_mode)
new_movie_df = pickle.load(pkl_file1)
movies_list = new_movie_df['title'].values

file_name2 = 'simlarity.pkl'
pkl_file2 = open(file_name2, file_mode)
simlarity = pickle.load(pkl_file2)

# title 
# st.title('Movie Recommender System')
st.markdown(
    """
    <div style="text-align:center; margin-bottom: 1em;">
        <h1 style="color: #e50914; font-size: 3em; font-weight: bold; margin:0;">🎬 Movie Recommender</h1>
        <p style="font-size:1.2em; font-style: italic; color: #f0f0f0;">Find your next favorite movie</p>
        <div style="width: 200px; height: 4px; background-color: #e50914; margin: 0.5em auto;"></div>
    </div>
    """,
    unsafe_allow_html=True
)


# select box
selected_movie_name = st.selectbox(
    'Choose a movie',
    movies_list
)

# recommender
def recommended(movie_title):
    movie = new_movie_df[new_movie_df['title'] == movie_title] # returns full movie row by title
    movie_idx = movie.index[0]
    enum_obj = enumerate(simlarity[movie_idx])
    best_movies = sorted(list(enum_obj), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    
    for i in best_movies:
        movie_row = new_movie_df.iloc[i[0]] #  returns full movie row by index
        recommended_movies.append(movie_row['title'])
        tmdb_id = movie_row['movie_id']
        recommended_movies_posters.append(poster_fetch(tmdb_id))
        
    return recommended_movies, recommended_movies_posters
        
# button
if st.button('Recommend'):
    top_five_movies_list, posters = recommended(selected_movie_name)
    cols = st.columns(5)  # 5 columns for 5 movies
    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_container_width=True)
            st.caption(top_five_movies_list[i])