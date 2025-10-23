import streamlit as st
import pandas as pd
import numpy as np


print('Hello')

st.title("Hello ................!!!!")
st.title("This is my baby's world")

data = {
'Name' : ['Hemanth', 'Bhavana', 'LRP', 'Bhudevi','Harshini', 'Anirudh', 'Padmavathi', 'Raja Shekar'],
'Age' : [30,29,54,50,27,29,52,52],
'Designation' : ['Data Engineer', 'Dentist', 'Family God', 'House wife','QnA', 'Cloud engineer', 'Lic Manager', 'HOD of School'],
'Relation' : ['Father', 'Mother', 'Paternal Grandfather', 'Paternal GrandMother','Atha', 'Mama', 'Maternal Grandmother', 'Maternal Grandfather']
}

df = pd.DataFrame(data)
st.write("!..................Family Members..................!")
st.write(df)


options = df["Name"].tolist()
relationship_check = st.selectbox("Baby relatives and their relation with them ", options)

def relation_ship(relationship_check):
    relation = df.loc[df["Name"] == relationship_check, "Relation"]
    return relation.iloc[0]

st.write("Relation to this person is : ", relation_ship(relationship_check))

slider_age = st.slider("select the age : " ,0,100)
st.write(f"you have selected the age as : {slider_age}")

def future_plans(slider_age):
    if slider_age == 0 :
        return None

    if slider_age > 0 and slider_age <= 2 :
        st.write(""" ### Infancy (0-2 years) 
- **First smile:** 6-8 weeks 
- **First words:** 12-18 months 
- **First steps:** 9-15 months 
- **Developing motor skills:** Throughout the period """)
    
    if slider_age > 2 and slider_age <= 5 :
        st.write(""" ### Early Childhood (3-5 years) 
- **Potty training:** 2-3 years 
- **Starting preschool:** 3-4 years 
- **Building social skills:** Ongoing 
- **Learning basic letters and numbers:** 4-5 years """)

    if slider_age > 5 and slider_age <= 12 :
        st.write(""" ### Middle Childhood (6-12 years) 
- **Starting primary school:** 5-6 years
- **Reading independently:** 6-8 years 
- **Learning to ride a bicycle:** 6-8 years
- **Joining sports teams or clubs:** 7-10 years
- **Developing hobbies and interests:** Ongoing """)

    if slider_age > 12 and slider_age <= 18 :
        st.write(""" ### Adolescence (13-18 years) 
- **Transition to high school:** 13-14 years 
- **Puberty:** typically 11-14 years
- **First job or internship:** 16-18 years
- **Preparing for college entrance exams:** 16-18 years 
- **Graduating high school:** 17-18 years """)

    if slider_age > 18 and slider_age <= 30 :
        st.write(""" ### Early Adulthood (19-30 years) 
- **Pursuing higher education:** 18-22 years 
- **Starting a career:** 21-25 years 
- **Marriage:** typically 22-30 years 
- **Starting a family:** Varies """) 
        
future_plans(slider_age)

