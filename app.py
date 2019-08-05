import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import plotly.graph_objs as go
from data import df_2,df_3,df_4

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

        html.Div([html.Div([
            dcc.Dropdown(
                id = 'dropdown_1',
        options=[
        {'label': 'Wards', 'value': 'ward'},
        {'label': 'Municipality', 'value': 'municipality'},
        {'label': 'Surveyor ID', 'value': 'surveyor id'}
    ],
    value='ward',
    clearable=False,
    placeholder="Select a city",
    searchable = False
    # labelStyle = {'display': 'inline-block'},
    # When the app starts what value is selected
)  ,
        ])
    ], className = "two columns"),
    ], className = "row"),
    
    html.Div([ 
        html.Div([
            dcc.Graph(
            id = 'first-graph',    
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

### Callbacks
@app.callback(
     Output('first-graph', 'figure'),
    [Input('dropdown_1', 'value')]
)
def update_count(selector):
    data = []
    if 'ward' in selector:
        data = df_2
    if 'municipality' in selector:
        data = df_3
    if 'surveyor id' in selector:
        data = df_4
   
    figure = {
    'data': [go.Bar(x=data['x'],y=data['y'],textposition='auto')],
    'layout': {
                'title': "Graphing {} Count".format(selector),
                 'xaxis' : dict(
                     title="{}".format(selector),
                     titlefont=dict(family = 'monospace'),
                     size= 20,
                     color="#000000",
                     tickangle = 15
                 ),
                 
                }
    }
    return figure



if __name__ == "__main__":
    app.run_server(debug=True)



