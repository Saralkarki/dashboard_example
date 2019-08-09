import os
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_table

import plotly.graph_objs as go

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True

global_df = pd.read_csv('data/data.xlsx')
app.layout = html.Div([
    dcc.Graph(id='graph'), 
    html.Table(id='table'),
    dcc.Dropdown(id='dropdown'),
    html.Div(id='intermediate-value', style={'display': 'none'})
])

@app.callback(Output('intermediate-value', 'children'), [Input('dropdown', 'value')])
def clean_data(value):
     # some expensive clean data step
     cleaned_df = your_expensive_clean_or_compute_step(value)
     return cleaned_df.to_json() # or, more generally, json.dumps(cleaned_df)

@app.callback(Output('graph', 'figure'), [Input('intermediate-value', 'children'])
def update_graph(jsonified_cleaned_data):
    dff = pd.read_json(jsonified_cleaned_data) # or, more generally json.loads(jsonified_cleaned_data)
    figure = create_figure(dff) 
    return figure

@app.callback(Output('table', 'children'), [Input('intermediate-value', 'children'])
def update_table(jsonified_cleaned_data):
    dff = pd.read_json(jsonified_cleaned_data) # or, more generally json.loads(jsonified_cleaned_data)
    table = create_table(dff) 
    return table

if __name__ == "__main__":
    app.run_server(debug=True)


