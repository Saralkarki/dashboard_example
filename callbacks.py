from dash.dependencies import Input, Output, State

from app import app
import plotly.graph_objs as go
from data import df,df_2,df_3,df_4

        
# ## Option select callback
from index import wards_options
@app.callback(Output('dem_var_select', 'options'),
              [Input('mun_select', 'value')]
)
def set_variable(selected_muni):
    return [{'label': k, 'value': k } for k in wards_options[selected_muni]]



    ###

## graph ##
# @app.callback(
#      Output('first-graph', 'figure'),
#     [Input('mun_select', 'value'),
#     Input('dem_var_select','value')]
# )
# def update_count(input_mun, input_dem_var):
#     data = []
#     if 'Bansgadi' in input_mun:
#         if 'Gender' in input_dem_var:
#             data = df_2
#     elif 'Barabardiya' in input_mun: 
#         if 'Gender' in input_dem_var:
#             data = df_3
#     elif 'Badaiyaataal' in input_mun:
#         if 'Gender' in input_dem_var:
#             data = df_4
#     else:
#         data = df_2  
#     figure = {
#     'data': [go.Bar(x=data['x'],y=data['y'],textposition='auto')],
#     'layout': {
#                 'title': "Graphing {} Count".format(input_mun),
#                  'xaxis' : dict(
#                      title="{}".format(input_mun),
#                      titlefont=dict(family = 'monospace'),
#                      size= 20,
#                      color="#000000",
#                      tickangle = 15
#                  ),
                 
#                 }
#     }
#     return figure

# ##upload file ##
# from upload_file import parse_contents
# @app.callback(Output('output-data-upload', 'children'),
#               [Input('upload-data', 'contents')],
#               [State('upload-data', 'filename'),
#                State('upload-data', 'last_modified')])
# def update_output(list_of_contents, list_of_names, list_of_dates):
#     if list_of_contents is not None:
        
#         children = [
#             parse_contents(c, n, d) for c, n, d in
#             zip(list_of_contents, list_of_names, list_of_dates)]
#         return children


    

