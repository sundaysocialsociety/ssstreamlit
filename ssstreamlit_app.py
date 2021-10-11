import pandas as pd
import numpy as np
import streamlit as st

st.title('SSSupremacy Rankings')

test_rankings = pd.DataFrame(columns={'#','Team','SSSupremacy','Elo','FP ROS','Points'})

test_rankings = test_rankings.append({
    '#': 1,
    'Team': 'Chicago Gunslingers',
    'SSSupremacy': 95,
    'Elo': 1400,
    'FP ROS': '5th',
    'Points': 750}, ignore_index=True)

test_rankings = test_rankings.append({
    '#': 2,
    'Team': "Schrodinger's Cat",
    'SSSupremacy': 93,
    'Elo': 1145,
    'FP ROS': '1st',
    'Points': 680}, ignore_index=True)

test_rankings = test_rankings.append({
    '#': 3,
    'Team': 'Dead Pigeon',
    'SSSupremacy': 88,
    'Elo': 1280,
    'FP ROS': '2nd',
    'Points': 650}, ignore_index=True)


test_rankings

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['GUNS', 'CHOD', 'DEAD'])
st.line_chart(chart_data)

#option = st.sidebar.selectbox(
#    'Which number do you like best?',
#     test_roster['player'])

#'You selected:', option
