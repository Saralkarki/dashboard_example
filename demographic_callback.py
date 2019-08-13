from dash.dependencies import Input, Output, State
import dash_html_components as html

from app import app
import plotly.graph_objs as go
# demographic data import
from data import (df_all_gender,df_mun_1_gender,df_mun_2_gender, df_mun_3_gender,
                  df,df_mun_1_caste, df_all_caste,df_mun_2_caste,df_mun_3_caste,
                  df_mun_1_ft,df_mun_2_ft,df_mun_3_ft,df_all_family_type,
                  df_age_group, df_mun_1_ag,df_mun_2_ag, df_mun_3_ag)


# # Assign color to legend
colors = ["#001f3f","#0074d9","#3d9970","#111111","#01ff70","#ffdc00","#ff851B","#ff4136","#85144b",
"#f012be","#b10dc9","#AAAAAA","#111111",]
colormap = {}
for ind, formation_name in enumerate(df["survey/caste"].unique().tolist()):
    colormap[formation_name] = colors[ind]


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
        if 'Caste' in input_dem_var:
            data = df_mun_1_caste
        if 'Family Type' in input_dem_var:
            data = df_mun_1_ft
        if 'Age Group' in input_dem_var:
            data = df_mun_1_ag

    elif 'Barabardiya' in input_mun: 
        if 'Gender' in input_dem_var:
            data = df_mun_2_gender
        if 'Caste' in input_dem_var:
            data = df_mun_2_caste
        if 'Family Type' in input_dem_var:
            data = df_mun_2_ft
        if 'Age Group' in input_dem_var:
            data = df_mun_2_ag

    elif 'Badaiyataal' in input_mun:
        if 'Gender' in input_dem_var:
            data = df_mun_3_gender
        if 'Caste' in input_dem_var:
            data = df_mun_3_caste
        if 'Family Type' in input_dem_var:
            data = df_mun_3_ft
        if 'Age Group' in input_dem_var:
            data = df_mun_3_ag

    elif 'All' in input_mun:
        if 'Gender' in input_dem_var:
            data = df_all_gender 
        if 'Caste' in input_dem_var:
            data = df_all_caste
        if 'Family Type' in input_dem_var:
            data = df_all_family_type
        if 'Age Group' in input_dem_var:
            data = df_age_group
    figure = {
    'data': [go.Bar(x=data['x'],y=data['y'],marker={"color": colors} ,textposition='auto')],
    'layout': {
                'title': "Graphing {} {} Count".format(input_mun, input_dem_var),
                 'xaxis' : dict(
                     title="{}".format(input_mun),
                     titlefont=dict(family = 'monospace'),
                     size= 20,
                     color="#000000",
                     tickangle = 15,
                     sorted = False

                 ),
                 
                }
    }
    return figure

