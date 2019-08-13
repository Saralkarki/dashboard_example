from dash.dependencies import Input, Output, State
import dash_table as dt

import pandas as pd
from app import app
import plotly.graph_objs as go
from data import df,df_mun_1,df_mun_2,df_mun_3


# @app.callback(Output('my-div', 'data'),
#             [Input('mun_select','value')]
#             )
# def display_val(input_mun):
#     return "{}".format(input_mun)

@app.callback(Output('my-div','children'),
    [Input('mun_select','value')],
)
def update_datatable(input_mun): 
    style_cell={'textAlign': 'left', 'padding':'5px'}
    style_as_list_view=True
    style_header={'backgroundColor': 'aqua','fontWeight': 'bold'}


    if 'All' in input_mun:                            
        dfgb = pd.DataFrame(df.Age.describe()).T
        data = dfgb.to_dict('rows')
        columns =  [{"name": i, "id": i,} for i in (dfgb.columns)]
        # print(data)
        return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)
        # print(data)
    if 'Bansgadi' in input_mun:                            
        dfgb = pd.DataFrame(df_mun_1.Age.describe()).T
        data = dfgb.to_dict('rows')
        columns =  [{"name": i, "id": i,} for i in (dfgb.columns)]
        # print(data)
        return dt.DataTable(data=data, columns=columns)
        # print(data)
    if 'Barabardiya' in input_mun:                            
        dfgb = pd.DataFrame(df_mun_2.Age.describe()).T
        data = dfgb.to_dict('rows')
        columns =  [{"name": i, "id": i,} for i in (dfgb.columns)]
        # print(data)
        return dt.DataTable(data=data, columns=columns,)

        # print(data)
    if 'Badaiyataal' in input_mun:                            
        dfgb = pd.DataFrame(df_mun_3.Age.describe()).T
        data = dfgb.to_dict('rows')
        columns =  [{"name": i, "id": i,} for i in (dfgb.columns)]
       
        return dt.DataTable(data=data, columns=columns)      
# Get the demographic options
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


    

