from dash.dependencies import Input, Output, State

from app import app
import plotly.graph_objs as go
from data import df_2,df_3,df_4



## graph ##
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

##upload file ##
from upload_file import parse_contents
@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children