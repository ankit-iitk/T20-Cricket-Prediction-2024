import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt


pipeline = pickle.load(open('pipeline.pkl','rb'))

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;  /* Dark Green background */
        color: white;  /* White text */
        font-size: 18px;  /* Font size */
        font-weight: bold;  /* Bold text */
        border-radius: 12px;  /* Rounded corners */
        padding: 10px 20px;  /* Padding around text */
        border: none;  /* Remove default border */
        cursor: pointer;  /* Pointer cursor on hover */
        transition: all 0.3s ease;  /* Smooth transition for effects */
    }

    .stButton>button:hover {
        background-color: #45a049;  /* Darker green on hover */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);  /* Shadow effect on hover */
    }

    .stButton>button:active {
        background-color: #3e8e41;  /* Even darker green when clicked */
    }
    </style>
    """, unsafe_allow_html=True
)


batting_team = ['Canada',
 'United States of America',
 'Papua New Guinea',
 'West Indies',
 'Oman',
 'Namibia',
 'Sri Lanka',
 'South Africa',
 'Afghanistan',
 'Uganda',
 'Scotland',
 'Nepal',
 'Netherlands',
 'Ireland',
 'India',
 'Australia',
 'Pakistan',
 'New Zealand',
 'Bangladesh',
 'England']

bowling_team = ['United States of America',
 'Canada',
 'West Indies',
 'Papua New Guinea',
 'Namibia',
 'Oman',
 'South Africa',
 'Sri Lanka',
 'Uganda',
 'Afghanistan',
 'England',
 'Netherlands',
 'Nepal',
 'India',
 'Ireland',
 'Australia',
 'Pakistan',
 'Scotland',
 'New Zealand',
 'Bangladesh']

innings = [1, 2]

city = ['Dallas',
 'Guyana',
 'Barbados',
 'New York',
 'Antigua',
 'Trinidad',
 'St Vincent',
 'St Lucia',
 'Lauderhill']

st.title('T20 World Cup 2024 Prediction 🏏')
st.write('')

st.sidebar.title("T20 Prediction 2024")
st.sidebar.write("")

uploaded_file = st.sidebar.file_uploader("Choose a CSV file",type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    st.write(f"DataFrame has {df.shape[0]} rows and {df.shape[1]} columns.")

innings = st.selectbox('Innings',innings)
st.write('')

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team',sorted(batting_team))

with col2:
    bowling_team = st.selectbox('Select Bowling Team',sorted(bowling_team))

st.write('')

city = st.selectbox('Select City',sorted(city))
st.write('')

col3,col4,col5 = st.columns(3)
with col3:
    current_score = st.number_input('Enter Current Score')

with col4:
    overs_done = st.number_input('Overs Done',min_value=0,max_value=20,step=1)

with col5:
    wickets = st.number_input('Wickets Out',min_value=0,max_value=10,step=1)

st.write('')

last_five = st.number_input('Runs Scored in Last 5 overs')

st.write('')

if st.button('🏏 Predict Score'):
    balls_left = 120 - (overs_done*6)
    wickets_left = 10 - wickets
    current_run_rate = current_score/overs_done

    input_df = pd.DataFrame({'innings':[innings],'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city],'current_score':[current_score],'balls_left':[balls_left],'wicket_left':[wickets_left],'current_run_rate':[current_run_rate],'last_five':[last_five]})
    result = pipeline.predict(input_df)
    st.header(f'Predicted Score - {round(result.tolist()[0],3)}')

st.write('')
st.markdown("""
    <footer style="text-align:center; padding: 10px; background-color: #1e3d59; color: white;">
        Made with ❤️ by  <b> Ankit Saluja </b>
    </footer>
""", unsafe_allow_html=True)
