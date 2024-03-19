# Book Recommendation System
This project implements a book recommendation system using collaborative filtering techniquest o suggest books to users based on their preferences and interactions.

## Data
The dataset for this project has been sourced from Kaggle: Book Recommendation Dataset. It consists of three main datasets: books, ratings, and users.

## Features
- Popularity-based recommendation engine: Considers only books with at least 250 ratings and users who have given at least 50 ratings for building the recommendation system.
- Collaborative filtering recommendation system: Implements a user-item matrix and computes similarity scores between items (books) based on user ratings.
- Web application: Utilizes Streamlit to build a web interface for users to explore popular books and receive personalized recommendations.

## Usage
To use the recommendation system:

- Install the required dependencies using pip install -r requirements.txt.
- Run the Streamlit web application using the command streamlit run book_recommender_system.py.
- Explore popular books and receive personalized recommendations by entering a book name.
