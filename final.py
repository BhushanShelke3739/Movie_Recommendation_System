# importing necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time
from scipy.sparse import csr_matrix
import random
 

    
movies = pd.read_csv("./joined4.csv")
movies = movies.drop('Unnamed: 0', axis=1)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Load Animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)


st.markdown("""
<h1 style='text-align: center; 
            color: #00A8E1;
            background-color: rgba(255, 255, 255, 0.9); 
            padding: 10px 20px; 
            border-radius: 5px'>
    Movie Recommendation based on plot
</h1>
""", unsafe_allow_html=True)


# Search bar with autocomplete suggestions


movies = movies[movies['year'] > 2007]



#movies = movies.loc[:16000]

search_query = st.text_input(label="Search for a movie", value="", key="search")

# Filtering suggestions based on the entered search query

suggestions = movies['title'].str.contains(search_query, case=False, na=False)
default_option = None

# Display autocomplete suggestions

autocomplete_suggestions = movies.loc[suggestions, 'title'].tolist()
selected_suggestion = st.selectbox("Select a Movie:", [default_option] + autocomplete_suggestions)

# Show the selected movie
if selected_suggestion:
    st.write(f"You selected: {selected_suggestion}")
    row_index = movies[movies['title'] == selected_suggestion].index[0]
    
    
with st.spinner('Wait for it...'):
    time.sleep(1)
    

# Center the button using HTML and CSS
st.markdown(
    """
    <style>
        div.stButton > button {
            display: block;
            margin: 0 auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the centered button
if st.button("Recommend"):
    st.write("Button clicked!")
    try:
    
        
        # Instantiate and fit TfidfVectorizer 
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(movies['overview'])
    
        #cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix) 
        tfidf_matrix_sparse = csr_matrix(tfidf_matrix)
        cosine_sim = cosine_similarity(tfidf_matrix_sparse, tfidf_matrix_sparse)
        
        # Create a mapping of movie titles to indices
        indices = pd.Series(movies.index, index=movies['title'])

    

        def get_recommendations(title, cosine_sim=cosine_sim):
            
            # Get index of movie
            idx = indices[title]

            # Get pairwise similarity scores  
            sim_scores = list(enumerate(cosine_sim[idx]))

            # Sort movies by similarity
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Return top 10 most similar movies
            return sim_scores[1:11]

        # Get recommendations for a movie  
        ans = get_recommendations(selected_suggestion)

        
            
        table_data = []  
        # Display the movie names using Streamlit Markdown
        st.markdown("#  Recommended Movies")

        for i, j in ans:
            movie_title = movies['title'][i]
            table_data.append({'Movie Title': movie_title})
            
            



# Display the table using Streamlit
        st.table(table_data)
        
        # Creating buttons linked to streaming platforms
        col1, col2, col3, col4 = st.columns(4)

           
        amazon_prime_link = "https://www.amazon.com/Amazon-Video"
        netflix_link = "https://www.netflix.com/"
        hulu_link = "https://www.hulu.com/"
        disney_plus_link = "https://www.disneyplus.com/"

        
        amazon_prime_color = "#00A8E1"  # Amazon Prime color
        netflix_color = "#E50914"  # Netflix color
        hulu_color = "#1CE783"  # Hulu color
        disney_plus_color = "#1F1F1F"  # Disney+ color

        with col1:
            m =  st.markdown(f'<a href="{amazon_prime_link}" style="color: white; text-decoration: none; background-color: #00A8E1; padding: 20px; display: inline-block; border-radius: 5px;">Prime Video</a>', unsafe_allow_html=True)

        with col2:
            m = st.markdown(f'<a href="{netflix_link}" style="color: white; text-decoration: none; background-color: {netflix_color}; padding: 20px; display: inline-block; border-radius: 5px;">Netflix</a>', unsafe_allow_html=True)

        with col3:
            m =   st.markdown(f'<a href="{hulu_link}" style="color: white; text-decoration: none; background-color: {hulu_color}; padding: 20px; display: inline-block; border-radius: 5px;">Hulu</a>', unsafe_allow_html=True)
            
        with col4:
            m = st.markdown(f'<a href="{disney_plus_link}" style="color: white; text-decoration: none; background-color: {disney_plus_color}; padding: 20px; display: inline-block; border-radius: 5px;">Disney Plus</a>', unsafe_allow_html=True)
            
    except (KeyError, MemoryError) as e:
        st.error(f"An error occurred: {e}. We are really sorry, we're working on expanding our database.")




if st.button("Generate Random Recommendations"):
    st.write("## Random recommendations")
    for i in range(10):
        num = random.randint(0, len(movies)-1)
        st.write(f"##### {movies['title'][num]}") 
        st.write(f"{movies['overview'][num]}")
   
    
    col1, col2, col3, col4 = st.columns(4)

       
    amazon_prime_link = "https://www.amazon.com/Amazon-Video"
    netflix_link = "https://www.netflix.com/"
    hulu_link = "https://www.hulu.com/"
    disney_plus_link = "https://www.disneyplus.com/"

    
    amazon_prime_color = "#00A8E1"  # Amazon Prime color
    netflix_color = "#E50914"  # Netflix color
    hulu_color = "#1CE783"  # Hulu color
    disney_plus_color = "#1F1F1F"  # Disney+ color

    with col1:
          m =  st.markdown(f'<a href="{amazon_prime_link}" style="color: white; text-decoration: none; background-color: #00A8E1; padding: 20px; display: inline-block; border-radius: 5px;">Prime Video</a>', unsafe_allow_html=True)

    with col2:
          m = st.markdown(f'<a href="{netflix_link}" style="color: white; text-decoration: none; background-color: {netflix_color}; padding: 20px; display: inline-block; border-radius: 5px;">Netflix</a>', unsafe_allow_html=True)

    with col3:
         m =   st.markdown(f'<a href="{hulu_link}" style="color: white; text-decoration: none; background-color: {hulu_color}; padding: 20px; display: inline-block; border-radius: 5px;">Hulu</a>', unsafe_allow_html=True)
         
    with col4:
        m = st.markdown(f'<a href="{disney_plus_link}" style="color: white; text-decoration: none; background-color: {disney_plus_color}; padding: 20px; display: inline-block; border-radius: 5px;">Disney Plus</a>', unsafe_allow_html=True)
