import streamlit as st
import pandas as pd
import pickle
import sklearn
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


df = pd.read_csv('final_df.csv')
model = pickle.load(open('model.pkl', 'rb'))

st.title('IPL Win Predictor')

#input fields
batting_team = st.selectbox("Select Batting Team",sorted(df['batting_team'].unique()))
bowling_team = st.selectbox("Select Bowling Team",sorted(df['bowling_team'].unique()))
city = st.selectbox("Select Host City",sorted(df['city'].unique()))
target = st.number_input("Enter Target ",min_value=00,max_value=400)
score = st.number_input("Enter Score",min_value=00,max_value=400)
wickets_left = st.number_input("Enter Wickets Left",min_value=0,max_value=10)
overs = st.number_input("Overs completed ",min_value=0,max_value=20,step=1)




# derived features
if st.button('Predict'):
    runs_left = target - score
    balls_left = 120 - (overs) * 6
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city], 'runs_left': [runs_left],
         'balls_left': [balls_left], 'wickets': [wickets_left], 'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]})

    result = model.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.markdown(f"##### 🟢 {batting_team} Win Probability: **{win * 100:.2f}%**")
    st.markdown(f"##### 🔴 {bowling_team} Win Probability: **{loss * 100:.2f}%**")
