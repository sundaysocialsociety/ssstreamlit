import pandas as pd
import numpy as np
import streamlit as st
#import plotly.graph_objects as go

st.title('SSSupremacy Rankings: Week 5')

test_rankings = pd.DataFrame(columns={'Rank', 'Points','Team','SSSupremacy','SSS Wins','FP ROS Rank'})

test_rankings = test_rankings.append({
    'Rank': 8,
    'Team': 'AI Takeover',
    'SSSupremacy': 76.1,
    'SSS Wins': 22,
    'FP ROS Rank': 5,
    'Points': 597}, ignore_index=True)

test_rankings = test_rankings.append({
    'Rank': 5,
    'Team': 'Revenge of the Sea hags',
    'SSSupremacy': 78.6,
    'SSS Wins': 36,
    'FP ROS Rank': 7,
    'Points': 670}, ignore_index=True)

test_rankings = test_rankings.append({
    'Rank': 1,
    'Team': "Schrodinger's Cat",
    'SSSupremacy': 84.6,
    'SSS Wins': 44,
    'FP ROS Rank': 1,
    'Points': 752}, ignore_index=True)

test_rankings = test_rankings.append({
    'Rank': 7,
    'Team': 'ICARUS: Reign of Chaos',
    'SSSupremacy': 77.7,
    'SSS Wins': 30,
    'FP ROS Rank': 7,
    'Points': 669}, ignore_index=True)

test_rankings = test_rankings.append({
    'Rank': 2,
    'Team': 'Chicago Gunslingers',
    'SSSupremacy': 83.2,
    'SSS Wins': 48,
    'FP ROS Rank': 4,
    'Points': 787}, ignore_index=True)

test_rankings = test_rankings.append({
    'Rank': 3,
    'Team': 'Boston Clamjammers',
    'SSSupremacy': 81.7,
    'SSS Wins': 36,
    'FP ROS Rank': 2,
    'Points': 671}, ignore_index=True)

test_rankings = test_rankings.append({
    'Rank': 12,
    'Team': 'Fawkes F.F.C.',
    'SSSupremacy': 65.6,
    'SSS Wins': 8,
    'FP ROS Rank': 12,
    'Points': 478}, ignore_index=True)

test_rankings = test_rankings.append({
    'Rank': 9,
    'Team': 'Bedwetters',
    'SSSupremacy': 73.1,
    'SSS Wins': 16,
    'FP ROS Rank': 9,
    'Points': 523}, ignore_index=True)

test_rankings = test_rankings.append({
    'Rank': 4,
    'Team': 'Dead Pigeon',
    'SSSupremacy': 80.0,
    'SSS Wins': 32,
    'FP ROS Rank': 3,
    'Points': 652}, ignore_index=True)

test_rankings = test_rankings.append({
    'Rank': 10,
    'Team': 'Cannibals',
    'SSSupremacy': 71.9,
    'SSS Wins': 15,
    'FP ROS Rank': 10,
    'Points': 548}, ignore_index=True)

test_rankings = test_rankings.append({
    'Rank': 11,
    'Team': 'The White Mamba',
    'SSSupremacy': 70.1,
    'SSS Wins': 12,
    'FP ROS Rank': 11,
    'Points': 509}, ignore_index=True)

test_rankings = test_rankings.append({
    'Rank': 6,
    'Team': 'PLOW',
    'SSSupremacy': 78.4,
    'SSS Wins': 31,
    'FP ROS Rank': 6,
    'Points': 627}, ignore_index=True)



test_rankings = test_rankings[['Rank', 'Team','SSSupremacy','Points','SSS Wins','FP ROS Rank']].sort_values('SSSupremacy', ascending=False).reset_index(drop=True)

# convert data to plotly figure
fig = go.Figure(data=[go.Table(
    header=dict(values=list(test_rankings.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[test_rankings['Rank'], test_rankings['Team'], test_rankings['SSSupremacy'], test_rankings['Points'], test_rankings['SSS Wins'], test_rankings['FP ROS Rank']],
               fill_color='lavender',
               align='left'))
])

# figure layout
fig.update_layout(
#    width=1400,
    height=10000
#    margin=dict(
#        l=0,
#        r=0,
#        b=0,
#        t=0
#        )
    )

#st.plotly_chart(fig)
st.dataframe(test_rankings.style.format({"SSSupremacy": "{:.1f}"}), height=1000)
#AgGrid(test_rankings, theme='material', width=1000, height = 1000)



#chart_data = pd.DataFrame(
#    np.random.randn(20, 3),
#    columns=['GUNS', 'CHOD', 'DEAD'])
#st.line_chart(chart_data)

#option = st.sidebar.selectbox(
#    'Which number do you like best?',
#     test_roster['player'])

#'You selected:', option
