# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import json

from psutil import cpu_count, virtual_memory

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from teska_monitor import telemetry


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })


#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Monitoring Dashboard'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    html.Button("Refresh", id = "refresh-button"),


    html.Pre(html.Code("waiting for data", id = "output")),

    dcc.Graph(
        id='example-graph',
    ),

    dcc.Graph(
        id='bullet-graph',
    )
])
@app.callback(
    Output(component_id='output', component_property='children'),
    Output(component_id= 'example-graph', component_property='figure'),
    Output(component_id= 'bullet-graph', component_property= 'figure'),
    Input(component_id= 'refresh-button', component_property='n_clicks')
)
def update_output_div(input_value):
    data = telemetry.get_all()

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = data["cpu_usage"],
        delta = {'reference': 100},
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "CPU Usage"},
        gauge = {'axis': {'range': [0, 100]}}
    ))

    labels = ["used memory", "free memory"]
    values = [data["virtual_memory"], 100 - data["virtual_memory"]]
    
    figs = go.Figure(data=[go.Pie(labels=labels, values=values)])


    return 'Output: {}'.format(data), fig, figs





# labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
# values = [4500, 2500, 1053, 500]

# fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

if __name__ == '__main__':
    app.run_server(debug=True)