import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output, State
import numpy as np

df = pd.read_excel('data/All_data.xlsx')
bins = np.array([10,20,30,40,50,60,70,80,90,100])
df['Age'] = 2019 - (df['survey/Group1A/year'] - 57)
df['Age_group'] = pd.cut(df.Age,bins)
df['Age_group'] = df['Age_group'].astype(str)

app = dash.Dash()
application = app.server

app.layout = html.Div([
    html.Div(id="table1"),

    html.Div([
        dcc.RadioItems(id='submit-button' ,
        options = [
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'} ], value='MTL'               
    )
    ]),    

])

@app.callback(Output('table1','children'),
            [Input('submit-button','value')],
                )
def update_datatable(select_radio):            
    if 'NYC' in select_radio:                            
        dfgb = pd.DataFrame(df.Age.describe()).T
        data = dfgb.to_dict('rows')
        columns =  [{"name": i, "id": i,} for i in (dfgb.columns)]
        print(data)
        return dt.DataTable(data=data, columns=columns)


if __name__ == '__main__':
    application.run(debug=True, port=8080)