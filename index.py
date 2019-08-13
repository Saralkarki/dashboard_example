import os
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import plotly.graph_objs as go
from data import df,df_2,df_3,df_4

from app import server
from app import app
import callbacks
import demographic_callback
import base64
import datetime

#Bootstrap CSS
server = app.server

wards_options = {'Bansgadi':['Gender'], 'Barabardiya': ['Gender'], 
                'Badaiyataal': ['Gender'], 
                'All': ['Gender']
                }

dropdown_var = [{'label': 'Gender', 'value': 'Gender' } ]

app.title = "NEPAL FERTILIZER FINAL"

app.layout = html.Div([
#     html.Div([
#     dcc.Upload(
#         id='upload-data',
#         children=html.Div([
#             'Drag and Drop or ',
#             html.A('Select Files')
#         ]),
#         style={
#             'width': '100%',
#             'height': '60px',
#             'lineHeight': '60px',
#             'borderWidth': '1px',
#             'borderStyle': 'dashed',
#             'borderRadius': '5px',
#             'textAlign': 'center',
#             'margin': '10px'
#         },
#         # Allow multiple files to be uploaded
#         multiple=True
#     ),
#     html.Div(id='output-data-upload'),
# ]),
    

    html.Div([
        html.Br([]),
        html.Div([
            html.H1(children = "IFPRI NEPAL FERTILIZER FINAL - DASHBOARD" , className="nine columns",
            style = {
                'color': '#000000',
                'fontsize':'32px',
                'text-align': 'center',
                'margin-top': '40px'

            },
            ),
            html.Img(
                src = "https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.ictsdsymposium.org%2Fwp-content%2Fuploads%2F2013%2F08%2FIFPRI_Logo_4L_Gn-Bx.png&f=1",
                className = "three columns",
                style={
                    'height': '10%',
                    'width': '10%',
                    'float':'left',
                    'position':'relative',
                    'margin-top': '40px'
                },
            )
            # html.Div(children = '''Graphs for all required variables''')
        ]),

        html.Div([html.Div([
            html.H5('Select Municipality', style={
                'color': '#000000',
                'fontsize':'49px',
                'text-align': 'center',
                'margin-top': '40px'
            }),
            dcc.RadioItems(
                id = 'mun_select',
        options=[{'label': k, 'value': k } for k in wards_options.keys()],
    value= 'All',
    labelStyle={'display': 'inline-block', 'text-align': 'center'},   
    # When the app starts what value is selected
)  ,
html.Br([]),
dcc.Dropdown(
    id = 'dem_var_select',
    value = 'Gender',
    clearable=False
)
        ])
    ], className = "five columns"),
    ], className = "row"),

    html.Div([       
        html.Div([
            html.H2('Survey Demographic Data',
            style = {
                'color': '#000000',
                'fontsize':'32px',
                'text-align': 'center',
                'margin-top': '40px'
            }),
            dcc.Graph(
            id = "demographic_graph"
        )
        ], className = "six columns "),
        html.Div([
            html.H2('Survey Summary Data',
            style = {
                'color': '#000000',
                'fontsize':'32px',
                'text-align': 'center',
                'margin-top': '40px'
            }),
        ], className = "six columns")
    ], className = 'row'),
    
    # html.Div([ 
    #     html.Div([
    #         dcc.Graph(
    #         id = 'first-graph',    
    #     ),
    #     ],  className = 'six columns'),

    #     html.Div([
    #         dcc.Graph(
    #         id = 'second-graph',
    #         figure= {
    #             'data': [
    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
    #             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
    #         ],
    #             'layout': {
    #             'title': "second graph"
    #             }
    #         }       
    #     ),
    #     ],  className = 'six columns')
    # ], className = 'row')       
])

if __name__ == "__main__":
    app.run_server(debug=True)



