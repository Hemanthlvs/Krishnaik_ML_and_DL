import streamlit as st
import pandas as pd
import tensorflow as tf
import pickle

# loading model.h5, scaler.pkl, labelencoder.pkl, ohe.pkl

model = tf.keras.models.load_model('model.h5')

with open('LabelEncoder_gender.pkl', 'rb') as file:
    LabelEncoder_gender = pickle.load(file)

with open('OHE_geography.pkl', 'rb') as file:
    OHE_geography = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)



# Title
st.title("Customer churn prediction")

# input values to provide
CreditScore = st.number_input('Credit Score')
Geography = st.selectbox('Geography', OHE_geography.categories_[0])
Gender = st.selectbox('Gender', LabelEncoder_gender.classes_)
Age = st.slider('Age', 1, 100)
Tenure = st.slider('Tenure', 1, 10)
Balance = st.number_input('Balance')
Num_Of_Products = st.slider('NumOfProducts', 1, 4)
HasCrCard = st.selectbox('Has_credit_card', [0,1])
Is_Active_member = st.selectbox('Is_Active_member', [0,1])
EstimatedSalary = st.number_input('Estimated_salary')

#prepare the input data
new_data = pd.DataFrame({
                        'CreditScore' : [CreditScore],
                        'Geography' : [Geography],
                        'Gender' : [Gender],
                        'Age' : [Age],
                        'Tenure' : [Tenure],
                        'Balance' : [Balance],
                        'NumOfProducts' : [Num_Of_Products],
                        'HasCrCard' : [HasCrCard],
                        'IsActiveMember' : [Is_Active_member],
                        'EstimatedSalary' : [EstimatedSalary]
                    })

#label encoding Gender
new_data['Gender'] = LabelEncoder_gender.transform(new_data['Gender'])

#OHE Geography
OHE_geo = OHE_geography.transform(new_data[['Geography']]).toarray()
OHE_Geo_df = pd.DataFrame(OHE_geo, columns= OHE_geography.get_feature_names_out(['Geography']))

#concatinating all columns
pred_data  = pd.concat([new_data.drop('Geography', axis=1),OHE_Geo_df], axis=1)

#scaling the data
scaled_data = scaler.transform(pred_data)

#Predicting the data
pred = model.predict(scaled_data)
predicted_value = pred[0][0]

st.write(f'Churn probablity : {predicted_value:.2f}')

if predicted_value > 0.5:
    st.write("The customer is likely to churn")
else:
    st.write("The customer is not likely to churn")