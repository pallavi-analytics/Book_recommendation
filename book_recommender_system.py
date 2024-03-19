import streamlit as st
import pickle
import numpy as np

# Load pickled data
popular_books_df = pickle.load(open('popular_books_df.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books_df = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))

# Define Streamlit UI
def main():
    st.title("Book Recommendation System")

    # Render homepage
    st.header("Popular Books")
    st.write(popular_books_df)

    # Render recommendation form
    st.header("Recommend Books")
    book_name = st.text_input("Enter a book name:")
    if st.button("Get Recommendations"):
        index = np.where(pt.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

        # Display recommended books individually

        st.subheader("Recommended Books:")
        for i, rec in enumerate(similar_items):
            rec_index = rec[0]
            book_title = books_df.iloc[rec_index]['Book-Title']
            book_author = books_df.iloc[rec_index]['Book-Author']
            
            # Choose the small-sized image URL
            image_url = books_df.iloc[rec_index]['Image-URL-S']
            
            st.write(f"{i + 1}: {book_title} by {book_author}")
            st.image(image_url, caption=book_title, width=80)  # Adjust image width here

if __name__ == "__main__":
    main()
