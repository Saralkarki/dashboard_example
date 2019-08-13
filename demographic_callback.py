from dash.dependencies import Input, Output, State
import dash_html_components as html

from app import app
import plotly.graph_objs as go
from data import df_all_gender,df_mun_1_gender,df_mun_2_gender, df_mun_3_gender
import plotly.io as pio


## Gender Graph ##
@app.callback(
     Output('demographic_graph', 'figure'),
    [Input('mun_select', 'value'),
    Input('dem_var_select', 'value')]
)
def update_count(input_mun, input_dem_var):
    data = []
    if 'Bansgadi' in input_mun:
        if 'Gender' in input_dem_var:
            data = df_mun_1_gender
    elif 'Barabardiya' in input_mun: 
        if 'Gender' in input_dem_var:
            data = df_mun_2_gender
    elif 'Badaiyataal' in input_mun:
        if 'Gender' in input_dem_var:
            data = df_mun_3_gender
    else:
        data = df_all_gender 
    figure = {
    'data': [go.Bar(x=data['x'],y=data['y'],textposition='auto')],
    'layout': {
                'title': "Graphing {} {} Count".format(input_mun, input_dem_var),
                 'xaxis' : dict(
                     title="{}".format(input_mun),
                     titlefont=dict(family = 'monospace'),
                     size= 20,
                     color="#000000",
                     tickangle = 15,

                 ),
                 
                }
    }
    return figure

