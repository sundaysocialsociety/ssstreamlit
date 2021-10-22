import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from IPython.display import HTML
from jinja2 import Template
#import plotly.graph_objects as go

st.title('SSSupremacy Rankings: Week 6')

components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vT3APEOGU85aTjw_-4tj5DCQRHqPluD3FYSB3MPlxUAbGamibLnCBwlvlP6bPIymybe4HWRq79e4fcz/embed?start=true&loop=true&delayms=60000", width=750, height=650, scrolling=True)

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


columns = ['Rank', 'Team','SSSupremacy','Points','SSS Wins','FP ROS Rank']
test_rankings = test_rankings[columns].sort_values('SSSupremacy', ascending=False).reset_index(drop=True)




#st.dataframe(test_rankings.style.format({"SSSupremacy": "{:.1f}"}), height=1000)

fivethirtyeight_template = """<div class="polls3">
  <table>
    <thead>
      <tr>
        {% for c in cols %}
            <th><div {% if c.lower() in ('grade', 'sample', 'x') %}
                   style="text-align: center"
                 {% endif %}>
          {{c}}</div>
        </th>
        {% endfor %}
      </tr>
    </thead>
    <tbody>
      {% for row in rows %}
      <tr>
        <td class="Rank">{{row['Rank']}}</td>
        <td class="Team">{{row['Team']}}</td>
        <td class="SSSupremacy">{{row['SSSupremacy']}}</td>
        <td class="SSS Wins">{{row['SSS Wins']}}</td>
        <td class="FP ROS Rank">{{row['FP ROS Rank']}}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

<style>

div .polls3 {
    overflow: scroll;
    margin-top: 6px;
}

.polls3 table {
    font-family: 'helvetica neue', helvetica, sans-serif;
    font-size: 12px;
    font-weight: 500;
    border-collapse: collapse;
    border-spacing: 0;
}

.polls3 table thead tr {
    border-bottom: 1px solid #222;
}

.polls3 table thead tr th {
    text-transform: uppercase;
    font-weight: 500;
    vertical-align: bottom;
    text-align: left !important;
}

.polls3 table thead tr th.rotate {
    height: 65px;
    width: 41px;
    padding: 0;
    position: relative;
}

.polls3 table thead tr th.rotate>div {
    position: absolute;
    left: 0;
    top: 0;
}

.polls3 table thead tr th.rotate>div svg line {
    stroke-width: 1;
    stroke: #cdcdcd;
}

.polls3 table tbody tr td {
    vertical-align: middle;
}

.polls3 table tbody tr td.dates {
    padding-left: 5px;
    min-width: 90px;
    font-size: 11px;
    text-transform: uppercase;
    color: #999;
    text-align: left;
}

.polls3 table tbody tr td.just-text {
    padding-left: 5px;
    min-width: 80px;
    font-size: 13px;
    text-align: left;
}

.polls3 table tbody tr td.grade {
    text-align: center;
    padding-left: 10px;
    border-right: 1px solid #222;
    width: 70px;
    min-width: 70px;
    font-size: 11px;
}

.polls3 table tbody tr td.grade>div {
    border: 2px solid;
    border-radius: 50%;
    height: 30px;
    width: 30px;
    font-weight: bold;
    margin-left: auto;
    margin-right: auto;
}

.polls3 table tbody tr td.sample {
    width: 65px;
    min-width: 65px;
    font-size: 13px;
    text-align: right;
    font-family: "DecimaMonoPro", monospace;
    margin-right: 5px;
    padding-left: 5px;
    text-transform: uppercase;
}

.polls3 table tbody tr td.weight {
    font-size: 13px;
    text-align: right;
    font-family: "DecimaMonoPro", monospace;
    width: 90px;
    min-width: 90px;
    border-right: 1px solid #222;
    text-transform: uppercase;
    padding-left: 5px;
}

.signal {
    width: 35px;
    height: 18px;
    margin: 0;
    padding: 0;
    display: table;
    float: left;
}

.bar {
    margin-left: 5%;
    padding: 0;
    vertical: align-bottom;
    width: 12%;
    display: inline-block;
}

.polls3 table tbody tr td.heat {
    padding: 0;
}

.polls3 table tbody tr td.heat>div {
    width: 40px;
    min-width: 40px;
    height: 50px;
    font-family: "DecimaMonoPro", monospace;
    font-size: 13px;
    display: table-cell;
    vertical-align: middle;
    text-align: center;
}

.polls3 table tbody tr td.adj-leader {
    width: 65px;
    min-width: 65px;
    font-weight: 700;
    font-size: 13px;
    text-align: left;
    padding-left: 5px;
}

</style>"""

#template = Template(fivethirtyeight_template)

#rows = (
#    test_rankings
#    .to_dict(orient='records')
#)[:12]   
    
#html = template.render(cols=columns, rows=rows)



#components.html(html)