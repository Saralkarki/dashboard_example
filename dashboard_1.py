import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


df = pd.read_excel('data/All_data.xlsx')

## For Ward counts ###
df_1 = pd.DataFrame(df.groupby(['ward'])['ward'].count())
x = df_1.index
y = df_1.ward
df_2 = pd.DataFrame({'x': x, 'y': y})
df_2.head()
#########

#Bootstrap CSS

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.title = "NEPAL FERTILIZER FINAL"

app.layout = html.Div([
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

        html.Div([
            html.Br([]),
            html.Br([]),
        ])
    ], className = "row"),
    html.Div([ 
        html.Div([
            dcc.Graph(
            id = 'first-graph',
            figure= {
                'data': [go.Bar(x=df_2['x'],y=df_2['y'],textposition='auto')],
                'layout': {
                'title': "First graph",
                 'xaxis' : dict(
                     title="wards",
                     titlefont=dict(family = 'monospace'),
                     size= 20,
                     color="#000000",
                     tickangle = 15
                 ),
                 
                }
            }       
        ),
        ],  className = 'six columns'),

        html.Div([
            dcc.Graph(
            id = 'second-graph',
            figure= {
                'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
            ],
                'layout': {
                'title': "second graph"
                }
            }       
        ),
        ],  className = 'six columns')
    ], className = 'row')       
], )

if __name__ == "__main__":
    app.run_server(debug=True)



