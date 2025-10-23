import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import load_model

model = load_model('simpleRNN_imdb.h5')

imdb_index = imdb.get_word_index()

voc_size = 10000

def preprocessing(review):
    splitted_review = review.lower().split()
    indexed_values = [imdb_index.get(word, 2) +3 for word in splitted_review]
    indexed_values = [index if index < voc_size else 2 for index in indexed_values]
    padded_review = sequence.pad_sequences([indexed_values], maxlen=500)
    return padded_review

def predict_sentiment(review):
    padded_review = preprocessing(review)    
    predicted_review = model.predict(padded_review)
    predicted_value = predicted_review[0][0]
    sentiment = 'Positive' if predicted_value > 0.5 else 'Negative'
    return sentiment, predicted_value 

import streamlit as st
## streamlit app
# Streamlit app
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative.')

# User input
user_input = st.text_area('Movie Review')

if st.button('Classify'):
    sentiment, predicted_value = predict_sentiment(user_input)
    # Display the result
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {predicted_value}')
else:
    st.write('Please enter a movie review.')