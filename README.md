# Movie_Recommendation_System
Final Project for INFO I - 501 course
Link to the app -> https://movierecommendationsystem-cs.streamlit.app/

This project is a movie recommendation system based on movie plots. The application is built using the Streamlit framework and leverages natural language processing techniques to recommend movies similar to the user's input.

## Concepts and Technologies Used
1. Streamlit: Streamlit is a Python library that simplifies the process of creating web applications for data science and machine learning.

2. Pandas: Pandas is a powerful data manipulation library for Python. It is used for reading and manipulating the movie dataset.

3. Matplotlib: Matplotlib is a plotting library for Python. It is used for visualizing data, and in this case, for displaying a snowflake animation and generating plots.

4. Scikit-learn (sklearn): Scikit-learn is a machine learning library for Python. The TfidfVectorizer and cosine_similarity functions from the library are employed to process and compare movie plot descriptions.

5. SciPy: The SciPy library is used for sparse matrix representation (csr_matrix) to handle the large dataset efficiently.

6. HTML and CSS: HTML and CSS are used to style and structure the web application. The design includes a snowflake animation, a centered title, and styled buttons.

## Project Overview
1. Loading and Preprocessing Data
The code starts by importing necessary libraries and loading the movie dataset from a CSV file. Unnamed columns are dropped for clarity.

2. User Interface
The Streamlit app begins by using a custom CSS file (style.css) to enhance the visual appeal. The main interface includes a title, a search bar with autocomplete suggestions, and a button for movie recommendations.

3. Autocomplete Search
Users can input a movie title, and autocomplete suggestions are dynamically generated based on the entered text. Suggestions are filtered from the dataset, and the user can select a movie from the dropdown.

4. Movie Recommendations
Upon selecting a movie and clicking the "Recommend" button, the system generates movie recommendations based on the similarity of plot descriptions using TF-IDF and cosine similarity. The top 10 recommended movies are displayed in a table.

5. Streaming Platform Links
For each recommended movie, clickable buttons are provided, linking to popular streaming platforms like Prime Video, Netflix, Hulu, and Disney Plus.

6. Random Recommendations
The "Generate Random Recommendations" button provides random movie recommendations, along with links to streaming platforms.

## Snapshots



## Error Handling
The code includes error handling to manage KeyError and MemoryError exceptions that may occur during recommendation generation.

## Limitations and Future Improvements
- The dataset is limited to the first 16,000 rows for performance reasons.
- The application may encounter MemoryError for larger datasets; optimizations are required.
- The recommendation algorithm can be further improved with advanced techniques.
- Feel free to explore and enhance this movie recommendation system!
