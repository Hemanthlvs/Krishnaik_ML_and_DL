import pandas as pd
import streamlit as st
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import numpy as np
from tensorflow.keras.models import load_model
import pickle

lstm_model = load_model('LSTM_model.h5')

with open('Tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

def pre_processing(tokenizer, line, max_sequence_length):
    sequence = tokenizer.texts_to_sequences([line])[0]
    if len(sequence) >= max_sequence_length:
        sequence = sequence[-(max_sequence_length):]  # Ensure the sequence length matches max_sequence_len-1
    padded_sequence = np.array(pad_sequences([sequence], maxlen=max_sequence_length, padding='pre'))

    return padded_sequence

def predict_model(model, pre_processing_result, ):
    predicted = model.predict(pre_processing_result, verbose = 0)
    max_predicted_class = np.argmax(predicted, axis = 1)
    for word, index in tokenizer.word_index.items():
        if index == max_predicted_class:
            return word
    return None

# streamlit app
st.title("Next Word Prediction With LSTM And Early Stopping")
input_text=st.text_input("Enter the sequence of Words","To be or not to")
if st.button("Predict Next Word"):
    max_sequence_len=lstm_model.input_shape[1]
    pre_processing_result = pre_processing(tokenizer, input_text, max_sequence_len)
    predicted_word = predict_model(lstm_model, pre_processing_result)
    st.write(f'Next word: {predicted_word}')


    