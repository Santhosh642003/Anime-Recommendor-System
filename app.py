import streamlit as st
import pickle
import pandas as pd

# Load pickled data
cosine_sim_content = pickle.load(open('cosine_sim_content.pkl', 'rb'))
indices = pickle.load(open('indices.pkl', 'rb'))
anime_features = pickle.load(open('anime.pkl', 'rb'))
anime_synopsis = pickle.load(open('anime_synopsis.pkl', 'rb'))
cosine_sim_synopsis = pickle.load(open('cosine_sim_synopsis.pkl', 'rb'))

# Function to get recommendations based on cosine similarity
def get_recommendations(title, cosine_sim, genre_or_synopsis='Genre'):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    anime_indices = [i[0] for i in sim_scores]
    recommendations = anime_features['Name'].iloc[anime_indices]

    if genre_or_synopsis == 'Synopsis':
        recommendations = recommendations.reset_index(drop=True)
        return recommendations

    return recommendations

# Streamlit App
st.title('Anime Recommender Based on Genre')

# Get recommendations based on Genre
selected_anime_genre = st.selectbox('Select an anime for Genre-based recommendations:', anime_features['Name'].values, index=None, placeholder='Enter the Anime')
if st.button('Get Recommendations Based on Genre'):
    recommendations_genre = get_recommendations(selected_anime_genre, cosine_sim_content)
    st.write(f"Top 10 recommendations for {selected_anime_genre} based on Genre:")
    for anime in recommendations_genre:
            st.write(anime)

# Get recommendations based on Synopsis
st.title('Anime Recommender Based on Synopsis')

selected_anime_synopsis = st.selectbox('Select an anime for Synopsis-based recommendations:', anime_features['Name'].values, index=None, placeholder='Enter the Anime')
if st.button('Get Recommendations Based on Synopsis', key='get_recommendations_button'):
    recommendations_synopsis = get_recommendations(selected_anime_synopsis, cosine_sim_synopsis, genre_or_synopsis='Synopsis')
    st.write(f"Top 10 recommendations for {selected_anime_synopsis} based on Synopsis:")
    for anime in recommendations_synopsis:
         
        st.write(anime)
