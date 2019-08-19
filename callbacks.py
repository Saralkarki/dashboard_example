from dash.dependencies import Input, Output, State
import dash_table as dt

import pandas as pd
from app import app
import plotly.graph_objs as go
from data import (df_all_gender,df_mun_1_gender,df_mun_2_gender, df_mun_3_gender,
                  df,df_mun_1_caste, df_all_caste,df_mun_2_caste,df_mun_3_caste,
                  df_mun_1_ft,df_mun_2_ft,df_mun_3_ft,df_all_family_type,
                  df_age_group, df_mun_1_ag,df_mun_2_ag, df_mun_3_ag)


# @app.callback(Output('my-div', 'data'),
#             [Input('mun_select','value')]
#             )
# def display_val(input_mun):
#     return "{}".format(input_mun)

@app.callback(Output('my-div','children'),
    [Input('mun_select','value'),
    Input('dem_var_select', 'value')],
)
def update_datatable(input_mun, input_dem_var): 
    style_cell={'textAlign': 'right', 
     'minWidth': '30px', 'width': '30px', 'maxWidth': '40px',}

    
    style_as_list_view=True
    style_header={'backgroundColor': 'white','fontWeight': 'bold'}
    if 'All' in input_mun:
        if 'Gender' in input_dem_var:
            data = df_all_gender.to_dict('rows')
            columns = [{'name': 'Gender', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)
        if 'Caste' in input_dem_var:
            data = df_all_caste.to_dict('rows')
            columns = [{'name': 'Caste', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)
        
        if 'Family Type' in input_dem_var:
            data = df_all_family_type.to_dict('rows')
            columns = [{'name': 'Family Type', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)
        if 'Age Group' in input_dem_var:
            data = df_age_group.to_dict('rows')
            columns = [{'name': 'Age Group', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)
        # print(data)

    if 'Bansgadi' in input_mun:
        if 'Gender' in input_dem_var:
            data = df_mun_1_gender.to_dict('rows')
            columns = [{'name': 'Gender', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)                       
        if 'Caste' in input_dem_var:
            data = df_mun_1_caste.to_dict('rows')
            columns = [{'name': 'Gender', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)
        
        if 'Family Type' in input_dem_var:
            data = df_mun_1_ft.to_dict('rows')
            columns = [{'name': 'Family Type', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)
        if 'Age Group' in input_dem_var:
            data = df_mun_1_ag.to_dict('rows')
            columns = [{'name': 'Age Group', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)

    if 'Barabardiya' in input_mun:                            
        if 'Gender' in input_dem_var:
            data = df_mun_2_gender.to_dict('rows')
            columns = [{'name': 'Gender', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)                       
        if 'Caste' in input_dem_var:
            data = df_mun_2_caste.to_dict('rows')
            columns = [{'name': 'Caste', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)
        
        if 'Family Type' in input_dem_var:
            data = df_mun_2_ft.to_dict('rows')
            columns = [{'name': 'Family Type', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)
        if 'Age Group' in input_dem_var:
            data = df_mun_2_ag.to_dict('rows')
            columns = [{'name': 'Age Group', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)

    if 'Badaiyataal' in input_mun:                            
        if 'Gender' in input_dem_var:
            data = df_mun_3_gender.to_dict('rows')
            columns = [{'name': 'Gender', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)                            
        if 'Caste' in input_dem_var:
            data = df_mun_3_caste.to_dict('rows')
            columns = [{'name': 'Caste', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)
        
        if 'Family Type' in input_dem_var:
            data = df_mun_3_ft.to_dict('rows')
            columns = [{'name': 'Family Type', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)
        if 'Age Group' in input_dem_var:
            data = df_mun_3_ag.to_dict('rows')
            columns = [{'name': 'Age Group', 'id': 'x'}, {'name': 'Count', 'id': 'y'}]
            # columns = [{"name": "{}".format(input_dem_var),"id": i,} for i in (df_all_gender.columns)]
            return dt.DataTable(data=data, columns=columns, style_cell = style_cell, style_header = style_header)

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


    

